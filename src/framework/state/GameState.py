from abc import ABCMeta, abstractmethod
#from .StateSwitcher import StateSwitcher
#from framework.state.StateSwitcher
#from framework.state.StateSwitcher import StateSwitcher
#from .SelectState import SelectState
#from framework.state.SelectState import SelectState
#import framework.state.StateSwitcher
#from framework.command.GameCommand import GameCommand
class GameState(type, metaclass=ABCMeta):
    @abstractmethod
    def Initialize(self): raise NotImplementedError()
    @abstractmethod
    def Finalize(self): raise NotImplementedError()
#    @abstractmethod
#    def Event(self, event): raise NotImplementedError()
#    @abstractmethod
#    def Draw(self, screen): raise NotImplementedError()
    @abstractmethod
    def Event(self, event, command): raise NotImplementedError()
    @abstractmethod
    def Draw(self, screen): raise NotImplementedError()
    @abstractmethod
    def SwitchScene(self, event, switcher): raise NotImplementedError()

