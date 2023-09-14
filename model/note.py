from datetime import datetime


class Note:

    def __init__(self, id:int, title:str, content:str, time:str) -> None:
        if time == None:
            time = self.__time_now()
        self.__note = {'id':id, 'title':title, 'content':content, 'time':time}

    def get_note(self) -> dict:
        return self.__note

    def set_note(self) -> dict:
        return self.__note
    
    def set_title(self, text:str) -> None:
        self.__note.update({'title':text, 'time':self.__time_now()})
    
    def set_content(self, text:str) -> None:
        self.__note.update({'content':text, 'time':self.__time_now()})

    def __time_now(self) -> str:
        return str(datetime.now())

    def get_time(self) -> str:
        return self.__note.get('time')