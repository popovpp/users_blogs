# users_blogs
 Users blogs service
Python 3.8, Django 3.1.1, SQLite3.
Requirements.txt прилагается.
Папку проекта расположить в заранее подготовленное виртуальное окружение Python.
Для запуска приложения выполнить команду:
python manage.py runserver.
Вход в приложение:
127.0.0.0:8000/accounts/login/ ,
Для администратора модно дополнительно воспользоваться:
127.0.0.0:8000/admin/ .
В систему заведены тестовые пользователи (login : password):
admin : dtrrrv ;
Pavel : 31121972Po ;
Vova : 30112020Qa ;
Kolya : 203040uh .
Посты начинают поступать в ленту новостей после выполнения подписки, и, соответственно
прекращают поступать после выполнения прекращения подписки. После выполнения подписки посты созданные ранее в 
новостную ленту не попадают. После выполнения прекращения подписки посты, пришедшие в ленту новостей ранее не удаляются.
Посты можно удалять только через админку. При отсутствии настроенного сервиса отправки электронной почты, при создании постов в консоль 
выдаются сообщения о неотправке электронных писем подписчикам автора поста (скриншот прилагается).
