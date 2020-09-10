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
import copy
from  browser import document, timer, alert

import kl,ktest
#from brythonInterface import boardSize

boardSize=9

boxList=[]
gridDict={}

def tuple2id(t): return "i%d%d" % t

def id2tuple(id): return (int(id[1]),int(id[2]))

"""
for a,b in re.findall(r'def (\w*).*:\n *return (\w*)',t,flags=re.MULTILINE): print(f'    {a}={b}')

"""
class State():
    def is_clicked(self): return False
    def name(self): 
        return self.__class__.__name__
    def mousein(self):
        return None
    def mouseout(self):
        return None
    def click(self):
        return None
    def grouped(self):
        return caged()
    
class unused(State):
    background='ivory'

    def mousein(self):
        return highlight()
    
class highlight(State):
    background='#eefbff'

    def click(self):
        return clicked()
    def mouseout(self):
        return unused()
    
class clicked(State):
    background='#f33fba4d'
    
    def is_clicked(self): return True
    def grouped(self):
        return caged()
    def click(self):
        return highlight()
    def mousein(self):
        return clicked()
    def mouseout(self):
        return clicked()
    
class caged(State):
    background='beige'

    def grouped(self):
        return caged()
    def mousein(self):
        if some_cells_clicked():
            return caged()
        else:
            return higrouped()
    def click(self):
        return caged()
    
    def mouseout(self):
        return caged()
    
class higrouped(State):
    background='bisque'

    def mouseout(self):
        return caged()
    def click(self):
        return clicked()
    
    
    
    
    
class GridSquare():
    def __init__(self,id):
        self.id=id
        self.status=unused()
    def action(self,act):
        self.status=getattr(self.status,act)()

def initCell(row,column):
    global gridDict
    id=tuple2id((row,column))
    gridDict[id]=GridSquare(id)
    return id
    
def members_of_group(id,russel=False):
    for num,idList in boxList:
        if id in idList:
            return idList
    return [id] if russel else []

def remove_box_for_id(id):
    global boxList,gridDict
    for num,idList in boxList:
        if id in idList:
            boxList.remove((num,idList))
            return
    
def setCageStyle(idList,style):
    def makeEdge(t,border):
        if tuple2id(t) not in idList:
            setattr(document[id].style,border,style)
    for id in idList:
        (r,c)=id2tuple(id)
        makeEdge((r,c-1) , "borderLeft")
        makeEdge((r,c+1) , "borderRight")
        makeEdge((r-1,c) , "borderTop")
        makeEdge((r+1,c) , "borderBottom")


def get_clicked_cells():
    return sorted([k for k,v in gridDict.items() if v.status.is_clicked() ])

def some_cells_clicked():
    return False #len(get_clicked_cells())>0

def set_backGround(id,cell):
    #print(f'cell {id} class from {document[id].Class} to {cell.status.name()}')
    #document[id].Class=cell.status.name()
    
    document[id].style.backgroundColor=cell.status.background
    
def on_number_button_pressed(ev):  # wxGlade: MyFrame.<event_handler>
    
    idList=get_clicked_cells()
    if idList==[]:
        return
    
    itm=ev.currentTarget
    boxCount=int(itm.text)
    add_cage(boxCount,idList)
    
def add_cage(boxCount,idList):
    global boxList,gridDict
    for s in idList:
        b=gridDict[s]
        b.action("grouped")
        itm=document[b.id]
        set_backGround(b.id, b)
        #itm.style.backgroundColor=b.status.background()
        itm.text=""
        
    b0=gridDict[idList[0]]
    itm=document[b0.id]
    #b0.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
    itm.text=str(boxCount)
    boxList.append((boxCount,idList))
    setCageStyle(idList,"solid thick")
        
        
    
def on_grid_button_pressed(ev): 
    itm=ev.currentTarget
    idList=members_of_group(itm.id,True)
    for id in idList:
        cell=gridDict[id]
        cell.action("click")
        set_backGround(id, cell)
        document[id].text=""
        #document[id].style.backgroundColor=cell.status.background()
    if len(idList)>1:
        setCageStyle(idList,"solid thin")
    remove_box_for_id(itm.id)
    
def on_mouse_enter(ev): 
    #document["progress"].text=f'entering {ev.currentTarget.id} {gridDict[ev.currentTarget.id].status.name()}'
    global gridDict
    itm=ev.currentTarget
    for id in members_of_group(itm.id,True):
        cell=gridDict[id]
        cell.action("mousein")
        set_backGround(id, cell)
        
        #document[id].style.backgroundColor=cell.status.background()
    
def on_mouse_leave(ev): 
    itm=ev.currentTarget
    idList=members_of_group(itm.id,True)
    for id in idList:
        cell=gridDict[id]
        cell.action("mouseout")
        set_backGround(id, cell)
        #document[id].style.backgroundColor=cell.status.background()
    



def show_solution(solution):
    if solution:
        for k,v in solution.items():
            id=tuple2id(k)
            document[id].text=str(v)
#            document[id].style.backgroundColor='white';
    else:
        alert("can't find solution")



import ktest

def sample(ev):
    global zz,boxList
    document["button1"].textContent = "Solve"
    boxList=[]
    for (n,sList)  in ktest.case[15][1]:
        add_cage(n,list(map(tuple2id,sList)))
    return
    
    
def change(event):
    global zz,qq,boxList,generator,doubles
    zz=kl.KillerSudoku(boardSize)
    qq=None
    try:
        if True:
            for (n,idList) in boxList:
                print ( "(",n,",",list(map(id2tuple,idList)),"),")
            zz.load([ (n,list(map(id2tuple,idList)))  for (n,idList) in boxList])
            #zz.solve()
            generator=zz.solve2()
            doubles=None
        else:
            zz=ktest.solve()
    except Exception as e:
        alert(" ".join(map(str,e.args)) )
        return
    
    document["progress"].text=""

    for s in gridDict.keys():
        b=gridDict[s]
        itm=document[b.id]
        itm.text=""
    
    document["button1"].textContent = "thinking"
    
    timer.set_timeout(ongoing,0)



def report(num):
    #document["progress"].text=str(num -81 )
    document["progress"].style.width=str(int((581 - num) / 5  ))+"%"
    

def ongoing():
    global zz,bsave,generator,doubles

    try:
        t=next(generator)
        if t==0:
            raise Exception("Failed to find solution")
        report(t)
        if t!=boardSize ** 2 and t!=0:
            for k,v in zz.board.items():
                if len(v)==1:
                    id=tuple2id(k)
                    document[id].text=str(list(v)[0])
    
            timer.set_timeout(ongoing,0)
        else:
            show_solution(zz.get_solution())
            document["button1"].textContent = "done"

    except Exception as e:
        def yy(l):
            for s,v in l:
                i=0
                for vv in v: #reversed( [ x for x in v]):
                    yield (s,vv,i)
                    i+=1
                
            
        if not doubles:
            doubles=yy( (s,v) for (s,v) in zz.board.items() if len(v)==2 )
            document["button1"].textContent = "Heuristic"
            bsave=copy.deepcopy(zz.board)
            
        try:
            (s,v,i)=next(doubles)
            if i==1 and e.args==("Failed to find solution",):
                #skip this one
                (s,v,i)=next(doubles)
                
            zz.board=copy.deepcopy(bsave)
            #zz.turbo=False
            print("copied")

            print("Try setting",s,"from",zz.board[s],"to",v)
            zz.board[s]={v}
            zz.last_inner={}
            zz.last_outer={}
            generator=zz.solve2()
            timer.set_timeout(ongoing,0)
            return
            
        except StopIteration:
            document["button1"].textContent = "failed"
            alert("No Solution" )
            return    
    


