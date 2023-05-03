import pytest
import requests

pytest --url=https://example.com
def pytest_addoption(parser):
    parser.addoption('--url', default='https://ya.ru', help='URL to test')


@pytest.fixture
def url(request):
    return request.config.getoption('--url')
def pytest_addoption(parser):
    parser.addoption('--url', default='https://ya.ru', help='URL to test')
    parser.addoption('--status_code', default=200, help='Expected HTTP status code')


@pytest.fixture
def url(request):
    return request.config.getoption('--url')


@pytest.fixture
def status_code(request):
    return int(request.config.getoption('--status_code'))






def test_url_status_code(url, status_code):
    resp = requests.get(url)
    assert resp.status_code == status_code
