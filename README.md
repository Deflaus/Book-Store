Инструкция по установке и настройке проекта:
--------------------------------------------

1. Инструкция по запуску проекта:

1) Клонируем репозиторий с проектом;
2) Переходим в папку с проектом;
3) Открываем терминал в данной директории и прописываем команду pipenv install для установки зависимостей;
4) Прописываем команду в запущенном терминале для запуска вирутального окружения pipenv shell;
5) Прописываем команду в запущенном терминале для запуска сервера python manage.py runserver;

2. Инструкция по запуску Celery:

1) Запускаем Rabbitmq-server;
2) В новом терминале с запущенным виртуальным окружением(пункты 2-4 инструкции по запуску проекта) прописываем команду celery -A myshop worker -l info -P gevent;

Инструкция по работе с API:
---------------------------

GET запросы:
1) url http://127.0.0.1:8000/books/list/
Возвращает список всех объектов книг в формате json

Пример:
{
    {
        "title": "451 градус по Фаренгейту"
    },
    {
        "title": "Марсианские хроники"
    },
    {
        "title": "Мы"
    }
}

2) url http://127.0.0.1:8000/books/authors/
Возвращает список всех объектов авторов в формате json

Пример:
{
    {
        "fio": "Евге́ний Ива́нович Замя́тин",
        "books": [
            {
                "title": "Мы"
            }
        ],
        "books_count": 1
    },
    {
        "fio": "Рэй Брэдбери",
        "books": [
            {
                "title": "451 градус по Фаренгейту"
            },
            {
                "title": "Марсианские хроники"
            }
        ],
        "books_count": 2
    }
}

POST запрос:
url http://127.0.0.1:8000/orders/add/
Принимает в теле запроса json: название книги, телефонный номер заказчика, комментарий по заказу(необязательно). Формат сообщения:
{
    "book": "451 градус по Фаренгейту",
    "phone_number": "79300392521",
    "comment": "test_comment"
}

При успешном заказе вернется код ответа 201, отправится сообщение об успешном заказе на почту, которое можно просмотреть в терминале с запущенным Celery.
При неуспешном заказе вернется код ответа 404.