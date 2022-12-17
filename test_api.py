import pytest as pytest

from app import app


@pytest.fixture()
def client():
    return app.test_client()


@pytest.fixture()
def post_keys():
    return {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk", "short_content1",
            "short_content2"}


@pytest.fixture()
def post_keys_id():
    return {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk", "short_content1",
            "short_content2", "comments", "sum_of_comments"}


def test_api_posts(client, post_keys):
    resp = client.get('/api/posts/')
    assert resp.status_code == 200
    assert isinstance(resp.json, list)
    for i in resp.json:
        assert isinstance(i, dict)
        assert set(i.keys()) == post_keys


def test_api_posts_id(client, post_keys_id):
    resp = client.get('/api/posts/1')
    assert resp.status_code == 200
    assert isinstance(resp.json, dict)
    assert set(resp.json.keys()) == post_keys_id
