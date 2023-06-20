import requests


def get_headers(token):
    return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(token)
        }


def create_new_folder(folder_name, token):
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = get_headers(token)
    params = {"path": folder_name}
    response = requests.put(url, headers=headers, params=params)
    return response.status_code


def delete_new_folder(folder_name, token):
    url = "https://cloud-api.yandex.net/v1/disk/resources"
    headers = get_headers(token)
    params = {"path": folder_name,
              "permanently": True}
    requests.delete(url, headers=headers, params=params)
