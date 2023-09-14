from model.model import Model
from model.file.SaveReadJson import SaveReadJson
from view.view import View


class Controller:

    def __init__(self, console:View) -> None:
        self.__model = Model()
        self.__console = console
        self.__path = 'notes.json'
        self.__save_read = SaveReadJson(self.__path)

    def create_note(self, title:str, content:str) -> None:
        self.__model.creat_note(title, content)

    def show_notes(self) -> str:
        return self.__model.get_str_notes()

    def search_note(self, search:str) -> str:
        return self.__model.search_note(search)
    
    def edit_note(self, id:int, title:str, content:str) -> None:
        self.__model.edit_note(id, title, content)

    def delete_note(self, id:int) -> None:
        self.__model.delete_note(id)

    def save_notes(self) -> None:
        self.__save_read.save_file(self.__model.get_list_notes())

    def read_notes(self) -> None:
        self.__model.clear_list_notes()
        temp = self.__save_read.read_file()
        for el in temp:
            self.__model.creat_note(el.get('title'), el.get('content'), el.get('id'), el.get('time'))

    def check_note(self, id:int) -> bool:
        if self.__model.check_note(id):
            return True
        return False