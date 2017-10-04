import pygame, sys
from pygame.locals import *
from abc import ABCMeta, abstractmethod
import ui.Screen
import framework.state.StateSwitcher
import framework.command.GameCommand

class Main:
    def __init__(self, title=None):
        self.__title = title
        self.__screen = ui.Screen.Screen()
        self.__stateSwitcher = framework.state.StateSwitcher.StateSwitcher()
        self.__command = framework.command.GameCommand.GameCommand()
    def Run(self):
        pygame.init()
        if self.__title: pygame.display.set_caption(self.__title)
        clock = pygame.time.Clock()
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: pygame.quit(); sys.exit();
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE: pygame.quit(); sys.exit();
                self.__stateSwitcher.State.SwitchScene(event, self.__stateSwitcher)
                self.__stateSwitcher.State.Event(event, self.__command)
            self.__stateSwitcher.State.Draw(self.__screen.Screen)
            pygame.display.flip()
            clock.tick(60) # 60 FPS


if __name__ == '__main__':
    main = Main(title="ゲーム状態")
    main.Run()
