# PS02-Requests

# Поиск репозиториев на GitHub

Этот скрипт выполняет поиск репозиториев на GitHub, которые содержат код HTML. Он использует GitHub API для получения данных о репозиториях, соответствующих запросу.

## Зависимости

Для работы скрипта вам нужно установить библиотеку `requests`, которая используется для отправки HTTP-запросов.

### Установка зависимостей

1. Установите Python 3.x с официального сайта: https://www.python.org/downloads/
2. Установите библиотеку `requests` с помощью pip:
    ```bash
    pip install requests
    ```

## Как использовать

1. Запустите скрипт:
    ```bash
    python main.py
    ```

2. Скрипт отправит GET-запрос к GitHub API для поиска репозиториев, содержащих ключевое слово `html`. В ответ вы получите JSON-данные с информацией о найденных репозиториях.
3. Статус-код ответа и содержимое JSON будет выведено в консоль.

### Пример вывода:
```bash
Статус-код: 200
{
    "total_count": 12345,
    "incomplete_results": false,
    "items": [
        {
            "id": 123456,
            "name": "example-repo",
            "full_name": "username/example-repo",
            "html_url": "https://github.com/username/example-repo",
            "description": "An example repository containing HTML code",
            "language": "HTML",
            ...
        },
        ...
    ]
}
