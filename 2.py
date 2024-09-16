import requests
import pprint

# URL API
url = 'https://jsonplaceholder.typicode.com/posts'

# Параметры запроса: userId равен 1
params = {
    'userId': 1,
}

# Отправляем GET-запрос
response = requests.get(url, params=params)

# Проверяем статус-код ответа
if response.status_code == 200:
    # Печатаем полученные записи в формате JSON
    pprint.pprint(response.json())
else:
    print(f"Ошибка {response.status_code}: Не удалось получить данные.")