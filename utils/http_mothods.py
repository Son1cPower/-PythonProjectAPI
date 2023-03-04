import requests
import allure
from utils.logger import Logger

'''Список HTTP методов'''


class Http_methods:
    headers = {"Content-Type": 'application/json'}
    cookie = ""

    @staticmethod
    def get(url):
        with allure.step("GET"):
            Logger.add_request(url, method='GET')
            resoult = requests.get(
                url, headers=Http_methods.headers, cookies=Http_methods.cookie)
            Logger.add_response(resoult)
            return resoult

    @staticmethod
    def post(url, body):
        with allure.step("POST"):
            Logger.add_request(url, method='POST')
            resoult = requests.post(
                url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
            Logger.add_response(resoult)
            return resoult

    @staticmethod
    def put(url, body):
        with allure.step("PUT"):
            Logger.add_request(url, method='PUT')
            resoult = requests.put(
                url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
            Logger.add_response(resoult)
            return resoult

    @staticmethod
    def delete(url, body):
        with allure.step("DELETE"):
            Logger.add_request(url, method='DELETE')
            resoult = requests.delete(
                url, json=body, headers=Http_methods.headers, cookies=Http_methods.cookie)
            Logger.add_response(resoult)
            return resoult
