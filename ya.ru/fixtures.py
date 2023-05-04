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