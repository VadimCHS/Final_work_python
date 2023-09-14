from view.view import View
from view.command.command import Command


class DeleteNote(Command):
    
    def __init__(self, console : View) -> None:
        super().__init__(console, 'Удалить заметку.')
    
    def get_description (self) -> str:
        return super().get_description()
    
    def execute(self) -> None:
        super().get_console().delete_note()