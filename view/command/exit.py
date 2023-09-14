from view.command.command import Command
from view.view import View


class Exit(Command):
    def __init__(self, console : View) -> None:
        super().__init__(console, 'Выйти.')
    
    def get_description (self) -> str:
        return super().get_description()
    
    def execute(self) -> None:
        super().get_console().exit()