import pytest
from src.app import get_status_code, get_with_urllib3

def test_requests_status():
    status = get_status_code("https://httpbin.org/status/200")
    assert status == 200

def test_urllib3_status():
    status = get_with_urllib3("https://httpbin.org/status/200")
    assert status == 200

def test_requests_404():
    status = get_status_code("https://httpbin.org/status/404")
    assert status == 404