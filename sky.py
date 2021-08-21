import kl
import pprint,copy

import itertools,functools

bb={(1, 1): {1, 2, 3, 4},
 (1, 2): {5},
 (1, 3): {2, 3, 4},
 (1, 4): {8},
 (1, 5): {1, 2, 3, 6},
 (1, 6): {2, 3, 4, 6},
 (1, 7): {7},
 (1, 8): {1, 2, 3, 6},
 (1, 9): {9},
 (2, 1): {9},
 (2, 2): {1, 2, 3, 6, 7},
 (2, 3): {1, 2, 3},
 (2, 4): {1, 2, 3, 6, 7},
 (2, 5): {5},
 (2, 6): {2, 3, 6, 7},
 (2, 7): {1, 2, 3, 6},
 (2, 8): {8},
 (2, 9): {4},
 (3, 1): {1, 2, 3, 4},
 (3, 2): {2, 3, 4, 6, 7},
 (3, 3): {8},
 (3, 4): {9},
 (3, 5): {1, 2, 3, 6, 7},
 (3, 6): {2, 3, 4, 6, 7},
 (3, 7): {1, 2, 3, 5, 6},
 (3, 8): {1, 2, 3, 5, 6},
 (3, 9): {1, 2, 3, 5},
 (4, 1): {1, 2, 3, 4, 7},
 (4, 2): {8},
 (4, 3): {1, 2, 3, 4, 6},
 (4, 4): {1, 2, 3, 6, 7},
 (4, 5): {1, 2, 3, 6, 7},
 (4, 6): {5},
 (4, 7): {9},
 (4, 8): {1, 2, 3, 4, 6},
 (4, 9): {1, 2, 3, 6, 7},
 (5, 1): {2, 3, 4, 5, 7},
 (5, 2): {1, 2, 3, 4},
 (5, 3): {9},
 (5, 4): {1, 2, 3, 6, 7},
 (5, 5): {8},
 (5, 6): {2, 3, 6, 7},
 (5, 7): {1, 2, 3, 4, 5, 6},
 (5, 8): {1, 2, 3, 4, 5, 6},
 (5, 9): {1, 2, 3, 5},
 (6, 1): {2, 3, 5},
 (6, 2): {1, 2, 3},
 (6, 3): {1, 2, 3, 5, 6},
 (6, 4): {4},
 (6, 5): {1, 2, 3, 6, 7, 9},
 (6, 6): {2, 3, 6, 7, 9},
 (6, 7): {8},
 (6, 8): {1, 2, 3, 5, 6},
 (6, 9): {1, 2, 3, 5, 6, 7},
 (7, 1): {8},
 (7, 2): {2, 3, 4},
 (7, 3): {2, 3, 4, 5, 7},
 (7, 4): {2, 3, 5, 6, 7},
 (7, 5): {9, 2, 3, 7},
 (7, 6): {1},
 (7, 7): {2, 3, 4, 5, 6},
 (7, 8): {2, 3, 4, 5, 9},
 (7, 9): {2, 3, 5, 6},
 (8, 1): {6},
 (8, 2): {1, 2, 3},
 (8, 3): {1, 2, 3, 7},
 (8, 4): {2, 3, 5, 7},
 (8, 5): {4},
 (8, 6): {9, 2, 3, 7},
 (8, 7): {1, 2, 3, 5},
 (8, 8): {1, 2, 3, 5, 9},
 (8, 9): {8},
 (9, 1): {1, 2, 3, 4, 5},
 (9, 2): {9},
 (9, 3): {1, 2, 3, 4, 5},
 (9, 4): {2, 3, 5, 6},
 (9, 5): {2, 3, 6},
 (9, 6): {8},
 (9, 7): {1, 2, 3, 4, 5},
 (9, 8): {7},
 (9, 9): {1, 2, 3, 5, 6}}

def getProduct(num_list_list, exclude=[]):

    if num_list_list == []:
        yield exclude

    else:
        for y in num_list_list[0]:
            if y not in exclude:
                yield from getProduct(num_list_list[1:], exclude + [y])

def compatible(x,y):
    for i,v in enumerate(x):
        if v== y[i]:
            return False
        j=i - (i%3)
        if v in y[j:j+3]:
            return False
        
    for i,v in enumerate(y):
        j=i - (i%3)
        if v in x[j:j+3]:
            return False
        
    return True

def validGridSet(c4,c5,c6):
    for x4 in c4:
        for x5 in c5:
            if compatible(x4,x5):
                for x6 in c6:
                    if  compatible(x4,x6) \
                    and compatible(x5,x6):
                        grid=set()
                        
                        g1 = set(x4[:3]) | set(x5[:3]) | set(x6[:3])
                        g2 = set(x4[3:6]) | set(x5[3:6]) | set(x6[3:6])
                        g3 = set(x4[6:]) | set(x5[6:]) | set(x6[6:])
                        if len(g3)==9 and len(g2)==9 and len(g3)==9:
                            yield [x4,x5,x6]
          
    
def allowed(al,x):
    for i,v in enumerate(x):
        if v not in al[i]:
            return False
    return True

def skyfilter(l,r,omit,row2):
    lc=0
    rc=0
    lm=0
    rm=0
    
    def checkSide(c,rr):
        lc=0
        lm=0
        if c==0:
            return True
        for i,v in enumerate(rr):
            if v>lm:
                lc+=1
                if lc>c:
                    return False
                lm=v
            if v==9:
                return lc==c
        return False
        
    
    row=list(row2)
    for i,v in omit:
        row.insert(i,v)
    
    ret=checkSide(l,row) and checkSide(r,reversed(row))
    if ret:
        #print(l,r,row)
        i=1
    return ret

def ttest(row,l,r,f,t):
    omit=[]
    ov=set()
    row2=[]

    values = set([p for p in range(1,10)])
    cc=itertools.permutations(values)
    al2=functools.partial(allowed,row)
    
    legal_candidates=filter(al2,cc)


    sk2=functools.partial(skyfilter,l,r,omit)

    ret=set(( x[f-1],x[t-1])for x in filter(sk2,legal_candidates))
        
    
            
        
    return ret
def validrows(row,l,r):
    omit=[]
    ov=set()
    row2=[]
    t = sum(map(len, row))
    if t>40:
        for i,v in enumerate(row):
            if len(v)==1:
                ov |= v
                omit.append((i,list(v)[0]))
            else:
                row2 += [v]
        values = set([p for p in range(1,10)]) - ov
        cc=itertools.permutations(values)
        al2=functools.partial(allowed,row2)
        
        legal_candidates=filter(al2,cc)
    else:
        #print("Method 2")
        legal_candidates=getProduct(row)
        
    sk2=functools.partial(skyfilter,l,r,omit)
    
    def reinsert(x):
        y=list(x)
        for i,v in omit:
            y.insert(i,v)
        return y
    
                
    possibles=list(map(reinsert,filter(sk2,legal_candidates)))

    if possibles==[]:
        raise kl.Error("No Solution")

    return possibles
    

def skytest(row,l,r):
    possibles=validrows(row,l,r)
    return list(map(set,zip(*possibles)))

    
            


class Skyscraper(kl.KillerSudoku):
    def __init__(self,*args):
        super().__init__(*args)
        self.oldt=0
    def border(self,trow,brow,lcol,rcol):
        self.trow=trow
        self.brow=brow
        self.lcol=lcol
        self.rcol=rcol
        
    def square(self,tl,br):
        tr=(tl[0],br[1])
        bl=(br[0],tl[1])
        
        rows={}
        cols={}
        x=tl[0]
        rows[tl]=ttest([ copy.deepcopy(self.board[(x,y)]) for y in self.board_size], int(self.lcol[x-1]),int(self.rcol[x-1]), tl[1], tr[1])
        x=bl[0]
        rows[bl]=ttest([ copy.deepcopy(self.board[(x,y)]) for y in self.board_size], int(self.lcol[x-1]),int(self.rcol[x-1]), bl[1], br[1])

        y=tl[1]
        cols[tl]=ttest([ copy.deepcopy(self.board[(x,y)]) for x in self.board_size], int(self.trow[y-1]),int(self.brow[y-1]), tl[0], bl[0])
        y=tr[1]
        cols[bl]=ttest([ copy.deepcopy(self.board[(x,y)]) for x in self.board_size], int(self.trow[y-1]),int(self.brow[y-1]), tr[0], br[0])
        
        i=1
        
    def bigBang(self):
        bigR=[ validrows(self.getRow(x),int(self.lcol[x-1]),int(self.rcol[x-1])) for x in self.board_size]
        pp=[]
        for i in range(0,9,3):
            grids=validGridSet(*bigR[i:i+3]) 
            possibles={}
            possibles[0]=set()
            possibles[1]=set()
            possibles[2]=set()
    
            gl=list(grids)
            for j,g in enumerate(gl):
                possibles[0] |= {tuple([tuple(g[0][:3]),tuple(g[1][:3]),tuple(g[2][:3])])}
                possibles[1] |= {tuple([tuple(g[0][3:6]),tuple(g[1][3:6]),tuple(g[2][3:6])])}
                possibles[2] |= {tuple([tuple(g[0][6:]),tuple(g[1][6:]),tuple(g[2][6:])])}
            pp.append(possibles)
        return pp
            
    
    def bigCol(self):
        bigC=[ validrows(self.getCol(x),int(self.trow[x-1]),int(self.brow[x-1])) for x in self.board_size]
        pp=[]
        for i in range(0,9,3):
            grids=validGridSet(*bigC[i:i+3]) 
            possibles={}
            possibles[0]=set()
            possibles[1]=set()
            possibles[2]=set()
    
            gl=list(grids)
            for j,g in enumerate(gl):
                possibles[0] |= {tuple([tuple(g[0][:3]),tuple(g[1][:3]),tuple(g[2][:3])])}
                possibles[1] |= {tuple([tuple(g[0][3:6]),tuple(g[1][3:6]),tuple(g[2][3:6])])}
                possibles[2] |= {tuple([tuple(g[0][6:]),tuple(g[1][6:]),tuple(g[2][6:])])}
            pp.append(possibles)
        return pp
            
    
    
    def iteration(self):
        t=1
        while t!=0:
            t=super().iteration()
            print(t, self.turbo)
            
            if t==81:
                return t
        
        for x in self.board_size:
            if int(self.lcol[x-1])==0 and int(self.rcol[x-1])==0:
                continue
            #row=[ copy.deepcopy(self.board[(x,y)]) for y in self.board_size]
            newrow=skytest(self.getRow(x),int(self.lcol[x-1]),int(self.rcol[x-1]))
            for y,v in enumerate(newrow,start=1):
                assert v <= self.board[(x,y)]
                if kl.debug and self.board[(x,y)] != v:
                    print(f"sky sets {(x,y)} from {self.board[(x,y)]} to {v}")
                self.board[(x,y)] = v
                
        for y in self.board_size:
            if int(self.trow[y-1])==0 and int(self.brow[y-1])==0:
                continue
            #col=[ copy.deepcopy(self.board[(x,y)]) for x in self.board_size]
            newcol=skytest(self.getCol(y),int(self.trow[y-1]),int(self.brow[y-1]))
            for x,v in enumerate(newcol,start=1):
                assert v <= self.board[(x,y)]
                if kl.debug and self.board[(x,y)] != v:
                    print(f"sky sets {(x,y)} from {self.board[(x,y)]} to {v}")
                self.board[(x,y)] = v
            
        if kl.debug:
            pprint.pprint(self.board)
        t = sum(map(len, self.board.values()))
        print(t, self.turbo)
        if t==self.oldt:
            print("stopped")
            flag=0
            #self.square((3,3),(9,7))
            poss=self.bigBang()
            for i,p in enumerate(poss):
                for j,grid in p.items():
                    zz= [ set(p) for p in zip(*[ a + b +c for a,b,c in grid]) ]
                    if len(grid)==1:
                        if kl.debug:
                            print(f'grid {i},{j} set to {grid}')
                        flag=1
                    for x in range(3):
                        for y in range(3):
                            if self.board[(3*i+x+1),(3*j+y+1)] != zz[x*3 + y]:
                                print(f'BIG changes ({3*i+x+1},{3*j+y+1}) {self.board[(3*i+x+1),(3*j+y+1)]} to {zz[x*3 + y]}')
                                self.board[(3*i+x+1),(3*j+y+1)] = zz[x*3 + y]
                                flag=1
                                
            poss=self.bigCol()
            for i,p in enumerate(poss):
                for j,grid in p.items():
                    zz= [ set(p) for p in zip(*[ a + b +c for a,b,c in grid]) ]
                    if len(grid)==1:
                        if kl.debug:
                            print(f'grid {i},{j} set to {grid}')
                        flag=1
                    for x in range(3):
                        for y in range(3):
                            oldindex=(3*j+y+1),(3*i+x+1)
                            oldval=self.board[oldindex]
                            newindex=3*x+y
                            newval=zz[newindex]
                            if oldval != newval:
                                print(f'BIG changes {oldindex} {oldval} to {newval}')
                                self.board[oldindex] = newval
                                flag=1
                                
            if flag==1:
                return self.iteration()
                                
                    

            i=1
            return 0
        else:
            self.oldt=t
        return t
        

        
        
"""
values = set([p for p in range(1,10)])
al=[values,{1,2},values,[6],[9],values,values,values,values]
ret=skytest(al, 2, 2)
print(ret)

    
i=1
col=[{1, 2, 3, 4, 5, 7}, {1, 2, 3, 4, 5, 7}, {1, 3, 4, 5, 7, 8}, {6}, {9},  {2, 3, 4, 5, 7, 8}, {1, 2, 4, 5, 7, 8}, {1, 2, 3, 4, 7, 8}, {1, 2, 3, 4, 7, 8}]
r=skytest(col,2,2)

print(r)
i=1
    
"""    
