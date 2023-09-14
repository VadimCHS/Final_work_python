from view.view import View
from view.command.command import Command


class SearchNote(Command):
    
    def __init__(self, console : View) -> None:
        super().__init__(console, 'Поиск заметки по заголовку.')
    
    def get_description (self) -> str:
        return super().get_description()
    
    def execute(self) -> None:
        super().get_console().search_note()