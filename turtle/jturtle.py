import ipyturtle3 as t3

def Turtle(width = 500, height = 500):
    myCanvas=t3.Canvas(width, height)
    display(myCanvas)
    myTS = t3.TurtleScreen(myCanvas)
    myTS.clear()
    return t3.Turtle(myTS)
