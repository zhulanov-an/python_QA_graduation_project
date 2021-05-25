# pythonQASelenoid

## Набор тестов для проверки opencart
- helpers.py - вспомогательные методы
- test_account_page.py - проверка отображения элементов страницы для регистрации пользователя
- test_admin_login_page.py - проверка формы авторизации администратора
- test_admin_product_page.py - проверка отображения страницы конфигурации продуктов
- test_desktops_page.py - проверка отображения раздела Desktops
- test_login_logout.py - проверка ф-ла корректной/некорректной авторизации
- test_main_page.py - проверка отображения элементов посадочной страницы
- test_product_page.py - проверка отображения элементов страницы с продуктом

## Запуск Jenkins
1. Выполнить установку java
2. Выполнить загрузку пакета в формате war с ресурса `https://www.jenkins.io/download/`
3. Выполнить `java -jar jenkins.war --httpPort=8888`

## Локальный запуск opencart
1. Выполнить загрузку образа `docker pull bitnami/opencart`

2. Установить переменные среды:
- `PHPADMIN_PORT` - порт для PHPMyAdmin
- `LOCAL_IP` - IP адрес для запуска приложения OpenCart

3. Загрузить файл `https://gist.github.com/konflic/ecd93a4bf7666d97d62bcecbe2713e55`
и выполнить в директории с файлом `docker-compose up -d`

4. Для остановки выполнить `docker stop $(docker ps -q)`

В случае возникновения ошибок при запуске и т.п. попробовать
выполнить:
`docker system prune` и `docker volume prune`

## Локальный запуск selenoid
1. Установить Docker
2. Загрузить актуальный Configuration manager с ресурса `https://github.com/aerokube/cm/releases/`
3. Загрузить браузеры `./cm selenoid configure --browsers chrome;firefox;opera` (загрузится последняя и предпоследняя версии браузера)
4. Запустить cm: `./cm selenoid start --vnc`(stop для остановки)
5. Запустить selenoid-ui: `./cm selenoid-ui start`(stop для остановки)

## Запуск тестов
`pytest --browser opera -n 5 --alluredir=../allure_results` - запустить тесты в браузере Opera в 5 потоков с генерацией данных для отчета Allure
- `--browser` - браузер
- `-n` - указание количества потоков при многопоточном выполнении тестов
- `--alluredir=../allure_results` - директория для файлов Allure

## Отчет Allure
1. Загрузить Allure `https://github.com/allure-framework/allure2/releases`
2. Прописать путь к исполняемому файлу allure в переменных среды окружения
3. После запуска тестов с указанием `--alluredir` и в директории с файлами данных Allure запустить `allure serve`
