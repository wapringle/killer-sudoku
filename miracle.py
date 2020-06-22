import pprint,copy
import kl

def dbg(*kargs):
#    print(*kargs)
    return

def inrange(t):
    for i in range(2):
        if t[i] <1 or t[i] > 9:
            return False
    return True

def knightKingMove(t):
    def plus(t1,t2):
            return [ t1[i]+t2[i] for i in range(2) ]

    k1=[(-1,2),(1,2),(1,1)]
    for i in range(0,4):
        for a in k1:
            b=plus(a,t)
            if inrange(b):
                yield tuple(b)
        k1=[ (-y,x) for (x,y) in k1]

class Miracle(kl.KillerSudoku):
    
            
    def remove_single_number(self,k,n):
        x,y=k
        sn={n}
        cells=self.rows[y]|self.cols[x]|self.grids[self.grid(x,y)]|set(knightKingMove(k))
        foundOne=False
        for c in cells:
            if k==c:
                self.board[c]=sn
            elif n in self.board[c]:
                self.board[c]-=sn
                foundOne=True
                dbg("rule 1 removes",c,n)
                if len(self.board[c])==0:
                    #
                    # We've eliminated all possibles, Oops.
                    #
                    # Should really throw an exception.
                    print("fatal %d %d" % (x,y))
                    raise Exception("No Solution")
        neighbours={n-1,n+1}-{0,10}
        for c in filter(inrange,[(x-1,y),(x+1,y),(x,y-1),(x,y+1)]):

            before=self.board[c]
            after = before - neighbours
            if after < before:
                dbg("neighbours",c,"from",before,"by",neighbours,"to",after)
            
            self.board[c]-=neighbours
            
            if len(self.board[c])==0:
                #
                # We've eliminated all possibles, Oops.
                #
                # Should really throw an exception.
                print("fatal %d %d" % (x,y))
                raise Exception("No Solution")

        return foundOne
    
    def remove_single_numbers(self):
        """ Classic sudoku. Given a singleton, remove from intersecting lines and grids 
        """
        
        foundOne=True
        while foundOne:
            foundOne=False
            for k,v in self.board.items():
                if len(v)==1:
                    if k not in self.foundSofar:
                        self.foundSofar |= {k}
                        dbg("singleton found",k,v)
                        foundOne=self.remove_single_number(k,v.pop())
                        # repeat while singletons keep appearing
                        
        

    
    
    def checkLegal(self):
        values=set([p for p in self.boardSize])
        for rcg in [self.rows,self.cols,self.grids]:
            for x in self.boardSize:
                target=copy.copy(values)
                for a in rcg[x]:
                    target -= self.board[a]
                    if target == set():
                        break
                if target!=set():
                    dbg("checkLegal finds",rcg[x],target)
                    return False
        return True
    
    def populate(self,rc,n):
        self.board[rc]={n}
        
            
        
            
zz=Miracle(9)
""" Populate the grid with 2 numbers, the original puzzle """

zz.populate((5,3),1)
zz.populate((6,7),2)

""" A little trial & error finds these 2 will produce a solution """

zz.populate((3,6),3) 
zz.populate((9,2),4)

if not zz.checkLegal():
    i=1
oldt=0
for i in range(30):
    zz.rule2()
    zz.rule3()
    zz.remove_single_numbers()
    zz.checkLegal()
    t=sum(map(len,zz.board.values()))
    print(t)
    if not zz.checkLegal():
        break
    if t==oldt:
        break
    oldt=t
    
    
    def magic(r,c):
        if len(zz.board[(r,c)])==1:
            return str(list(zz.board[(r,c)])[0])
        else:
            return "+"
    for r in zz.boardSize:
        rw=" ".join([magic(r,c) for c in zz.boardSize])
        print(rw)


#pprint.pprint(zz.board)
i=1

            
        
