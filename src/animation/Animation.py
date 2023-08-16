import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import queue

class Element():
  def __init__(self,shape = '',color = '') -> None:
    return
  
class Frame():
  def __init__(self,shape = '',color = '') -> None:
    return
     

class Animation():
  def __init__(self,title:str,x_min:float,x_max:float,y_min:float,y_max:float) -> None:
    self.title = title
    self.x_min = x_min
    self.x_max = x_max
    self.y_min = y_min
    self.y_max = y_max 
    self.interval = 100
    self.fig, self.ax = plt.subplots()
    self.__queue = queue.Queue()

    self.line, = self.ax.plot([self.x_min, self.x_max], \
       [self.y_min, self.y_max])
    self.ax.set_title(self.title)
    # self.ax.grid()

  def AddFrame(self,data:Element):
    self.__queue.put(data)

  def Animate(self,i):
    # print(i,self.__queue.qsize())
    if self.__queue.empty():
      return self.line,

    elem = self.__queue.get()
    print(elem.x,elem.y)
    self.line.set_xdata(elem.x)
    self.line.set_ydata(elem.y)

    return self.line,
  
  def Run(self):
    print("queue size = " ,self.__queue.qsize())
    anim = FuncAnimation(self.fig, self.Animate, interval=100, blit=True)
    plt.show()