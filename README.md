# Тестовое задание: API-сервис для вопросов и ответов

## ТЗ
> ### Функциональные требования
> **Модели:**
> 1. **Question** – вопрос:
>     - `id`: int
>     - `text`: str (текст вопроса)
>     - `created_at`: datetime
>
> 2. **Answer** – ответ на вопрос:
>     - `id`: int
>     - `question_id`: int (ссылка на Question)
>     - `user_id`: str (идентификатор пользователя, например uuid)
>     - `text`: str (текст ответа)
>     - `created_at`: datetime
> ---
> **Методы API:**
> 1. **Вопросы (Questions):**
>     - `GET /questions/` — список всех вопросов
>     - `POST /questions/` — создать новый вопрос
>     - `GET /questions/{id}` — получить вопрос и все ответы на него
>     - `DELETE /questions/{id}` — удалить вопрос (вместе с ответами)
>
> 2. **Ответы (Answers):**
>     - `POST /questions/{id}/answers/` — добавить ответ к вопросу
>     - `GET /answers/{id}` — получить конкретный ответ
>     - `DELETE /answers/{id}` — удалить ответ
> ---
> **Логика:**
> - Нельзя создать ответ к несуществующему вопросу.
> - Один и тот же пользователь может оставлять несколько ответов на один вопрос.
> - При удалении вопроса должны удаляться все его ответы (каскадно).

## Инструкция по запуску

1. **Склонируйте репозиторий и перейдите в каталог:**
    ```bash
    git clone https://github.com/Sab8rz/Api-service-Hitalent-.git
    cd Api-service-Hitalent-
    ```

2. **Создайте и активируйте виртуальное окружение:**
    ```bash
    python -m venv venv
    source venv/Scripts/activate
    ```

3.  **Создайте файл `.env` в корне проекта** и настройте переменные:
    ```bash
    DJANGO_SECRET_KEY=django-insecure-ll$=vz3tve3op0h2cy4b@0w_nyg)fe&yqt$y52_n)x@l+6g9w@
    DEBUG=True
    DJANGO_LOGLEVEL=info
    DJANGO_ALLOWED_HOSTS=localhost
    DATABASE_ENGINE=postgresql_psycopg2
    DATABASE_NAME=hitalent
    DATABASE_USERNAME=ваше имя пользователя в PostgreSQL
    DATABASE_PASSWORD=ваш пароль в PostgreSQL
    DATABASE_HOST=db
    DATABASE_PORT=5432
    ```

4.  **Запустите приложение:**
    ```bash
    docker-compose -f compose.yml up --build
    ```

5.  **API будет доступно по адресу:** `http://localhost:8000/api/`

## Эндпоинты

### Вопросы (`/api/questions/`)
- `GET /` — список всех вопросов
- `POST /` — создать новый вопрос 
- `GET /{id}/` — получить вопрос и все ответы на него
- `DELETE /{id}/` — удалить вопрос (вместе с ответами)

### Ответы (`/api/answers/`)
- `GET /` — список всех ответов
- `GET /{id}/` — получить конкретный ответ
- `DELETE /{id}/` — удалить ответ

### Ответы к конкретному вопросу (`/api/questions/{id}/answers/`)
- `POST /` — добавить ответ к вопросу

>   При `POST` на `/api/questions/{id}/answers/`, `id` из URL перезаписывает значение `question_id`, переданное в теле JSON. Id берется автоматически из URL.

## Тесты

Запуск юнит-тестов:

```bash
docker-compose -f compose.yml run --rm web pytest hitalent/api/tests/ -v