import pytest
import re

"""

import kl
from ktest import case

assert_flag=1

@pytest.fixture
def load():
    t=case[18]
    zz=kl.KillerSudoku(t[0])
    zz.load(t[1])
    return zz

def test_killer_load_error(capsys):
    t=case[1]
    # introduce error
    zz=kl.KillerSudoku(t[0])
    with  pytest.raises(kl.Error, match=re.escape('Duplicate 1 {(1, 1)}')) as exc_info:
        zz.load(t[1]+[(1,(1,1))])
    
    assert assert_flag
    
def test_fixture(load):
    assert load.grid_size == 3
    assert assert_flag

"""
from browser import html
from brythonInterface import make_grid
from sudoku_panel import on_mouse_enter, on_mouse_leave, on_grid_button_pressed, on_number_button_pressed
from sudoku_panel import  boxList


@pytest.fixture 
def load_grid():
    grid={}
    make_grid(grid)
    
def test_grid(load_grid):
    
    i24=html._EV('i24')
    i25=html._EV('i25')
    
    evn=html._EV("3")
    evn.currentTarget.text="3"
    
    on_mouse_enter(i25)         
    on_grid_button_pressed(i25)
    on_mouse_leave(i25)
    on_mouse_enter(i24)
    on_grid_button_pressed(i24)
    on_mouse_leave(i24)
    on_mouse_enter(i25)
    assert boxList == [ ]

def test_grid2(load_grid):
    ev=html._EV("i11")
    ev2=html._EV("i12")
    evn2=html._EV("3")
    evn2.currentTarget.text="3"


    # mousover square
    on_mouse_enter(ev)
    # click on square
    on_grid_button_pressed(ev)
    on_mouse_leave(ev)
    on_mouse_enter(ev2)
    on_grid_button_pressed(ev2)
    
    
   # then alocate number to group
    on_number_button_pressed(evn2)
    assert boxList == [ (3, ['i11','i12'])]
    i=1

    
    
"""
def test_solve(capsys):
    from brythonInterface import make_grid
    from sudoku_panel import sample, ongoing, change,testcase
    from browser import timer 
    
    
    def set_timeout(fun,i):
        fun()
        
    timer.set_timeout=set_timeout
    
    grid={}
    make_grid(grid)
    ev=None
    
    for testcase in [13,14,15,17,18]:
        sample(ev)
        change(ev)
        captured = capsys.readouterr()
        
        assert captured.out.endswith("done\n")
        assert assert_flag
"""
        
        
#test_grid()