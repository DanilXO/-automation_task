# Test automation task

### Задание:
   см.[здесь](https://docs.google.com/spreadsheets/d/1IxOlfHQtonXjxr9wUw-vVSlkS_YHPpm0LnTjiWGX34U/edit#gid=381784469)

### Зависимости:
   см. [requirements.txt](https://github.com/DanilXO/automation_task/blob/master/requirements.txt)
   Для тестирования используется СhromeDriver v80
   
### Структура проекта:
    ├── automation_task
        ├── drivers                        # Драйвера для браузеров
        ├── pages                          # Pages для реализации паттерна Page Object
            ├── base.py                    # Класс с общей реализацией
            ├── google_page.py             # Реализация логики работы со страницой google
            ├── mtc_bank_page.py           # Реализация логики работы со страницой МТС Банк
        ├── conftest.py                    # Настройки pytest                         
        ├── requirements.txt               # Необходимые зависимости
        ├── tests.py                       # Тестирование согласно заданию
