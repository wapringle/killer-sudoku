from browser import document, html, alert
from browser.html import *

from sudoku_panel import on_mouse_enter, on_mouse_leave, on_grid_button_pressed, on_number_button_pressed, sample, change, initCell


def make_numbers():
    t = html.TABLE()
    tb = html.TBODY()
    t <= tb
    i = 1
    val = ""
    for row in range(5):
        line = html.TR()
        tb <= line
        for column in range(10):
            b = html.BUTTON(str(i), id="x%s" % i, Class="nobutton")
            cell = html.TD(b)
            b.bind("click", on_number_button_pressed)
            line <= cell
            i += 1
    return t


grid_step = 3

# gridStep=2 ( smaller size for devel )
board_size = grid_step ** 2


def make_grid(grid):
    # returns an HTML table with 9 rows and 9 columns
    global current_cell, gridDict

    t = html.TABLE()
    for i in range(grid_step):
        cg = html.COLGROUP()
        for j in range(grid_step):
            cg <= html.COL()
        t <= cg
    srow = -1
    # for i,val in enumerate(grid):
    #    row, column = divmod(i, boardSize)
    val = " "
    i = 0
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
            cell = html.TD(val, id=id, Class="unused")
            cell.bind("mouseenter", on_mouse_enter)
            cell.bind("mouseleave", on_mouse_leave)
            cell.bind("click", on_grid_button_pressed)
            cell.style.contentEditable = True
            if column % grid_step == 0:
                cell.style.borderLeftWidth = "1px"
            if column == board_size - 1:
                cell.style.borderRightWidth = "1px"
            line <= cell
            i += 1

    current_cell = None
    print(t)
    return t


def xxx():
    puzzle = html.DIV(style={"margin": "auto", "width": "100%" if grid_step == 3 else "50%"})
    grids = {}
    puzzle <= make_grid(grids)
    return puzzle

def help(ev) :
    txt="""    Click on cages to build cells, then click on number button to select 
    total for cage. When complete, press 'Solve'.
    Press 'Sample' for a sample puzzle. 
    For background see https://en.wikipedia.org/wiki/Killer_sudoku 
    """
    alert(txt)


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
    document["help"].bind("click",help)
