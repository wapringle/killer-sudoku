#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import kl
import pprint

"""
class KillerFrame(MyFrame):
    boxList=[]
    gridDict={}
    redo=False
    def __init__(self, *args, **kwds):
        MyFrame.__init__(self, *args, **kwds)
        # if required, insert more initialization code here and create data structures

        sz=3
        qz=range(sz)
        rx,cx=0,0
        button_no=28
        for rr in qz:
            for cc in qz:
                for r in qz:
                    for c in qz:
                        row=sz*rr + r + 1
                        col=sz*cc+c + 1
                        button=eval("self.button_%d" % (button_no))
                        self.gridDict[(row,col)]=button
                        self.Bind(wx.EVT_TOGGLEBUTTON, lambda event,button_id=(row,col) : self.on_grid_button_pressed(event,button_id), button)
                        button.Bind(wx.EVT_ENTER_WINDOW, lambda event,button_id=(row,col) : self.on_mouse_enter(event,button_id) )
                        button.Bind(wx.EVT_LEAVE_WINDOW, lambda event,button_id=(row,col) : self.on_mouse_leave(event,button_id) )
                        button_no+=1
            rx+=1

       
        num=1
        for bb in list(range(3,28)) + list(range(109,124)):
            button=eval("self.button_%d" % bb )
            button.SetLabelText(str(num))
            self.Bind(wx.EVT_BUTTON, lambda event,temp=str(num) : self.on_number_button_pressed(event,temp), button)
            num+=1
        self.boxList=[]
        
    def on_number_button_pressed(self,event,num):
        sList=sorted([k for k,v in self.gridDict.items() if v.GetValue() ])
        if sList==[]:
            return
        boxCount=int(num)
        for s in sList:
            b=self.gridDict[s]
            b.SetValue(False)
            b.SetBackgroundColour('#e30000')
            b.SetLabelText("")
        b0=self.gridDict[sList[0]]
        b0.SetFont(wx.Font(12, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        b0.SetLabelText(str(boxCount))
        print(boxCount,sList)
        self.boxList.append((boxCount,sList))
        if sum(map(len,[sList for boxCount,sList in self.boxList]))==81:
            try:
                kk=kl.KillerSudoku(9)
                kk.load(self.boxList)
                pprint.pprint(self.boxList)
                solution=kk.solve()
                if solution:
                    for k,v in solution.items():
                        b=self.gridDict[k]
                        b.SetFont(wx.Font(24, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
                        b.SetLabelText(str(v))
                        b.SetBackgroundColour(wx.NullColour)
                        
            except Exception as e:
                mess=" ".join(map(str,e.args))                
                a=MyDialog(self)
                m2=a.FindWindowByLabel('Message')
                m2.SetLabelText(mess)
                a.ShowModal() 
        event.Skip()
        
"""
boxList=[]
gridDict={}

def selectedGroup(self,button_id,remove=False):
    global boxList,gridDict
    for boxCount, sList in self.boxList:
        if button_id in sList:
            for s in sList:
                yield gridDict[s]
            if remove:
                boxList.remove((boxCount,sList))
            break
    

def on_grid_button_pressed(self, event,button_id):  # wxGlade: MyFrame.<event_handler>
    for b in selectedGroup(button_id,remove=True):
        b.SetValue(True)
        b.SetBackgroundColour(wx.NullColour)
        b.SetLabelText("")
    event.Skip()

def on_mouse_enter(ev): 
    f'entering {ev.currentTarget.id}'
    for b in selectedGroup(button_id):
        b.SetValue(True)

def on_mouse_leave(self, event, button_id): 
    for b in selectedGroup(button_id):
        b.SetValue(False)



