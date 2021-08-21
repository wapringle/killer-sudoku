import pytest
import re


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
        
    