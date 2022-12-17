import json

all_posts = 'data/posts.json'
all_comments = 'data/comments.json'


def load_json(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_posts_all():
    posts = load_json(all_posts)
    for post in posts:
        post['short_content1'] = post['content'][:100]
        post['short_content2'] = ' '.join(post['content'].split(' ')[:10])
    return posts


def get_comments_all():
    return load_json(all_comments)


def get_posts_by_user(user_name):
    """
Возвращает посты определенного пользователя.
"""
    return [post for post in get_posts_all() if post['poster_name'].lower() == user_name.lower()]


def get_comments_by_post_id(post_id):
    """
Возвращает комментарии определенного поста.
"""
    return [comment for comment in get_comments_all() if comment['post_id'] == post_id]


def search_for_posts(query):
    """
Возвращает список постов по ключевому слову
"""
    return [post for post in get_posts_all() if query.lower() in post['content'].lower()]


def get_post_by_pk(pk):
    """
Возвращает один пост по его идентификатору.
"""
    posts = get_posts_all()
    for post in posts:
        if post['pk'] == pk:
            return post
