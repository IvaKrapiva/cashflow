Документация проекта "Движение денежных средств (ДДС)"

Основные функции

Добавление, редактирование и удаление записей ДДС.
Фильтрация записей по дате, типу, категории, подкатегории и статусу.
Управление справочниками (типы, категории, подкатегории, статусы) через веб-страницы.
Простая навигация с помощью кнопок.

Технологии

Backend: Django 5.2.1, Python 3.9+
Frontend: Bootstrap 5.3 (через CDN)
База данных: SQLite (db.sqlite3)
Инструменты: Visual Studio Code, SQLPro for SQLite, Terminal (macOS)

Требования

Операционная система: Windows, macOS (рекомендуется Ventura или новее)
Инструменты:
Visual Studio Code (редактирование кода)
SQLPro for SQLite (управление базой данных)
Terminal (встроенный в macOS)




Установка

Клонирование проекта:

Откройте Terminal и перейдите в нужную директорию:cd ~/path/to/your/projects


Склонируйте репозиторий: git clone https://github.com/IvaKrapiva/cashflow cashflow_project


Перейдите в папку проекта:cd cashflow_project




Настройка виртуального окружения:

Создайте виртуальное окружение:python3 -m venv venv


Активируйте его:source venv/bin/activate




Настройка базы данных:

Убедитесь, что файл db.sqlite3 находится в корневой папке проекта.
Выполните миграции для создания таблиц: python3 manage.py migrate





Запуск сервера:

Запустите сервер разработки: python3 manage.py runserver


Откройте браузер и перейдите по адресу: http://127.0.0.1:8000/.



Использование
Главная страница

URL: http://127.0.0.1:8000/
Функции:
Просмотр списка записей ДДС.
Фильтрация записей по дате, типу, категории, подкатегории и статусу.
Добавление новой записи ДДС.
Навигация по справочникам.


Инструкции:
На главной странице вы увидите таблицу с существующими записями ДДС.
Используйте форму фильтрации:
Установите диапазон дат (Дата от и Дата до).
Выберите тип, категорию, подкатегорию или статус.
Нажмите «Фильтровать» для применения фильтров.
Нажмите «Сбросить» для очистки фильтров.


Нажмите «Добавить запись» для создания новой записи ДДС.



Управление справочниками

Типы:
Список типов: http://127.0.0.1:8000/types/
Добавление типа: http://127.0.0.1:8000/types/create/


Категории:
Список категорий: http://127.0.0.1:8000/categories/
Добавление категории: http://127.0.0.1:8000/categories/create/


Подкатегории:
Список подкатегорий: http://127.0.0.1:8000/subcategories/
Добавление подкатегории: http://127.0.0.1:8000/subcategories/create/

Статусы:
Список статусов: http://127.0.0.1:8000/statuses/
Добавление статусов: http://127.0.0.1:8000/statuses/create/


Инструкции:
На главной странице в разделе «Справочники» нажмите на кнопку, например, «Типы».
На странице списка нажмите «Добавить тип» (или аналогичную кнопку для других справочников).
Заполните форму (например, введите название типа) и нажмите «Сохранить».
Для возврата на главную страницу нажмите «На главную».



Добавление записи ДДС

URL: http://127.0.0.1:8000/create/
Инструкции:
На главной странице нажмите «Добавить запись».
Заполните форму:
Укажите дату.
Введите сумму.
Выберите тип, категорию, подкатегорию (если есть) и статус.


Нажмите «Сохранить».
Вы будете перенаправлены на главную страницу, где новая запись появится в таблице.



Проверка данных в базе

Инструмент: SQLPro for SQLite
Инструкции:
Откройте SQLPro for SQLite.
Выберите File > Open и укажите путь к db.sqlite3 (в корне проекта).
Выполните запросы для проверки данных:
Список записей ДДС:SELECT * FROM dds_cashflow;


Типы:SELECT * FROM dds_type;


Категории:SELECT c.name, t.name AS type_name FROM dds_category c JOIN dds_type t ON c.type_id = t.id;


Подкатегории:SELECT s.name, c.name AS category_name FROM dds_subcategory s JOIN dds_category c ON s.category_id = c.id;




Для экспорта данных: File > Export и выберите формат (например, CSV).



Разработка
Структура проекта

cashflow/: Основной каталог настроек проекта.
settings.py: Настройки проекта (база данных, логирование и т.д.).
urls.py: Основные маршруты.


dds/: Приложение для управления ДДС.
models.py: Модели данных (CashFlow, Type, Category, Subcategory, Status).
views.py: Представления для обработки запросов.
forms.py: Формы (CashFlowFilterForm, CategoryForm, SubcategoryForm и т.д.).
urls.py: Маршруты приложения.
templates/dds/: Шаблоны HTML.


db.sqlite3: Файл базы данных SQLite.

Добавление новых функций

Создание новой модели:
Откройте dds/models.py и добавьте новую модель:class NewModel(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name


Создайте миграции:python3 manage.py makemigrations
python3 manage.py migrate




Добавление маршрута:
В dds/urls.py добавьте новый маршрут:path('newmodel/', views.newmodel_list, name='newmodel_list'),


В dds/views.py создайте представление:def newmodel_list(request):
    newmodels = NewModel.objects.all()
    return render(request, 'dds/newmodel_list.html', {'newmodels': newmodels})




Создание шаблона:
Создайте файл templates/dds/newmodel_list.html:<!DOCTYPE html>
<html lang="ru">
<head>
    <meta charset="UTF-8">
    <title>Список новых моделей</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
</head>
<body>
    <div class="container">
        <h1 class="mt-4">Список новых моделей</h1>
        <table class="table table-striped">
            <thead>
                <tr><th>Название</th></tr>
            </thead>
            <tbody>
                {% for model in newmodels %}
                    <tr><td>{{ model.name }}</td></tr>
                {% empty %}
                    <tr><td class="text-center">Записи отсутствуют</td></tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>
