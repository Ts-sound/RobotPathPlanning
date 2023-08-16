from Map import *

m = Map(0,100)
frame = m.frame

elem= Element()
elem.AddPoints([1,2,3],[1,2,3])
frame.AddElem(elem)

chart =  Animation("test",0,120,0,120)

chart.SetFrame(frame)
chart.Run()

print("end ")