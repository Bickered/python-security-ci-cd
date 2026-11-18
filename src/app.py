import requests
import urllib3

def get_status_code(url: str) -> int:
    """Fetch a URL and return the HTTP status code."""
    response = requests.get(url, timeout=10)
    return response.status_code

def get_with_urllib3(url: str) -> int:
    """Alternative using urllib3 directly."""
    http = urllib3.PoolManager()
    response = http.request("GET", url)
    return response.status