## «API для Yatube»

### Описание проекта:

Проект YaMDb собирает отзывы пользователей на произведения.
Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка». 
Произведению делятся по жанрам. 
Добавлять произведения, категории и жанры может только администратор.
Аутентифицированные пользователи могут оставлять отзывы и ставить оценки произведениям в диапазоне от одного до десяти.

Проект был подготовлен на основе **Redoc** API документации. 
  Подробнее про **Redoc** – https://redocly.com/redoc/
 

Авторизация в проекте настроена через получения на почту `confirmation_code`, после получения которого можно получить **JWT**-токен для дальнейшей работы в системе.
  Подробнее про **JWT** – https://jwt.io/introduction
 
В системе есть разделение ролей: администратор, модератор и пользователь.

### Как запустить проект:

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

Просмотр API документации: 

```
http://127.0.0.1:8000/redoc/
```


### Примеры API запросов

**Получение confirmation_code на почту**

Запрос - POST `http://127.0.0.1:8000/api/v1/auth/signup/`

```
{

    "email": "string",
    "username": "string"

}
```

Ответ

```
{

    "email": "string",
    "username": "string"

}
```


**Получение JWT токена**

Запрос - POST `http://127.0.0.1:8000/api/v1/auth/token/`

```
{

    "username": "string",
    "confirmation_code": "string"

}
```

Ответ

```
{

    "token": "string"

}
```



**Получение списка призведений**

Запрос – GET `http://127.0.0.1:8000/api/v1/titles/`


Ответ

```
[

{

    "count": 0,
    "next": "string",
    "previous": "string",
    "results": 

[

{

    "id": 0,
    "name": "string",
    "year": 0,
    "rating": 0,
    "description": "string",
    "genre": 

[

    {}

],
"category": 

                {
                    "name": "string",
                    "slug": "string"
                }
            }
        ]
    }

]
```

**Добавление нового отзыва**

Запрос - `http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/`

```
{

    "text": "string",
    "score": 1

}
```

Ответ

```
{

    "id": 0,
    "text": "string",
    "author": "string",
    "score": 1,
    "pub_date": "2019-08-24T14:15:22Z"

}
```

