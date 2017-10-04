from game.Ghostleg import Ghostleg
from game.LinesAnimation import LinesAnimation
from game.PointList import PointList
from ui.Screen import Screen
from ui.CalcSize import CalcSize
"""
class CommonClasses:
    def __init__(self):
        self.__ghostleg = Ghostleg()
        self.__screen = Screen()
        self.__calcSize = CalcSize(self.__ghostleg, self.__screen)
        self.__pointlist = Pointlist(ghostleg, calcSize, screen)
        self.__linesAnimation = None
    @property
    def Screeen(self): return self.__screen
"""
class GameCommand:
    def __init__(self):
#        self.__common = CommonClasses()
        self.__ghostleg = Ghostleg()
        self.__ghostleg.Create()
        print('self.__ghostleg', self.__ghostleg)
        self.__screen = Screen()
        self.__calcSize = CalcSize(self.__ghostleg, self.__screen)
        self.__pointlist = PointList(self.__ghostleg, self.__calcSize, self.__screen)
        self.__linesAnimation = None
    def NewGhostleg(self): self.__ghostleg.Create()
    def StartAnimation(self, selectedIndex):
        self.__pointlist.Create(selectedIndex)
        self.__linesAnimation = LinesAnimation(self.__pointlist.Pointlist)
    def Animation(self, screen): self.__linesAnimation.draw(screen)
    def EndAnimation(self):
        print('EndAnimation()')
    def StartGoalPerformance(self):
        print('StartGoalPerformance()')
    def EndGoalPerformance(self):
        print('EndGoalPerformance()')

