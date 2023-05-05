import pytest
import requests


def test_url_status_code(url, status_code):
    resp = requests.get(url)
    assert resp.status_code == status_code