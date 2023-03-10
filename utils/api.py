from utils.http_mothods import Http_methods


'''Методы для тестирования Gooogle maps API'''
base_url = 'https://rahulshettyacademy.com'  # Базовая URL
key = "?key=qaclick123"  # Параметр для всех запросов для URL


class Gooogle_maps_api():

    '''Метод для создания новой локации'''
    @staticmethod
    def create_new_place():
        post_resource = "/maps/api/place/add/json"  # Resource for POST URL
        json_body_for_create_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }
        post_url = base_url + post_resource + key
        print(post_url)
        result_post = Http_methods.post(
            post_url, json_body_for_create_new_place)
        print(result_post.text)
        return result_post

    '''Метод для проверки новой локации'''
    @staticmethod
    def get_new_place(place_id):
        get_resource = "/maps/api/place/get/json"  # Resource for GET URL
        get_url = base_url + get_resource + key + "&place_id=" + place_id
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get

    '''Метод для обновления новой локации'''
    @staticmethod
    def put_new_place(place_id):
        put_resource = "/maps/api/place/update/json"  # Resource for PUT URL
        json_body_for_update_new_place = {
            "place_id": place_id,
            "address": "Kyiv Bylvarno-kydravskay 17B, UA",
            "key": "qaclick123"
        }
        put_url = base_url + put_resource + key
        print(put_url)
        result_put = Http_methods.put(put_url, json_body_for_update_new_place)
        print(result_put.text)
        return result_put

    '''Метод для удаления новой локации'''
    @staticmethod
    def delete_new_place(place_id):
        delete_resource = "/maps/api/place/delete/json"  # Resource for PUT URL
        json_body_for_delete_new_place = {
            "place_id": place_id
        }
        delete_url = base_url + delete_resource + key
        print(delete_url)
        result_delete = Http_methods.delete(
            delete_url, json_body_for_delete_new_place)
        print(result_delete.text)
        return result_delete
