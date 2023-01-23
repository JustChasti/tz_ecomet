--- Инструкция по запуску и работе ---

1) Склонировать репозиторий: git clone https://github.com/JustChasti/tz_ecomet
2) Созадть в папках /api и /parser .env файлы
    - по умолчанию настройки таковы:
        BASE_USER=gray
        BASE_PASSWORD=qm7hFSIW
        BASE_NAME=ecometbase
        BASE_HOST=postgres
        BASE_PORT=5432
    - они же указаны и docker-compose файле
    - Прошу обратить внимание, что не все настройки находятся в .env
    например в api/config.py указан хост парсера, на который идут запросы от api
3) Собрать docker-compose - коммандой docker-compose build
4) Запустить docker-compose - коммандой docker-compose up
5) При переходе по адресу: 'http://127.0.0.1:8000/docs#/' будет доступен сваггер:
    - предоставляет графический интерфейс для запросов (не требует postman)
    - содержит примеры правильного построения запросов
    - к примеру формат временного периода для (GET /city_stats)
