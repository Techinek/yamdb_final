# yamdb_final
![yamdb_workflow](https://github.com/Techinek/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

REST API для сервиса YaMDb — база отзывов о различных произведения: фильмы, 
книги, музыка и прочее. Авторизация реализована по JWT-токенам. Пользователи
имеют возможность добавлять отзывы, просматривать их и изменять их.

Документация по эндпоинтам доступна по адресу: http://localhost/redoc/

## Запуск (docker)

Запустить docker-compose:

```docker-compose up```

При первом запуске для функционирования проекта обязательно выполнить миграции:

```docker-compose exec web python manage.py migrate```

Чтобы загрузить список сущностей в БД:

```docker-compose exec web python manage.py loaddata fixtures.json```

**Автор**: [Кусков Андрей](https://github.com/Techinek).
Документация по эндпоинтам: [http://51.250.100.130/redoc/](http://51.250.100.130/redoc/)
