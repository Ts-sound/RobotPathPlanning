import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))  # 将父级目录加入执行目录列表

from animation.Animation import *
from Map import Map


class MapView(Map):
    def __init__(self,row,col) -> None:
        super().__init__(row,col)
        self.edge = 10
        self.anime = Animation('',-self.edge,self.edge+col,-self.edge,self.edge+row)
        self.frame = Frame()

        


    def DrawFrame(self):
        elem= Element()
        elem.AddPoints([1,2,3],[1,2,3])
        self.frame.AddElem(elem)

        self.frame.AddElem(self.wall)
        self.frame.AddElem(self.obstacle)
        self.frame.AddElem(self.start)
        self.frame.AddElem(self.end)

        self.anime.SetFrame(self.frame)
        self.anime.Run()

        return
