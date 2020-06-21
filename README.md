# killer-sudoku

Web app to solve Killer Sudoku puzzles, see https://en.wikipedia.org/wiki/Killer_sudoku

Click on squares to form a cage, then click on the sum of numbers in the cage. When the grid is complete, presss "Solve" and the grid should be gradually filled in. Alternatively click the button "Sample" to load a sample puzzle and "Solve" to solve it.

The app is written in brython https://brython.info/index.html (A Python 3 implementation for client-side web programming) adapted from a command line version of same.

Files
  - index.html - Contains stylesheet and lnk to brythoninterface.py
  - brythoninterface.py - script to build the webpage
  - sudoku_panel.py - script that reacts to the mousclicks etc and displays the result
  - kl.py - pure python script that solves the puzzle, can also be run from the command line, see below. Makes extensive use of the python set operator
  - jtest.js - javascript rewrite of critical python function as a speedup
  
Extras
  - ktest.py - contains a number of sample puzzles that can be run from the command line
  
  
  


