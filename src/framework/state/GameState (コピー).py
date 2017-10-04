from abc import ABCMeta, abstractmethod
#from .StateSwitcher import StateSwitcher
#from framework.state.StateSwitcher
#from framework.state.StateSwitcher import StateSwitcher
#from .SelectState import SelectState
#from framework.state.SelectState import SelectState
#import framework.state.StateSwitcher
#from framework.command.GameCommand import GameCommand
class GameState(type, metaclass=ABCMeta):
    __stateSwitcher = None
    __command = None
    def __new__(cls, name, bases, attrs):
        attrs['_'+name+'__stateSwitcher'] = cls.__NewStateSwitcher()
        attrs['_'+name+'__command'] = cls.__NewCommand()
        return type.__new__(cls, name, bases, attrs)
    @classmethod
    def __NewStateSwitcher(cls):
        print(SelectState())
        if not cls.__stateSwitcher: cls.__stateSwitcher = StateSwitcher()
        return cls.__stateSwitcher
        pass
    @classmethod
    def __NewCommand(cls):
        if not cls.__command: cls.__command = GameCommand()
        return cls.__command

#    @property
#    def Switcher(self): return self.__stateSwitcher
#    @property
#    def Command(self): return self.__command

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

