import pygame
from pygame.locals import *
from .GameState import GameState

class ResultState(metaclass=GameState):
#class ResultState(GameState):
#    def __init__(self, stateSwitcher): super().__init__(stateSwitcher)
    def Initialize(self):
        print('ゴール演出開始。')
    def Finalize(self):
        print('ゴール演出終了。たとえば効果音などが鳴っている最中なら終わらせる。')
    def Event(self, event, command):
        pass
    def Draw(self, screen): screen.fill((0,0,255))
    def SwitchScene(self, event, switcher):
        if event.type == KEYDOWN:
            if event.key == K_RETURN or event.key == K_SPACE or event.key == K_z: switcher.Next()

