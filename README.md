
# Test exercise
### Python 3.11, Django 4.2, DRF, Celery, redis

### Разработано в ссответсвии с заданием:

* 1. Cущность книги. Эндпоинты viewset
  2. Модель пользователя. Эндпоинт регистрации. Авторизация - basic auth.
  3. Celery task - приветсвенное писбмо на почту при регистрации (yandex smtp)
  4. Работа с git. Слияние веток
  5. Контейнеризация в docker c postgres, redis

#### Список эндпонтов доступен по ссылке localhost/api/schema/swagger-ui/

* Перед запуском необходимо заполнить .env.dev 
для авторизационных данных postgres и yandex mail.

### Запуск:
    1.  docker-compose build
    2.  docker-compose up
