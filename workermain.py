"""Main script."""

from browser import bind, document, worker  

result = document.select_one('.result')
inputs = document.select("input")

# Create a web worker, identified by a script id in this page.
myWorker = worker.Worker("myworker")

@bind(inputs, "change")
def change(evt):
    """Called when the value in one of the input fields changes."""
    # Send a message (here a list of values) to the worker
    myWorker.send([x.value for x in inputs])

@bind(myWorker, "message")
def onmessage(e):
    """Handles the messages sent by the worker."""
    result.text = e.data