# killer-sudoku

Web app to solve Killer Sudoku puzzles, see https://en.wikipedia.org/wiki/Killer_sudoku

Click on squares to form a cage, then click on the sum of numbers in the cage. When the grid is complete, press "Solve" and the grid should be gradually filled in. Alternatively click the button "Sample" to load a sample puzzle and "Solve" to solve it.

The app is written in brython https://brython.info/index.html (A Python 3 implementation for client-side web programming) adapted from a command line version of same.

Files
  - index.html - Contains stylesheet and link to brythoninterface.py
  - brythoninterface.py - script to build the webpage
  - sudoku_panel.py - script that reacts to the mouseclicks and displays the result
  - kl.py - pure python script that solves the puzzle, can also be run from the command line, see below. 
  - jtest.js - javascript rewrite of critical python function as a speedup
  
Extras
  - ktest.py - contains a number of sample puzzles that can be run from the command line
  
Notes
  - kl.py makes extensive use of the python 'set' type
  - kl.py makes a number of passes to solve the puzzle. After each pass it passes control to the webpage to update the numbers found. Otherwise the screen sits blank for 20 seconds or so until the puzzle is completely solved.
  
  


