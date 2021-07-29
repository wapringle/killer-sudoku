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

from browser import document, html, alert,bind
from browser.html import *
from browser.widgets.dialog import InfoDialog

from sudoku_panel import on_mouse_enter, on_mouse_leave, on_grid_button_pressed, on_number_button_pressed, sample, change, initCell, canMouse


def make_numbers():
    t = html.TABLE()
    tb = html.TBODY()
    t <= tb
    i = 0
    val = ""
    for row in range(5):
        line = html.TR()
        tb <= line
        for column in range(10):
            if i>0:
                b = html.BUTTON(str(i), id="x%s" % i, Class="nobutton")
                b.bind("click", on_number_button_pressed)
            else:
                b = html.SPAN("")
            cell = html.TD(b)
            line <= cell
            i += 1
    return t


grid_step = 3

# gridStep=2 ( smaller size for devel )
board_size = grid_step ** 2


def make_grid(grid):
    # returns an HTML table with 9 rows and 9 columns
    global current_cell, gridDict

    t = html.TABLE(Class="grid")
    for i in range(grid_step):
        cg = html.COLGROUP()
        for j in range(grid_step):
            cg <= html.COL()
        t <= cg
    srow = -1
    # for i,val in enumerate(grid):
    #    row, column = divmod(i, boardSize)
    val = " "
    for row in range(board_size):
        for column in range(board_size):
            if row > srow:
                if row % grid_step == 0:
                    tb = html.TBODY()
                    t <= tb
                line = html.TR()
                tb <= line
                srow = row

            id = initCell(row + 1, column + 1)
            cell = html.DIV(val, id=id, Class="unused")
            cell.bind("mouseenter", on_mouse_enter)
            cell.bind("mouseleave", on_mouse_leave)
            cell.bind("click", on_grid_button_pressed)
            cell.style.contentEditable = True
            
            td = html.TD(id="td"+id)
            td <= cell
            if column % grid_step == 0:
                td.style.borderLeftWidth = "1px"
            if column == board_size - 1:
                td.style.borderRightWidth = "1px"
            line <= td

    current_cell = None
    print(t)
    return t


def xxx():
    puzzle = html.DIV(style={"margin": "auto", "width": "100%" if grid_step == 3 else "50%"})
    grids = {}
    puzzle <= make_grid(grids)
    return puzzle



def init():
    table = TABLE(Class='outer')

    table <= TR(TD(make_numbers(), colspan=3, Class="outer"))
#    table <= TR(TD(HR(style={'width': '80%', 'height': '10px', 'background-color': 'black'}),colspan=2,Class="outer"))
    table <= TR(TD(
          SPAN("KILLER SODUKO")
        + SPAN("?", id="help",style={"background-color": "tomato", "border-style": "outset","margin-left": "50px", "cursor": "help"})
        , colspan=3, Class="outer")) 
    table <= TR(TD(xxx(), colspan=3, Class="outer"))
    table <= TR(
        TD(
            BUTTON("Sample", id="button0", Class="nobutton"),
            Class="outer") +
        TD(
            BUTTON("Solve", id="button1", Class="nobutton"),
            Class="outer") +
        TD(

            DIV(
                DIV(id="progress",
                    style={"background-color": "#f1f1f1", "height": "10px", "width": "1%"},
                    ),
                Class="progress"
            ),
            Class="outer"
        )
    )

    document <= DIV(table, Class='border')
    progress = document["progress"]
    document["button1"].bind("click", change)
    document["button0"].bind("click", sample)

    @bind(document["help"],"click")
    def help(ev) :
        global canMouse
        if not canMouse: return
        canMouse=False
        
        txt="""Click on cells to build cages, then click on number button to select 
        total for cage.<p>When complete, press 'Solve'.
        <p>
        Press 'Sample' for a sample puzzle. 
        <p>
        For background see <a href='https://en.wikipedia.org/wiki/Killer_sudoku'>https://en.wikipedia.org/wiki/Killer_sudoku</a>
        """
        document["help"].style["border-style"]="inset"
        d=InfoDialog("Help",txt,ok=True, default_css=False)
        @bind(d.ok_button, "click")
        def ok(ev):
            global canMouse
            canMouse=True
            document["help"].style["border-style"]="outset"
        
        

"""
<div style="color: black;font-size: medium;text-align: center;border-color: black;border-right-color: black;width: 100%;/* border-right:  thick solid; */border-left: thick solid;height: 100%;">11</div>
"""