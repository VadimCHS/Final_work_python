import json

class SaveReadJson:

    def __init__(self, path:str) -> None:
        self.__path = path

    def save_file(self, file) -> None:
        with open(self.__path, 'w') as outfile:
            json.dump(file, outfile)
                

    def read_file(self) -> list:
        with open(self.__path) as json_file:
            temp = json.load(json_file)
            return temp
       