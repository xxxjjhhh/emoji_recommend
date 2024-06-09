# -*- coding: utf-8 -*-
import json

class JonsExecutor:
    def __init__(self) -> None:
        self.__read_path = '../asset/emoji_korean.json'
        self.__write_path = '../asset/emoji_vector.json'

    def read_file(self) -> list:
        with open(self.__read_path, encoding='utf-8') as file:
            json_data = json.load(file)

        return json_data
    
    def write_file(self, list_data) -> None:
        with open(self.__write_path, 'w', encoding='utf-8') as file:
            file.write(json.dumps(list_data))
