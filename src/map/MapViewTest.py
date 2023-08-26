
from MapView import *
import threading,time

def isRunning():
  for i in range(10):
    time.sleep(1)
    logger.info("is running %d.",i)

mv = MapView(100,100)

mv.SetPathStartEnd(Point(10,10),Point(90,80))

t2 = threading.Thread(target= isRunning)
t2.start()


mv.ChangePath([Point(10,10),Point(11,11),Point(11,12),Point(11,13),Point(11,14),Point(11,15)])

mv.DrawFrame()

t2.join()
