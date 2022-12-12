import threading
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import time


class Worker:
    base_url = ''
    queue = []
    crawled = set()
    lock = threading.Semaphore(value=1)

    def __init__(self, base_url):
        self.base_url = base_url
        self.queue = [base_url]

    @staticmethod
    def write_file(path, data):
        with open(path, 'a') as f:
            f.write(data)
            f.close()

    def report(self, url):
        with self.lock:
            print("Successfully crawled", url)

    def crawl(self, link):
        try:
            page = requests.get(link)
            soup = BeautifulSoup(page.text, 'lxml')

            self.write_file("dump.txt", soup.text)
            self.write_file("log.txt", link + "\n")
            self.report(link)
            self.crawled.add(link)

            for upper_domain in soup.find_all('a', href=True):
                joined_link = urljoin(self.base_url, upper_domain['href'])
                if joined_link not in self.crawled:
                    self.queue.append(joined_link)

            time.sleep(1)  # pause the worker thread for 1 second

        except:
            self.write_file("error_log.txt", str(link) + "\n")
            pass
