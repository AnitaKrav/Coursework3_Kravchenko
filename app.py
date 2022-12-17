from flask import Flask, render_template, request

from api_bp.api import api_bp
from main_bp.main import main_bp
from utils import utils

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

app.register_blueprint(api_bp)
app.register_blueprint(main_bp)


@app.route('/search/', methods=['POST'])
def get_posts_by_word():
    posts = utils.search_for_posts(request.form.get('word'))
    sum_of_posts = len(posts)
    return render_template('search.html', posts=posts, sum_of_posts=sum_of_posts)


@app.route('/users/<user_name>/')
def get_posts_by_user(user_name):

    posts = utils.get_posts_by_user(user_name)
    sum_of_posts = len(posts)
    return render_template('user-feed.html', posts=posts, sum_of_posts=sum_of_posts, user_name=user_name)

@app.errorhandler(404)
def pageNot(error):
    return ("Страница не найдена, 404", 404)

@app.errorhandler(500)
def pageNot(error):
    return ("Ошибка на стороне сервера, 500", 500)


if __name__ == "__main__":
    app.run()
