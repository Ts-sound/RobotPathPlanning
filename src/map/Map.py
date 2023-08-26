import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))  # 将父级目录加入执行目录列表

from animation.Animation import *

def RectanglePoints(start=[0,0],end=[1,1]):
  points=[]
  for i in range(start[0],end[0]+1):
    for j in range(start[1],end[1]+1):
      points.append(Point(i,j))
  
  logger.debug('x,y %s',points)
  return points

class Map():
    def __init__(self,row,col) -> None:
      
      self.row = row
      self.col = col
      
      self.wall=Element(Shape.squre,Color.black)
      self.obstacle=Element(Shape.circle,Color.black)
      self.start = Element(Shape.squre,Color.blue)
      self.end = Element(Shape.x,Color.red)
      self.path = Element(Shape.circle,Color.yellow)
      
      self.wall.AddPoints(RectanglePoints((0,0),(row,0)))
      self.wall.AddPoints(RectanglePoints((row,0),(row,col)))
      self.wall.AddPoints(RectanglePoints((0,0),(0,col)))
      self.wall.AddPoints(RectanglePoints((0,col),(row,col)))
      
      return
    
    def SetObstacle(self,p1=[0,0],p2=[1,1]):
      points = RectanglePoints(p1,p2)
      self.obstacle.AddPoints(points)
      
    def SetPathStartEnd(self,start=Point(0,0),end=Point(1,1)):
      self.start.AddPoints([start])
      self.end.AddPoints([end])
      
    def ChangePath(self,points:list[Point]):
      self.path.AddPoints(points)

    
