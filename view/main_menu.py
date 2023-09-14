from view.command.exit import Exit
from view.command.deleteNote import DeleteNote
from view.command.readNotes import ReadNotes
from view.command.saveNotes import SaveNotes
from view.command.editNote import EditNote
from view.command.searchNote import SearchNote
from view.command.showNotes import ShowNotes
from view.command.addNote import AddNote
from view.menu import Menu
from view.view import View


class MainMenu(Menu):

    def __init__(self, console:View) -> None:
        self.__command_list = []
        self.__command_list.append(AddNote(console))
        self.__command_list.append(ShowNotes(console))
        self.__command_list.append(SearchNote(console))
        self.__command_list.append(EditNote(console))
        self.__command_list.append(SaveNotes(console))
        self.__command_list.append(ReadNotes(console))
        self.__command_list.append(DeleteNote(console))
        self.__command_list.append(Exit(console))

    def menu(self) -> str:
        count = 1
        str_builder = ''
        for i in self.__command_list:
            str_builder += (f"{count}. {i.get_description()}\n")
            count += 1
        return str_builder
    
    def get_size(self) -> int:
        return len(self.__command_list)
    
    def execute(self, choice:int) -> None:
        command = self.__command_list[choice - 1]
        command.execute()



