from Map import *

def test_map():
    m = Map(0,100)
    frame = Frame()

    elem= Element()
    p1=Point(1,1)
    p2=Point(2,2)
    elem.AddPoints([p1,p2])

    frame.AddElem(elem)
    frame.AddElem(m.wall)

    chart =  Animation("test",0,120,0,120)

    chart.SetFrame(frame)
    chart.Run()

    print("end ")

def test_rectangle():
    RectanglePoints([0,0],[0,100])
    RectanglePoints([0,0],[100,0])


test_rectangle()