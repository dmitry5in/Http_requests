import requests
from pprint import pprint


# Задача №1

hero_list = ['Captain America', 'Thanos', 'Hulk']


def smartest_hero(list_hero):
    hero_intelligence = {}
    url = 'https://superheroapi.com/api/2619421814940190/'
    for hero in list_hero:
        response = requests.get(url + '/search/' + hero)
        for element in response.json()['results']:
            hero_intelligence[element['name']] = element['powerstats']['intelligence']
    smartest = sorted(hero_intelligence)
    return f'Самый умный супергерой - {smartest[-1]}'


print(smartest_hero(hero_list))



# Задача №2

class YaUploader:

    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url = 'https://cloud-api.yandex.net/'
        headers = {'accept': 'application/json', 'authorization': f'{uploader.token}'}
        params = {'path': 'some folder/' + file_path}
        response = requests.get(url + 'v1/disk/resources/upload', params=params, headers=headers)
        upload_url = response.json()['href']
        response = requests.put(upload_url, files={'file': open(file_path, 'rb')})
        return

if __name__ == '__main__':
    path_to_file = '5.jpeg'
    token = ''
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)

