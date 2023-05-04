mport pytest
import requests


def pytest_addoption(parser):
    parser.addoption('--url', default='https://ya.ru', help='URL to test')



def test_url_status_code(url, status_code):
    resp = requests.get(url)
    assert resp.status_code == status_code