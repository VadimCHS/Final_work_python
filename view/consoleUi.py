from controller.controller import Controller
from view.view import View
from view.main_menu import MainMenu
from view.menu import Menu


class Console(View):

    def __init__(self) -> None:
        self.__main_menu = MainMenu(self)
        self.__controller = Controller(self)
        self.__count_menu = 0
        self.__work = True
    
    def start(self) -> None:
        self.__print_answer('Добро пожаловать в консольное приложение "заметки".')
        self.menu(self.__main_menu)
        pass
          
    def menu(self, menu:Menu) -> None:
        self.__count_menu += 1
        while self.__work:
            self.__print_answer(menu.menu())
            self.execute(menu)

        self.__count_menu -= 1
        if self.__count_menu != 0:
            self.__work = True

    def __print_answer(self, text:str) -> None:
        print(text)

    def execute(self, menu:Menu) -> None:
        choice = input('Выберите пункт меню: ')
        if choice.isdigit() and self.check_number_menu(choice, menu):
            menu.execute(int(choice))

    def check_number_menu(self, number:int, menu:Menu) -> bool:
        return 0 < int(number) <= menu.get_size()

    def create_note(self) -> None:
        title = input('Заголовок: ')
        content = input('Содержание: ')
        self.__controller.create_note(title, content)

    def show_notes(self) -> None:
        self.__print_answer(self.__controller.show_notes())

    def search_note(self) -> None:
        serch = input('Поиск: ')
        self.__print_answer(self.__controller.search_note(serch))

    def edit_note(self) -> None:
        id = input('Введите номер заметки: ')
        if id.isdigit() and self.__controller.check_note(int(id)):
            title = input('Заголовок: ')
            if title == '':
                title = None
            content = input('Содержание: ')
            if content == '':
                content = None
            self.__controller.edit_note(int(id), title, content)
    
    def delete_note(self) -> None:
        id = input('Введите номер заметки: ')
        if id.isdigit() and self.__controller.check_note(int(id)):
            self.__controller.delete_note(int(id))


    def save_notes(self) -> None:
        self.__controller.save_notes()

    def read_notes(self) -> None:
        self.__controller.read_notes()

    def error(self) -> None:
        self.__print_answer('')

    def exit(self) -> None:
        self.__work = False