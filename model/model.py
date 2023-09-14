from model.note import Note

class Model:

    def __init__(self) -> None:
        self.__count_id = 1
        self.__list_notes = []
   
    def creat_note(self, title:str, content:str, id=None, time=None) -> None:
        if id == None:
            id = self.__count_id
        self.__list_notes.append(Note(int(id), title, content, time))
        self.__count_id = int(id) + 1

    def get_list_notes(self) -> list:
        list_notes = []
        for el in self.__list_notes:
            list_notes.append(el.get_note())
        return list_notes
    
    def __get_note_id(self, id:int) -> dict:
        for el in self.__list_notes:
            if el.get_note().get('id') == id:
                return el
        return None

    def __get_header(self) -> str:
        header = ['id', 'Заголовок', 'Содержание', 'Время(создания/изменения)']
        result = '\n' + '=' * 81 + '\n'
        result += f'{header[0]:>3} {header[1]:>4} {header[2]:>15} {header[3]:>50}'
        result += '\n' + '=' * 81 + '\n'
        return result

    def get_str_notes(self) -> str:
        result = self.__get_header()
        for el in self.__list_notes: 
            result += f'{self.__note_to_str(el.get_note())}'
        result += '\n' + '=' * 81 + '\n'   
        return result
    
    def search_note(self, search:str) -> str:
        result = self.__get_header()
        for el in self.__list_notes:
            if search in el.get_note().get('title'):
                result += self.__note_to_str(el.get_note())
        result += '\n' + '=' * 81 + '\n'
        return result
    
    def __note_to_str(self, note:dict) -> str:
        result = ''
        id = note.get('id')
        title = note.get('title')
        content = note.get('content')
        time = note.get('time')
        result += f'{id:>3}. {title:<13} {content:<11} {time:>50}\n'
        return result 
    
    def edit_note(self, id:int, title:str, content:str) -> None:
        if(title != None):
            self.__get_note_id(id).set_title(title)

        if(content != None):
            self.__get_note_id(id).set_content(content)
    
    def delete_note(self, id:int) -> bool:
        for el in self.__list_notes:
            if el.get_note().get('id') == id:
                self.__list_notes.remove(el)
                return True
        return False
    
    def clear_list_notes(self) -> None:
        self.__list_notes.clear()

    def check_note(self, id:int) -> bool:
        if self.__get_note_id(id) == None:
            return False
        return True
    