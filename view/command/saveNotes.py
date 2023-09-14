from view.view import View
from view.command.command import Command


class SaveNotes(Command):
    def __init__(self, console : View) -> None:
        super().__init__(console, 'Сохранить.')
    
    def get_description (self) -> str:
        return super().get_description()
    
    def execute(self) -> None:
        super().get_console().save_notes()