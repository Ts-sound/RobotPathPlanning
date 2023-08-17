from Animation import *
import time

def test_elem():
    elem= Element()
    elem.AddPoints([1,2,3],[1,2,3])

    
    return

def test_anime():
    chart =  Animation("test",0,80,0,80)

    elem= Element()
    elem.AddPoints([1,2,3],[1,2,3])

    frame =  Frame()
    frame.AddElem(elem)

    elem2= Element(Shape.squre,Color.black)
    elem2.AddPoints([4,4,5],[4,5,5])
    frame.AddElem(elem2)

    chart.SetFrame(frame)

    chart.Run()

    print("end ")
    return


test_elem()