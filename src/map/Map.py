import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))  # 将父级目录加入执行目录列表

from animation.Animation import *

def RectanglePoints(start=[0,0],end=[1,1]):
  x,y=[],[]
  for i in range(start[0],end[0]):
    for j in range(start[1],end[1]):
      x.append(i)
      y.append(j)
  
  return x,y

class Map():
    def __init__(self,row,col) -> None:
      
      self.row = row
      self.col = col
      self.frame = Frame()
      
      self.wall=Element(Shape.squre,Color.black)
      self.obstacle=Element(Shape.circle,Color.black)
      self.start = Element(Shape.squre,Color.blue)
      self.end = Element(Shape.x,Color.blue)
      
      self.wall.AddPoints(RectanglePoints((0,0),(row,0)))
      self.wall.AddPoints(RectanglePoints((row,0),(row,col)))
      self.wall.AddPoints(RectanglePoints((0,0),(0,col)))
      self.wall.AddPoints(RectanglePoints((0,col),(row,col)))
      
      self.frame.AddElem(self.wall)
      self.frame.AddElem(self.obstacle)
      self.frame.AddElem(self.start)
      self.frame.AddElem(self.end)
      
      return
    
    def SetObstacle(self,start=[0,0],end=[1,1]):
      x,y = RectanglePoints(start,end)
      self.obstacle.AddPoints(x,y)
      
    def SetPathStartEnd(self,start=[0,0],end=[1,1]):
      self.start.AddPoints(start)
      self.end.AddPoints(end)
