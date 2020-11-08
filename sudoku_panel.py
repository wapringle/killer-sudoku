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
from  browser import document, timer, bind
import kl
from browser.widgets.dialog import InfoDialog
#from brythonInterface import boardSize

boardSize=9

boxList=[]
gridDict={}

canMouse=True
def myAlert(txt):
    global canMouse
    canMouse=False
    
    document["help"].style["border-style"]="inset"
    d=InfoDialog("Alert!",txt,ok=True, default_css=False)
    @bind(d.ok_button, "click")
    def ok(ev):
        global canMouse
        document["help"].style["border-style"]="outset" 
        canMouse=True


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
            setattr(document["td"+id].style,border,style)
    for id in idList:
        (r,c)=id2tuple(id)
        if c>1:
            makeEdge((r,c-1) , "borderLeft")
        if c<9:
            makeEdge((r,c+1) , "borderRight")
        if r>1:
            makeEdge((r-1,c) , "borderTop")
        if r<9:
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
    global canMouse
    if not canMouse: return
    
    idList=get_clicked_cells()
    if idList==[]:
        return
    
    itm=ev.currentTarget
    boxCount=int(itm.text)
    add_cage(boxCount,idList)
    document[itm.id].style.borderStyle="inset"
    
    
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
    setCageStyle(idList,"solid")
        
        
    
def on_grid_button_pressed(ev): 
    global canMouse
    if not canMouse: return
    itm=ev.currentTarget
    idList=members_of_group(itm.id,True)
    for id in idList:
        cell=gridDict[id]
        cell.action("click")
        set_backGround(id, cell)
        document[id].text=""
    if len(idList)>1:
        setCageStyle(idList,"solid thin")
    remove_box_for_id(itm.id)
    
def on_mouse_enter(ev): 
    global canMouse
    if not canMouse: return
    #document["progress"].text=f'entering {ev.currentTarget.id} {gridDict[ev.currentTarget.id].status.name()}'
    global gridDict
    itm=ev.currentTarget
    for id in members_of_group(itm.id,True):
        cell=gridDict[id]
        cell.action("mousein")
        set_backGround(id, cell)
        
        #document[id].style.backgroundColor=cell.status.background()
    
def on_mouse_leave(ev): 
    global canMouse
    if not canMouse: return
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
        myAlert("can't find solution")



import ktest
testcase=13
def sample(ev):
    global zz,boxList,testcase
    document["button1"].textContent = "Solve"
    boxList=[]
    for (n,sList)  in ktest.case[testcase][1]:
        add_cage(n,list(map(tuple2id,sList)))
    return
    

def change(event):
    global canMouse
    canMouse = False
    
    global zz,qq,boxList,generator,doubles
    zz=kl.KillerSudoku(boardSize)
    try:
        for (n,idList) in boxList:
            print ( "(",n,",",list(map(id2tuple,idList)),"),")
        zz.load([ (n,list(map(id2tuple,idList)))  for (n,idList) in boxList])
        generator=kl.doit(zz)
    except Exception as e:
        myAlert(" ".join(map(str,e.args)) )
        canMouse=True
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
    global zz,bsave,generator

    try:
        t=next(generator)
        if t==0:
            raise Exception("Failed to find solution")
        report(t)
        if t!=boardSize ** 2:
            for k,v in zz.board.items():
                if len(v)==1:
                    id=tuple2id(k)
                    document[id].text=str(list(v)[0])
                else:
                    id=tuple2id(k)
                    document[id].text=""
    
            timer.set_timeout(ongoing,0)
        else:
            print("done")
            show_solution(zz.get_solution())
            document["button1"].textContent = "done"

    except StopIteration:
        print("done")
        show_solution(zz.get_solution())
        document["button1"].textContent = "done"
        global canMouse
        canMouse = True
        
        pass
    except Exception as e:
        document["button1"].textContent = "Solve"
        global canMouse
        canMouse = True
        myAlert(e.message)

        
        

"""
from browser import bind, worker, window

# Create a web worker, identified by a script id in this page.
myWorker = worker.Worker("myworker")

def change(evt):
    #Called when the value in one of the input fields changes.
    # Send a message (here a list of values) to the worker
    myWorker.send([ (n,list(map(id2tuple,idList)))  for (n,idList) in boxList])
    
    document["progress"].text=""

    for s in gridDict.keys():
        b=gridDict[s]
        itm=document[b.id]
        itm.text=""
    
    document["button1"].textContent = "thinking"
    

@bind(myWorker, "message")
def onmessage(e):
    #Handles the messages sent by the worker.
    print(e.data)
    l=e.data
    if l[0]==0:
        document[tuple2id(tuple(l[1]))].text=str(l[2])
        
        """        
