"""
MIT License

Copyright (c) 2020 William A Pringle

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import sys
import os
import copy
import math
import pprint


def dbg(*kargs):
#    print(*kargs)
    return


def report(*kargs):
    dbg(*kargs)
    return


def flatten(lst):
    p = []
    for l in lst:
        p += flatten(l) if isinstance(l, list) else [l]
    return p


def getSubTotals(target, num_list_list, sofar, use_exclude, exclude):
    """
    return those sets of numbers that add up to target, selected from numListList. 
    Used to eliminate candidates in numListList that cant be used to get target.
    The web version replaces this with its js equivalent as it is a bit faster.
    """
    if num_list_list == []:
        if target == 0:
            sofar.append(exclude)

    else:
        for y in num_list_list[0]:
            if not use_exclude or y not in exclude:
                getSubTotals(target - y, num_list_list[1:], sofar, use_exclude, exclude + [y])
    return sofar


def unpack(x, y):
    """ Used to unpack test samples that are entered offline """
    def r(a):
        while True:
            yield a

    def s(c):
        a, b = c
        for i in range(b):
            yield a + i

    tt = (isinstance(x, tuple), isinstance(y, tuple))
    if tt == (False, False):
        yield (x, y)
    elif tt == (False, True):
        for z in zip(r(x), s(y)):
            yield z
    elif tt == (True, False):
        for z in zip(s(x), r(y)):
            yield z
    elif tt == (True, True):
        for a in s(x):
            for z in zip(r(a), s(y)):
                yield z


def unpackGroup(squares):
    res = []
    for i, j in squares:
        for q in unpack(i, j):
            if q not in res:
                res.append(q)
    return res


########################################################################
class KillerSudoku:
    """Methods to solve the Killer Sudoku """

    # ----------------------------------------------------------------------
    board = {}
    board_size = 0
    grid_size = 0
    line_total = 0
    rows = {}
    cols = {}
    grids = {}
    turbo = False

    def grid(self, x, y):
        gx = (x - 1) // self.grid_size
        gy = (y - 1) // self.grid_size
        return self.grid_size * gx + gy + 1

    def __init__(self, boardSize):
        """Constructor"""
        #
        # each row,column and grid has a set of possible values. As a value is
        # entered it can be eliminated from set of possibles.
        # First create these sets of possibles.
        #
        self.grid_size = int(math.sqrt(boardSize))
        # this is the grid size, eq for a 9 x 9 puselfle the grid size is 3
        self.board = {}  # possibles per square
        self.board_size = range(1, boardSize + 1)
        self.line_total = boardSize * (boardSize + 1) // 2
        values = set([p for p in self.board_size])
        for r in self.board_size:
            for c in self.board_size:
                self.board[(r, c)] = copy.copy(values)
        self.last_inner = {}
        self.last_outer = {}
        self.found_sofar = set()
        """Helpers"""
        for x in self.board_size:
            self.rows[x] = set((r, c) for (r, c) in self.board.keys() if c == x)
            self.cols[x] = set((r, c) for (r, c) in self.board.keys() if r == x)
            self.grids[x] = set((r, c) for (r, c) in self.board.keys() if self.grid(r, c) == x)
        return

    def load(self, boxes):
        """ Load and validate the puzzle """
        def getrcg(cage):
            """ get the rows, columns and grids that a cage intersects"""
            rows = set()
            cols = set()
            grids = set()
            for (row, col) in cage:
                g = self.grid(row, col)
                rows |= {row}
                cols |= {col}
                grids |= {g}
            return rows, cols, grids

        self.cage_list = []

        test_box = set(self.board.keys())
        boxTotal = 0
        for (box_count, squares) in boxes:
            boxTotal += box_count
            if isinstance(squares, tuple):
                squares = [squares]
            cage = unpackGroup(squares)
            rows, cols, grids = getrcg(cage)
            s = set(cage)
            if s <= test_box:
                test_box -= s
            else:
                err = (test_box & s) ^ s
                raise Exception("Duplicate", box_count, err)

            self.cage_list.append((box_count, cage, rows, cols, grids))

        if len(test_box) != 0:
            raise Exception("Missing", test_box)

        if boxTotal != self.line_total * max(self.board_size):
            raise Exception("Incorrect total", boxTotal - 405)
        self.inners = list(self.getInners())
        self.outers = list(self.getOuters())
        self.oldt = 0
        return

    def collect(self, fun):
        tot = 0
        b = []
        for itm in filter(fun, self.cage_list):
            tot += itm[0]
            b += itm[1]
        return (tot, set(b))

    def getInners(self):
        """ look for rows, columns or squares that completely enclose a number of cages. We can calculate the 
            required total for the free squares
        """
        for (box_count, cage, rows, cols, squares) in self.cage_list:
            yield box_count, cage
        for rcg, full in [(3, self.rows), (2, self.cols), (4, self.grids)]:  # numbers correspond to position in cage tuple
            for x in self.board_size:
                tot, b = self.collect(lambda p: p[rcg] == {x})  # fully enclosed cages
                target = list(full[x] - b)
                if len(target) > 0 and tot < self.line_total:
                    yield((self.line_total - tot, target))

    def getOuters(self):
        """ Look for cages that just overflow a grid or lines
            Duplicates are allowed in the cells found
        """
        lmt = 10
        doubles = []
        for x in self.board_size:
            for j in [1, 3]:
                if x + j <= max(self.board_size):
                    doubles += [{x, x + j}]

        for rcg, full in [(2, self.cols), (3, self.rows), (4, self.grids)]:
            for x in self.board_size:
                (tot, b) = self.collect(lambda p: p[rcg] >= {x})  # cage intersect rcg
                target = list(b - full[x])
                if len(target) < lmt:  # ignore rcg with outrageous overflows
                    yield tot - self.line_total, target

                """ The following were added to pick up overflows/underflows for multiple adjacent lines or grids 
                    Duplicates allowed
                """

                if rcg != 4 and x < max(self.board_size):
                    """ Check adjacent rows & columns """
                    (tot, b) = self.collect(lambda p: not p[rcg].isdisjoint({x, x + 1}))  # check overflows
                    target = list(b - (full[x] | full[x + 1]))
                    if len(target) < lmt:
                        yield tot - 2 * self.line_total, target

                if rcg != 4 and x < max(self.board_size):  # moved from inner as can have duplicates
                    s = {x}
                    tt = copy.copy(full[x])
                    for p in range(x + 1, max(self.board_size)):
                        s |= {p}
                        tt |= full[p]
                        (tot, b) = self.collect(lambda p: p[rcg] <= s)  # check underflows
                        target = sorted(list(tt - b))
                        if len(b) > 2 * max(self.board_size) - lmt:
                            yield len(s) * self.line_total - tot, target

            if rcg == 4:  # moved from inner as can have duplicates
                for g in [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}] + doubles if max(self.board_size) == 9 else []:
                    (tot, b) = self.collect(lambda p: p[rcg] <= g)  # contained in contiguous grids
                    if len(b) > len(g) * max(self.board_size) - lmt:
                        target = set()
                        for k in g:
                            target |= full[k]
                        target -= b
                        t2 = list(set(flatten([list(full[k]) for k in g])) - b)
                        yield len(g) * self.line_total - tot, list(target)

            if rcg == 4:
                for g in [{1, 2, 3}, {4, 5, 6}, {7, 8, 9}, {1, 4, 7}, {2, 5, 8}, {3, 6, 9}] + doubles if max(self.board_size) == 9 else []:
                    (tot, b) = self.collect(lambda p: not p[rcg].isdisjoint(g))  # overflow contiguous groups
                    t2 = list(b - set(flatten([list(full[k]) for k in list(g)])))
                    target = b
                    for k in g:
                        target -= full[k]
                    if len(target) < lmt:
                        yield tot - len(g) * self.line_total, list(target)

    def squeeze(self, n, cage, use_exclude=True):
        """ remove candidate numbers from squares if they cant be used to for totals that a cage contributes to 
        """
        limit = 6 if self.turbo else 3  # start off with quick scan for speed, go deeper if needed.
        if len([s for s in cage if len(s) > 1]) > limit:
            # if not self.turbo:
                dbg("reject ", cage)
                return None
        ll = [list(l) for l in list(map(self.board.get, cage))]
        solutions = getSubTotals(n, ll, [], use_exclude, [])
        ll = list(map(set, zip(*solutions)))
        i = 0
        for s in ll:

            before = self.board[cage[i]]
            after = before & set(s)
            if after < before:
                dbg("Squeeze", cage[i], "from", before, "by", set(s), "to", after)
                zz = 1

            self.board[cage[i]] &= set(s)
            i += 1

        return ll

    def removeSingleNumbers(self):
        """ Classic sudoku. Given a singleton, remove from intersecting lines and grids 
        """
        def removeSingleNumber(k, n):
            x, y = k
            sn = {n}
            cells = self.rows[y] | self.cols[x] | self.grids[self.grid(x, y)]
            foundMore = False
            for c in cells:
                if k == c:
                    self.board[c] = sn
                elif n in self.board[c]:
                    self.board[c] -= sn
                    foundMore = True
                    dbg("rule 1 removes", c, n)
                    if len(self.board[c]) == 0:
                        #
                        # We've eliminated all possibles, Oops.
                        #
                        print("fatal %d %d" % (x, y))
                        raise Exception("No Solution")
            return foundMore

        foundOne = True
        while foundOne:
            foundOne = False
            for k, v in self.board.items():
                if len(v) == 1:
                    if k not in self.found_sofar:
                        self.found_sofar |= {k}
                        dbg("singleton found", k, v)
                        foundOne = removeSingleNumber(k, v.pop())
                        # repeat while singletons keep appearing

    def rule2(self):
        #
        # Rule 2 states that a value must go somewhere, ie each row, column and grid
        # must contain a complete set of values. If there is only one place a value
        # can go, then put it there.
        #
        # This is not very efficient, but Hey - it works.
        #
        for x in self.board_size:
            for y in self.board_size:
                if len(self.board[(x, y)]) > 1:
                    #
                    # look for unresolved squares
                    #
                    g = self.grid(x, y)
                    for full in [self.rows[y], self.cols[x], self.grids[g]]:
                        target = copy.copy(self.board[(x, y)])
                        for rc in full:
                            if rc != (x, y):
                                # print(target,self.board[rc])
                                target -= self.board[rc]
                                if target == set():
                                    break
                        if target != set():
                            dbg("Rule 2 finds", (x, y), target)
                            self.board[(x, y)] = target
                            break

        #
        # repeat for all squares
        #
        return True

    def rule3(self):
    #
    # Rule 3 states that if a row, column or grid contains 2 squares with the same options
    # then these options can be eliminated from other squares in the group.
    #
        def purge(index):
            doubles = {}
            removed = 0
            for i in index:
                l = len(self.board[i])
                if l > 1 and l <= 4:
                    t = tuple(self.board[i])
                    doubles[t] = doubles.get(t, 0) + 1  # count occurrences of t

            for dl in doubles:
                if len(dl) == doubles[dl]:
                    for i in index:
                        sbi = self.board[i]
                        s = sbi - set(dl)
                        if len(s) > 0 and len(s) != len(sbi):
                            self.board[i] = s
                            dbg("Rule 3 removes", i, sbi - s)
                            removed += 1
            return removed

        ret = 0
        for x in self.board_size:
            ret += purge(self.rows[x])  # select rows
            ret += purge(self.cols[x])  # select cols
            ret += purge(self.grids[x])  # select grids
        return ret == 0

    def solve(self):
        oldt = 0
        # pprint.pprint(self.inners)
        # pprint.pprint(self.outers)
        target = max(self.board_size) ** 2
        for i in range(40):
            t = self.iteration()
            if t == 0:
                return None
            if t == target:
                return self.get_solution()
        return None

    def iteration(self):
        """ Repeat this loop until solution emerges. 
        """
        def ccc(io, lastone, unique):
            """ Speedup routine. keeps a copy of number candidates going into a squeeze
                If nothing has changed, dont rerun squeeze
            """
            for i, (n, cage) in enumerate(io):
                    r = lastone.get(i, {99})
                    if r:
                        for a, b in zip(r, map(self.board.get, cage)):
                            if a != b:
                                lastone[i] = self.squeeze(n, cage, unique)
                                break

        ccc(self.inners, self.last_inner, True)
        ccc(self.outers, self.last_outer, False)

        self.rule2()
        self.rule3()
        self.removeSingleNumbers()
        # pprint.pprint(self.board)
        t = sum(map(len, self.board.values()))
        print(t, self.turbo)
        if self.oldt == t:
            if self.turbo:
                return 0  # failed
            else:
                # beef up search path if we have run into the sand
                # The first few iterations have seriously cleaned up the options
                # so we can go deeper
                self.last_inner = {}
                self.last_outer = {}
                self.turbo = True
        self.oldt = t
        return t

    def get_solution(self):
        return dict([(k, v.pop()) for k, v in self.board.items()])



