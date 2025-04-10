import httpx
from tenacity import retry, stop_after_attempt, wait_random

DEFAULT_HEADER = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/122.0.0.0 Safari/537.36"
    ),
    "Accept-Language": "en,gb-en,es-ES,es;q=0.9",
    "Accept": (
        "text/html,application/xhtml+xml,application/xml;q=0.9,"
        "image/avif,image/webp,*/*;q=0.8"
    )
}


@retry(wait=wait_random(1, 2), stop=stop_after_attempt(3))
def fetch_html(url: str, header: dict = None):
    header = header or DEFAULT_HEADER
    with httpx.Client(timeout=10) as client:
        response = client.get(url, headers=header)
        response.raise_for_status()
        return response.text