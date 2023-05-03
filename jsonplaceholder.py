import requests
import pytest

def test_get_users_status_code_equals_200():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    assert response.status_code == 200




import requests
import pytest

def test_users_list_is_not_empty():
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    data = response.json()
    assert len(data) > 0




import requests
import pytest

def test_get_user_posts_status_code_equals_200():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1/posts")
    assert response.status_code == 200


import requests
import pytest

def test_user_posts_list_is_not_empty():
    response = requests.get("https://jsonplaceholder.typicode.com/users/1/posts")
    data = response.json()
    assert len(data) > 0







import requests
import pytest

def test_post_comments_list_is_not_empty():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1/comments")
    data = response.json()
    assert len(data) > 0



import requests
import pytest

@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_post_status_code_equals_200(post_id):
    response = requests.get(f"https://jsonplaceholder.typicode.com/posts/{post_id}")
    assert response.status_code == 200




import requests
import pytest

def test_post_has_title_and_body():
    response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
    data = response.json()
    assert data["title"] != None
    assert data["body"] != None

