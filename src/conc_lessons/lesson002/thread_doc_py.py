from concurrent.futures import ThreadPoolExecutor, as_completed, Future
from urllib import request
import os

os.system('cls')

URLS = ['http://www.foxnews.com/',
        'http://www.cnn.com/',
        'http://europe.wsj.com/',
        'http://www.bbc.co.uk/',
        'http://nonexistent-subdomain.python.org/']

def load_url(url, timeout):
    with request.urlopen(url, timeout=timeout) as conn:
        return conn.read()

with ThreadPoolExecutor(max_workers=5) as executor:
    future_to_url: dict[Future, str] = {}
    
    for url in URLS:
        t1 = executor.submit(load_url, url, 60)
        future_to_url[t1] = url

    for future in as_completed(future_to_url):
        url = future_to_url[future]
        try:
            data = future.result()
        except Exception as exc:
            print(f'{url} generated an exception: {exc}')
        else:
            print(f'{url} page is {len(data)} bytes')