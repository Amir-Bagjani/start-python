from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
import threading

WEBSITES = [
    "https://example.com",
    "https://httpbin.org",
    "https://www.python.org",
    "https://github.com",
    "https://stackoverflow.com",
    "https://news.ycombinator.com",
    "https://www.wikipedia.org",
    "https://www.reddit.com",
    "https://www.bbc.com",
    "https://www.nytimes.com",
    "https://www.cnn.com",
    "https://www.mozilla.org",
    "https://www.apple.com",
    "https://www.microsoft.com",
    "https://www.amazon.com",
    "https://www.ebay.com",
    "https://www.linkedin.com",
    "https://x.com",
    "https://www.instagram.com",
    "https://www.youtube.com",
]
session = requests.Session()
session.headers.update(
    {
        "User-Agent": (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/138.0.0.0 Safari/537.36"
        ),
        "Accept": (
            "text/html,application/xhtml+xml,application/xml;q=0.9,"
            "image/avif,image/webp,*/*;q=0.8"
        ),
        "Accept-Language": "en-US,en;q=0.9",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
    }
)


def check_site_availabilty(url):
    try:
        res = session.get(url, timeout=10)
        return {"url": url, "availability": res.status_code == 200}
    except requests.exceptions.RequestException as e:
        return {"url": url, "availability": False}


def main():
    # with ThreadPoolExecutor(max_workers=5) as executor:
    #     for res in executor.map(check_site_availabilty, WEBSITES):
    #         print(res)

    with ThreadPoolExecutor(max_workers=50) as executor:
        futures = [executor.submit(check_site_availabilty, url) for url in WEBSITES]
        for future in as_completed(futures):
            print(future.result())


if __name__ == "__main__":
    main()
