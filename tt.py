from brythonInterface import make_grid
from sudoku_panel import sample, ongoing, change
from browser import timer 


def set_timeout(fun,i):
    fun()
    
timer.set_timeout=set_timeout

grid={}
make_grid(grid)
ev=None

sample(ev)
change(ev)
i=1
    