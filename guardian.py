import kl
import copy,pprint




case={
    1: (4,[
        (4,(1,(1,2))),
        (9,((2,3),1)),
        (8,[((2,2),2),(2,3)]),
        (7,[(4,(2,2)),(3,3)]),
        (7,[(1,(3,2)),(2,4)]),
        (5,((3,2),4))
        ]),
    2: (4,[
        (20,[(1,(1,3)),(2,(1,2)),(3,1),(4,(1,4))]),
        (16,[(2,(3,2)),(3,(2,3))]),
        (4,[(1,4)])
        ]),
    70: (6,[
        (14,[(1,(2,4))]),
        (14,[((1,2),1),(2,(2,2))]),
        (14,[((1,4),6)]),
        (14,[(2,(4,2)),(3,(3,2))]),
        (14,[(3,(1,2)),(4,2)]),
        
        (14,[((3,3),5),(4,4),(5,6)]),
        (14,[((4,3),1)]),
        (14,[((4,2),3),((5,2),2)]),
        (14,[(5,4),(6,(3,4))]),
        ]),
    
    80: (4,[
        (20,[(1,(1,3)),(2,(1,2)),(3,1),(4,(1,4))]),
        (20,[(1,4),(2,(3,2)),(3,(2,3))])
    ]),
    90: (5,[
        (15,[(2,(1,3)),(3,3),(4,(3,3)),(5,5)]),
        (15,[(1,(1,4)),(2,4)]),
        (15,[((1,3),5),(3,4)]),
        (15,[((3,3),1),(3,2)]),
        (15,[(5,(2,3)),(4,2)]),
         
    ]),
    3: (9,[
        (13,((1,4),1)),
        (18,[(5,(1,2)),(4,2)]),
        (24,((6,4),1)),
        (20,(1,(2,4))),
        (22,(2,(2,3))),
        (26,[(3,(2,2)),(4,(3,2))]),
        (13,((6,3),2)),
        (17,(9,(2,3))),
        (9,(5,(3,3))),
        (8,(6,(3,2))),
        (11,[((7,2),3),(7,4)]),
        (21,[(3,4),((3,2),5)]),
        (8,[(8,4),((7,2),5)]),
        (8,[(2,5),((1,2),6)]),
        (20,(6,(5,3))),
        (13,(9,(5,2))),
        (7,((3,2),6)),
        (13,[(5,(6,3)),(6,8)]),
        (24,((7,2),(6,2))),
        (18,(1,(7,3))),
        (12,((2,2),7)),
        (17,(4,(7,3))),
        (20,[(9,7),((7,3),8)]),
        (4,(2,(8,2))),
        (11,(3,(8,2))),
        (20,((5,3),9)),
        (8,((8,2),9))
    ]),
}
caseno=1


def dbg(*kargs):
    print(*kargs)
    return


def solve():
    zz=kl.KillerSudoku(case[caseno][0])
    zz.load           (case[caseno][1])
    return zz


def uniquerc(rc,y,current):
    r,c=rc
    for (r1,c1),v in current:
        if (r==r1 or c==c1) and y==v:
            return False
    return True
        
def newGetSubTotals(target, num_list_list, sofar, current):
    """
    return those sets of numbers that add up to target, selected from numListList. 
    Used to eliminate candidates in numListList that cant be used to get target.
    The web version replaces this with its js equivalent as it is a bit faster.
    """
    #print(target)
    if target < 0:
        return sofar
    if num_list_list == []:
        if target == 0:
            sofar.append(current)

    else:
        rc,values=num_list_list[0]
        for y in values:
            if target < y:
                break
            if uniquerc(rc,y,current):
                newGetSubTotals(target - y, num_list_list[1:], sofar,  current + [(rc,y)])
    return sofar


class localSudoku(kl.KillerSudoku):
    
    def grid(self, x, y):
        return 1
    
    def squeeze(self, n, cage, use_exclude=False):
        """ remove candidate numbers from squares if they cant be used to for totals that a cage contributes to 
        """
        solutions = newGetSubTotals(n, cage, [], [])
        if len(solutions)==0:
            raise kl.Error("No Solution")
        ll=dict((k,[]) for k,v in solutions[0])
        for s in solutions:
            for k,v in s:
                ll[k].append(v)
        oldboard=dict(cage)
        for rc,v in ll.items():

            before = oldboard[rc]
            after = before & set(v)
            if after < before:
                dbg("Squeeze", rc, "from", before,  "to", after)
                if len(after)==1:
                    self.singleton_found(rc,copy.deepcopy(after))
                    pass
                zz = 1

            self.board[rc] &= after

        return ll    
    
    def removeSingleNumbers(self):
        """ Classic sudoku. Given a singleton, remove from intersecting lines and grids 
        """
        def removeSingleNumber(k, n):
            x, y = k
            sn = {n}
            try:
                cages=set([ p[1] for p in self.cage_list if k in p[1]][0])
            except IndexError:
                # in case cage doent cover this square
                cages=set()
            cages=set() ## for guardian puzzle, cages aren't unique
            cells = self.rows[y] | self.cols[x] | self.grids[self.grid(x, y)]  | cages
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
                        raise Error("No Solution")
            return foundMore

        foundOne = True
        while foundOne:
            foundOne = False
            for k, v in self.board.items():
                if len(v) == 1:
                    if k not in self.found_sofar:
                        self.singleton_found(k,v)
                    foundOne = removeSingleNumber(k, v.pop())
                        # repeat while singletons keep appearing

    

    def iteration(self):
        """ Repeat this loop until solution emerges. 
        """
        self.turbo=True
        self.limit=100
        
        for cl in self.cage_list:
            n,cage=cl[:2]
            
            self.squeeze(n,[ (l,self.board[l]) for l in cage])

        self.rule2()
        self.rule3()
        self.removeSingleNumbers()
        #self.Xget_doubles()
        pprint.pprint(self.board)
        t = sum(map(len, self.board.values()))
        #print(t, self.turbo)
        if self.oldt == t:
            if self.turbo:
                self.rule3(True)
                return 0  # failed
            else:
                # beef up search path if we have run into the sand
                # The first few iterations have seriously cleaned up the options
                # so we can go deeper
                self.limit += 3
                self.last_inner = {}
                self.last_outer = {}
                self.turbo = True
        self.oldt = t
        return t
    pass



def main():

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-t","--test", help="test number", type=int, default=80)
    parser.add_argument("-d","--debug", help="debug", action="store_true")
    args = parser.parse_args()
    cc=args.test
    zz=localSudoku(case[cc][0])
    zz.debug=args.debug
    kl.debug=args.debug
    try:
        zz.load(case[cc][1])
    except Exception as e:
        print(e.args)
        return 1
    
    zz.grids=dict((i,set()) for i in zz.board_size)
    
    zz.limit=100

    
    for t in kl.doit(zz):
        print(t)
        
        
    solution=zz.get_solution()
    if solution:
        #import pprint
        #pprint.pprint(solution)
        for r in zz.board_size:
            rw=" ".join([str(solution[(r,c)]) for c in zz.board_size])
            print(rw)
        return 0


    
    
if __name__ == '__main__':
    main()
