
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import logging

logging.basicConfig(level=logging.DEBUG )

class Color():
  red='r'
  black='k'
  white='w'
  yellow='y'
  green='g'
  blue='b'
  cyan='c'
  magenta='m'
  
class Shape():
  point='.'
  circle='o'
  squre='s'
  x='x'


class Element():
  def __init__(self,shape:Shape =Shape.point,color:Color = Color.red) -> None:
    self.shape = shape
    self.color = color
    self.x=[]
    self.y=[]
    return
  
  def AddPoints(self,x=[],y=[]):
    self.x.extend(x)
    self.y.extend(y)
    logging.debug("points: %s %s",self.x,self.y)

  def GetFormat(self):
    return str(self.shape + self.color)
  
  
  
  
class Frame():
  def __init__(self ) -> None:
    self.elems =[]
    return
  
  def AddElem(self,elem:Element):
    self.elems.append(elem)
    return
     

class Animation():
  def __init__(self,title:str,x_min:float,x_max:float,y_min:float,y_max:float) -> None:
    self.title = title
    self.x_min = x_min
    self.x_max = x_max
    self.y_min = y_min
    self.y_max = y_max 
    self.interval = 100
    self.fig, self.ax, = plt.subplots()

    self.ax.set_title(self.title)
    self.ax.set_xlim(x_min ,x_max )
    self.ax.set_ylim(y_min ,y_max )
    # self.ax.grid()

  def SetFrame(self,data:Frame):
    self.frame = data

  def Animate(self,i):
    try:
      for i in self.frame.elems:
        logging.debug("points: ",str(i.x), str(i.y))
        self.ax.plot(i.x,i.y,i.GetFormat())

      return self.ax,
    except Exception as e:
      logging.error(e)
      logging.warn('cant get frame')
      return self.ax,
    
  
  def Run(self):
    self.anim = FuncAnimation(self.fig, self.Animate, interval=100, blit=True)
    plt.show()