import threading
import sys
import time
import urllib.request

urls = [
    'https://www.yandex.ru', 'https://www.google.com',
    'https://habrahabr.ru', 'https://www.python.org',
    'https://isocpp.org',
]


def read_url(url):
    with urllib.request.urlopen(url) as u:
        return u.read()


def run_threads(count):
    threads = [
        threading.Thread(target=read_url, args=(i,))
        for i in urls
    ]
    for thread in threads:
        thread.start()


start = time.time()
run_threads(urls)
print(time.time() - start)