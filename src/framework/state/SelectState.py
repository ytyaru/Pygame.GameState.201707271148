import pygame
from pygame.locals import *
from .GameState import GameState

class SelectState(metaclass=GameState):
#class SelectState(GameState):
#    def __init__(self, stateSwitcher): super().__init__(stateSwitcher)
    def __init__(self):
        print(dir(self))
    def Initialize(self):
        print('あみだくじ新規作成。')
    def Finalize(self): pass
    def Event(self, event, command):
        if event.type == KEYDOWN:
            if event.key == K_LEFT: pass
            elif event.key == K_RIGHT: pass
            elif event.key == K_RETURN or event.key == K_SPACE or event.key == K_z:
                print('左右キーで選択indexを変更し、SPACEキーで決定する。')
    def Draw(self, screen): screen.fill((255,0,0))
    def SwitchScene(self, event, switcher):
        if event.type == KEYDOWN:
#            if event.key == K_RETURN or event.key == K_SPACE or event.key == K_z: self.Switcher.Next()
#            if event.key == K_RETURN or event.key == K_SPACE or event.key == K_z: self.__stateSwitcher.Next()
            if event.key == K_RETURN or event.key == K_SPACE or event.key == K_z: switcher.Next()

