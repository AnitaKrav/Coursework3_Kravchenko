from flask import Blueprint, jsonify

from logger import get_logger
from utils import utils

api_bp = Blueprint('api_bp', __name__, url_prefix='/api/')

logger = get_logger(__name__)


@api_bp.route('posts/')
def api_posts():
    posts = utils.get_posts_all()
    logger.info('Был запрос "/api/posts/"')
    return jsonify(posts)


@api_bp.route('posts/<int:post_id>')
def api_get_post(post_id):
    post = utils.get_post_by_pk(post_id)
    comments = utils.get_comments_by_post_id(post_id)
    post['comments'] = comments
    post['sum_of_comments'] = len(comments)
    logger.info('Был запрос "/api/posts/id"')
    return jsonify(post)
