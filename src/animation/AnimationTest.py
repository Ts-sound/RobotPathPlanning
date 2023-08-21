from Animation import *
import time

def test_elem():
    elem= Element()
    p1=Point(1,1)
    p2=Point(2,2)
    elem.AddPoints([p1,p2])


    return

def test_anime():
    chart =  Animation("test",0,80,0,80)

    elem= Element()
    p1=Point(1,1)
    p2=Point(2,2)
    elem.AddPoints([p1,p2])
    elem.AddPoints([Point(7,7),Point(8,8)])

    frame =  Frame()
    frame.AddElem(elem)

    elem2= Element(Shape.squre,Color.black)
    elem2.AddPoints([Point(4,5),Point(5,5)])
    frame.AddElem(elem2)

    chart.SetFrame(frame)

    chart.Run()

    print("end ")
    return


# test_elem()
test_anime()