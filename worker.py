"""Web Worker script."""

# In web workers, "window" is replaced by "self".
from browser import bind, self
import copy
import kl
#print(self.getSubTotals)
print("loaded")

def report_singleton(k,v):
    self.send([0,k,list(v)[0]])
@bind(self, "message")
def message(evt):
    global flag
    """Handle a message sent by the main script.
    evt.data is the message body.
    """
    zz=kl.KillerSudoku(9,report_singleton=report_singleton)
    #zz.report_singleton=report_singleton
    zz.load(evt.data)
    t=kl.doit(zz)
    try:
        self.send('OK')
    except ValueError:
        self.send('BAD')