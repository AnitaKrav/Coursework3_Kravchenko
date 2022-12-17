from flask import Blueprint, render_template

from utils import utils

main_bp = Blueprint('main_bp', __name__)


@main_bp.route('/')
def page_index():
    posts = utils.get_posts_all()
    return render_template('index.html', posts=posts)


@main_bp.route('/posts/<int:post_id>')
def get_post(post_id):
    post = utils.get_post_by_pk(post_id)
    comments = utils.get_comments_by_post_id(post_id)
    sum_of_comments = len(comments)
    return render_template('post.html', post=post, comments=comments, sum_of_comments=sum_of_comments)
