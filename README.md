## Пример проекта API автотестов для сервиса [petstore.swagger.io](https://petstore.swagger.io/)
<p align="center">
    <img src="readme_images/screenshot/logo.png"/>&nbsp;
</p>

## Используемые технологии
<p>
<a href="https://www.python.org/"><img src="readme_images/logo/python.png" width="40" height="40"  alt="PYTHON"/></a>
<a href="https://docs.pytest.org/en/"><img src="readme_images/logo/pytest.png" width="40" height="40"  alt="PYTEST"/></a>
<a href="https://www.jetbrains.com/pycharm/"><img src="readme_images/logo/pycharm.png" width="40" height="40"  alt="PYCHARM"/></a>
<a href="https://pypi.org/project/requests/"><img src="readme_images/logo/requests.png" width="40" height="40"  alt="REQUESTS"/></a>
<a href="https://github.com/"><img src="readme_images/logo/github.png" width="40" height="40"  alt="GITHUB"/></a>
<a href="https://www.jenkins.io/"><img src="readme_images/logo/jenkins.png" width="40" height="40"  alt="JENKINS"/></a>
<a href="https://allurereport.org/"><img src="readme_images/logo/allure_report.png" width="40" height="40"  alt="ALLUREREPORT"/></a>
<a href="https://qameta.io/"><img src="readme_images/logo/allure_testops.png" width="40" height="40"  alt="ALLURETESTOPS"/></a>
<a href="https://telegram.org/"><img src="readme_images/logo/tg.png" width="40" height="40"  alt="TELEGRAM"/></a>
</p>

## API тесты:
Были протестированы следующие методы:
* POST pet
* GET /findByStatus pet
* PUT pet
* DELETE pet
* POST /order
* GET /order/ {order_id}
* DELETE /order/ {order_id}

Тесты проверяют:
* Статус код
* Значение в response
* Cхема ответа

 Пример запущенного теста (POST pet):
<p align="center">
    <img src="readme_images/screenshot/request_example.png"/>&nbsp;
</p>

## Запуск тестов

### Для локального запуска
1. Склонируйте репозиторий
2. Откройте проект в PyCharm
3. Введите в терминале команду
``` 
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest .
```
### Для запуска тестов из [Jenkins](https://jenkins.autotests.cloud/job/qa_guru_graduation_project_API_petstore/):
Для запуска тестов из **Jenkins** нажмите «Собрать сейчас».

<img src="readme_images/screenshot/jenkins_project_page.png"/>&nbsp;

### Для запуска тестов из [Allure Test Ops](https://allure.autotests.cloud/project/3710/):
Реализована интеграция с **Allure Test Ops**, откуда напрямую можно запускать тесты. В **Allure Test Ops** также есть возможность настраивать параметры запуска, выбирая конкретные тестовые случаи.

<img src="readme_images/screenshot/allure_job.png"/>&nbsp;
<img src="readme_images/screenshot/allure_launch.png"/>&nbsp;

## Отчет о пройденных тестах в [Allure Report](https://jenkins.autotests.cloud/job/qa_guru_graduation_project_API_petstore/allure/) и тестовая документация:

### Локальный запуск тестов

Для MacOS введите в терминале команду 
```
allure serve allure-results
``` 
Для Windows введите в терминале команду 
```
allure.bat serve allure-results
``` 

### Запуск тестов из Jenkins или Allure Test Ops

**Allure Report** можно открыть на странице Jenkins (см. скриншот Jenkins в разделе выше) и содержит графику, детализацию выполнения тестов, различные виды вложений (запросы, ответы и т.д.).
<img src="readme_images/screenshot/allure_report_1.png"/>&nbsp;
<img src="readme_images/screenshot/allure_report_2.png"/>&nbsp;

**Allure Test Ops** также содержит информацию о прохождении и создает тестовую документацию.
<img src="readme_images/screenshot/allure_test_ops_1.png"/>&nbsp;
<img src="readme_images/screenshot/allure_test_ops_2.png"/>&nbsp;

## Нотификация о прохождении тестов

После выполнения тестового запуска будет отправлено телеграмм-сообщение со следующей информацией:
* общее количество тестов и продолжительность выполнения
* процент пройденных/неудачных/пропущенных/и т.д. тестов
* ссылка на allure отчет

<p align="center">
<img src="readme_images/screenshot/tg_report.png" height="400"/>&nbsp;
</p>

Для отправки сообщений в телеграм была использована [notifications library](https://github.com/qa-guru/allure-notifications), создан и добавлен в чат телеграм бот.