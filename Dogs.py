import requests
import pytest

def test_get_all_breeds_status_code_equals_200():
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    assert response.status_code == 200



import requests
import pytest

def test_all_breeds_list_is_not_empty():
    response = requests.get("https://dog.ceo/api/breeds/list/all")
    data = response.json()
    assert len(data["message"]) > 0


import requests
import pytest

def test_random_image_status_code_equals_200():
    response = requests.get("https://dog.ceo/api/breed/husky/images/random")
    data = response.json()
    assert data["status"] == "success"




import requests
import pytest

def test_breed_images_are_not_empty():
    response = requests.get("https://dog.ceo/api/breed/husky/images")
    data = response.json()
    assert len(data["message"]) > 0




import requests
import pytest

def test_random_image_status_code_equals_200_for_breed():
    response = requests.get("https://dog.ceo/api/breed/husky/images/random")
    assert response.status_code == 200




import requests
import pytest

def test_random_image_status_code_equals_200_for_all_breeds():
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    assert response.status_code == 200




import requests
import pytest

@pytest.mark.parametrize("size", ["small", "thumb", "medium", "large"])
def test_random_image_by_size(size):
    response = requests.get(f"https://dog.ceo/api/breed/husky/images/random/{size}")
    assert response.status_code == 200




import requests
import pytest

def test_sub_breeds_for_breed():
    response = requests.get("https://dog.ceo/api/breed/husky/list")
    data = response.json()
    assert len(data["message"]) > 0