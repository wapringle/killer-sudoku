from  browser import document, timer, alert

import kl,ktest
#from brythonInterface import boardSize

boardSize=9

boxList=[]
gridDict={}

def tuple2id(t): return "i%d%d" % t

def id2tuple(id): return (int(id[1]),int(id[2]))

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
    def background(self):
        return 'ivory'
    def mousein(self):
        return highlight()
    
class highlight(State):
    def background(self):
        return '#eefbff'
    def click(self):
        return clicked()
    def mouseout(self):
        return unused()
    
class clicked(State):
    def is_clicked(self): return True
    def background(self):
        return '#f33fba4d'
    def grouped(self):
        return caged()
    def click(self):
        return highlight()
    def mousein(self):
        return clicked()
    def mouseout(self):
        return clicked()
    
class caged(State):
    def background(self):
        return 'beige'
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
    def background(self):
        return 'bisque'
    def mouseout(self):
        return caged()
    def click(self):
        return clicked()
    
    
    
    
    
class GridSquare():
    def __init__(self,id):
        self.id=id
        self.status=unused()
        
    def on_clicked(self):
        self.status=self.status.click()
        pass
        
    def on_grouped(self):
        self.status=self.status.grouped()
        pass
        
    def on_mouse_enter(self):
        self.status=self.status.mousein()
        pass
    
    def on_mouse_leave(self):
        self.status=self.status.mouseout()
        pass

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
    tList= [ id2tuple(id) for id in idList]
    for (r,c) in tList:
        t=(r,c)
        if (r,c-1) not in tList:
            document[tuple2id(t)].style.borderLeft=style
            pass
        if (r,c+1) not in tList:
            document[tuple2id(t)].style.borderRight=style
            pass
        if (r-1,c) not in tList:
            document[tuple2id(t)].style.borderTop=style
            pass
        if (r+1,c) not in tList:
            document[tuple2id(t)].style.borderBottom=style
            pass

def get_clicked_cells():
    return sorted([k for k,v in gridDict.items() if v.status.is_clicked() ])

def some_cells_clicked():
    return False #len(get_clicked_cells())>0

def set_backGround(id,cell):
    #print(f'cell {id} class from {document[id].Class} to {cell.status.name()}')
    #document[id].Class=cell.status.name()
    
    document[id].style.backgroundColor=cell.status.background()
    
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
        b.on_grouped()
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
        cell.on_clicked()
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
        cell.on_mouse_enter()
        set_backGround(id, cell)
        
        #document[id].style.backgroundColor=cell.status.background()
    
def on_mouse_leave(ev): 
    itm=ev.currentTarget
    idList=members_of_group(itm.id,True)
    for id in idList:
        cell=gridDict[id]
        cell.on_mouse_leave()
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

def change(event):
    global zz,boxList
    document["progress"].text=""
    if len(boxList)==0:
        boxList=[]
        for (n,sList)  in ktest.case[10][1]:
            add_cage(n,list(map(tuple2id,sList)))
        return
    for s in gridDict.keys():
        b=gridDict[s]
        itm=document[b.id]
        itm.text=""
    
    document["button1"].textContent = "thinking"
    zz=kl.KillerSudoku(boardSize)
    try:
        if True:
            for (n,idList) in boxList:
                print ( "(",n,",",list(map(id2tuple,idList)),"),")
            zz.load([ (n,list(map(id2tuple,idList)))  for (n,idList) in boxList])
            #zz.solve()
        else:
            zz=ktest.solve()
    except Exception as e:
        alert(" ".join(map(str,e.args)) )
        return
    
    
    timer.set_timeout(ongoing,0)



def report(num):
    document["progress"].text=str(num)

def ongoing():
    global zz
    try:
        t=zz.iteration()
    except Exception as e:
        document["button1"].textContent = "failed"
        alert("No Solution" )
        return    
    report(t)
    if t!=boardSize ** 2 and t!=0:
        for k,v in zz.board.items():
            if len(v)==1:
                id=tuple2id(k)
                document[id].text=str(list(v)[0])

        timer.set_timeout(ongoing,0)
    else:
        if t==0:
            document["button1"].textContent = "failed"
            alert("can't find solution")
        else:
            show_solution(zz.get_solution())
        document["button1"].textContent = "done"
    


