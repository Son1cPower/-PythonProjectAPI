'''Методы для проверки ответов наших запросов'''
import json
from requests import Response


class Checking():

    '''Метод для проверки Статус Кода'''
    @staticmethod
    def check_status_code(responce: Response, status_code):
        assert status_code == responce.status_code
        if responce.status_code == status_code:
            print("Success!!! Status Code = " + str(responce.status_code))
        else:
            print('Error!!! Status Code = ' + str(responce.status_code))

    '''Метод для проверки наличе всех полей в ответе'''
    @staticmethod
    def check_json_token(responce: Response, expected_value):
        token = json.loads(responce.text)
        assert list(token) == expected_value
        print("Responce with the same fileds like expected")

    '''Метод для проверки наличие некоторых полей в ответе'''
    @staticmethod
    def check_json_token_contain(responce: Response, expected_value):
        token = json.loads(responce.text)
        assert all(elem in list(token) for elem in expected_value)
        print("All fileds are present in responce")

    '''Метод для проверки значения полей в запросе'''
    @staticmethod
    def check_json_token_value(responce: Response, filed_name, expected_value):
        check_info = responce.json().get(filed_name)
        assert check_info == expected_value
        print(filed_name + " has correct value")

    '''Метод для проверки значения полей в запросе'''
    @staticmethod
    def check_json_token_search_word_in_value(responce: Response, filed_name, search_word):
        check_info = responce.json().get(filed_name)
        assert search_word in check_info
        print(filed_name + " has " + search_word + " in value")
