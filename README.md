# SKYPROGRAM

Автор: Кравченко Анна


## О чем этот проект?
### *В данном проекте реализованы следующие представления страниц во Flask:*
* **Лента**\
    Список всех постов. У каждого выводится автор, укороченный до 50 символов текст, количество просмотров , ссылка, которая ведет на пост. 
* **Подробное содержание поста**\
    Страничка с подробной информацией про пост. 
* **Поиск постов, содержащих слово**\
    Форма поиска, отправляется по нажатию на Enter. После нее – результаты поиска. 
* **Поиск постов конкретного пользователя**\
    Посты выбранного пользователя по порядку
____
### *Каким образом проект реализован?*
Главный файл запуска app.py
Страницы api реализованы с использованием блюпринта (папка api_bp)
Страницы ленты и подробное содержание поста - блюпринт (папка main_bp)

#### *Функции, использованные в проекте*
1. load_json(filepath)
2. get_posts_all()
3. get_comments_all()
4. get_posts_by_user(user_name)
5. get_comments_by_post_id(post_id)
6. search_for_posts(query)
7. get_post_by_pk(pk)
