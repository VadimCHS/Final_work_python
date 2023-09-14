from abc import abstractmethod

class Menu:
    
    @abstractmethod
    def menu(self) -> str:
        pass

    @abstractmethod
    def get_size(self) -> int:
        pass

    @abstractmethod
    def execute(self, choice:int) -> None:
        pass