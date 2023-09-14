from abc import abstractmethod

from view.view import View


class Command:

    def __init__(self, console : View, description : str) -> None:
        self.__console = console
        self.__description = description

    def get_console(self) -> View:
        return self.__console

    def get_description (self) -> str:
        return self.__description
    
    @abstractmethod
    def execute(self) -> None:
        pass
