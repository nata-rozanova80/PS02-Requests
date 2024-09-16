import requests
import pprint

# URL для поиска репозиториев на GitHub
url = 'https://api.github.com/search/repositories'

# Параметры запроса: ищем репозитории с кодом html
params = {
    'q': 'html',
}

# Отправляем GET-запрос
response = requests.get(url, params=params)

# Печатаем статус-код ответа
print("Статус-код:", response.status_code)

# Печатаем содержимое ответа в формате JSON
pprint.pprint(response.json())