## Получение уведомлений о проверенных работах в Telegram

### Описание

Скрипт отправляет запросы на [API сайта DEVMAN](https://dvmn.org/api/docs/) для того, чтобы узнать изменился ли статус проверки работ. В случае изменения статуса отправляется сообщение в Telegram.

### Как установить

У вас должен быть установлен Python3. Затем используйте `pip` (или `pip3`, если есть конфликт с Python2) для установки зависимостей:

```
pip install -r requirement.txt
```

Рекомендуется использовать [virtualenv/venv](https://docs.python.org/3/library/venv.html) для изоляции проекта.

Также необходимо добавить следующие переменные окружения:

1. ```DEVMAN_TOKEN``` - это API токен DEVMAN, который можно получить [зарегистрировавшись на сайте](https://dvmn.org/modules/).
2. ```BOT_TOKEN``` - токен Telegram бота, который можно получить после регистрации нового бота у [BotFather.](https://telegram.me/BotFather)

Для работы скрипту в качестве аргумента необходимо передать ```chat_id``` - ID вашего чата . Для его получения достаточно написать в Telegram специальному боту: [@useringobot](https://telegram.me/userinfobot). 

### Пример использования
Запуск скрипта с ```chat_id``` в качестве аргумента:

```console
$ python3 --chat_id=<ваш chat_id>
```

