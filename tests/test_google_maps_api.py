import json
import allure
from utils.api import Gooogle_maps_api
from utils.cheking import Checking
from requests import Response

'''Создание, изменение и удалние новой локации'''


@allure.epic('Test create place')
class Test_create_place():

    @allure.description('Test created, update, delete new place')
    def test_create_new_place(self):

        print('\nМетод POST')
        result_post = Gooogle_maps_api.create_new_place()
        place_id = result_post.json().get('place_id')
        Checking.check_status_code(result_post, 200)
        # token = json.loads(result_post.text)
        # print(list(token))
        Checking.check_json_token_contain(
            result_post, ['status', 'reference', 'id'])
        Checking.check_json_token(
            result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        Checking.check_json_token_value(result_post, 'status', 'OK')
        Checking.check_json_token_value(result_post, 'scope', 'APP')

        print('Метод GET after POST')
        result_get = Gooogle_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(
            result_get, ['location', 'accuracy', 'name', 'phone_number',
                         'address', 'types', 'website', 'language'])
        Checking.check_json_token_value(
            result_get, 'address', '29, side layout, cohen 09')

        print('Метод PUT')
        result_put = Gooogle_maps_api.put_new_place(place_id)
        Checking.check_status_code(result_put, 200)
        Checking.check_json_token(result_put, ['msg'])
        Checking.check_json_token_value(
            result_put, 'msg', 'Address successfully updated')

        print('Метод GET after PUT')
        result_get = Gooogle_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 200)
        Checking.check_json_token(
            result_get, ['location', 'accuracy', 'name', 'phone_number',
                         'address', 'types', 'website', 'language'])
        Checking.check_json_token_value(
            result_get, 'address', 'Kyiv Bylvarno-kydravskay 17B, UA')

        print('Метод DELETE')
        result_delete = Gooogle_maps_api.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 200)
        Checking.check_json_token(result_delete, ['status'])
        Checking.check_json_token_value(
            result_delete, 'status', 'OK')

        print('Метод GET after DELETE')
        result_get = Gooogle_maps_api.get_new_place(place_id)
        Checking.check_status_code(result_get, 404)
        Checking.check_json_token(result_get, ['msg'])
        Checking.check_json_token_search_word_in_value(
            result_get, 'msg', 'Get operation failed, looks like place_id  doesn\'t exists')

        print('Метод DELETE after DELETE')
        result_delete = Gooogle_maps_api.delete_new_place(place_id)
        Checking.check_status_code(result_delete, 404)
        Checking.check_json_token(result_delete, ['msg'])
        Checking.check_json_token_value(
            result_delete, 'msg', "Delete operation failed, looks like the data doesn't exists")

    print('Тестрирование Создание, изменение и удалние новой локации прошло успешно!!!')
