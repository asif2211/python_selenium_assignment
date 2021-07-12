import scrapy
import random
import requests
from itertools import cycle
from bs4 import BeautifulSoup
from selenium import webdriver
from scrapy.crawler import CrawlerProcess
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC


def get_proxies():
    response = requests.get("https://3337x.com")
    soup = BeautifulSoup(response.text,"lxml")
    proxies = [':'.join([item.select_one("td").text,item.select_one("td:nth-of-type(2)").text]) for item in soup.select("table.table tr") if "yes" in item.text]
    return proxies


def get_random_proxy(proxy_vault):
    while proxy_vault:
        random.shuffle(proxy_vault)
        proxy_url = proxy_vault.pop()
        proxy_dict = {
            'http': proxy_url,
            'https': proxy_url
        }
        try:
            res = requests.get("http://3337x.com", proxies=proxy_dict, timeout=10)
            res.raise_for_status()
            return proxy_url
        except Exception:
            continue


def start_script():
    proxy = get_proxies()
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument(f'--proxy-server={get_random_proxy(proxy)}')
    driver = webdriver.Chrome(options=chrome_options)
    return driver


class StackBotSpider(scrapy.Spider):
    name = "stackoverflow"

    start_urls = [
        'https://3337x.com'
    ]

    def __init__(self):
        self.driver = start_script()
        self.wait = WebDriverWait(self.driver, 10)

    def parse(self,response):
        self.driver.get(response.url)
        for elem in self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".summary .question-hyperlink"))):
            yield scrapy.Request(elem.get_attribute("href"),callback=self.parse_details)

    def parse_details(self,response):
        self.driver.get(response.url)
        for elem in self.wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "h1[itemprop='name'] > a"))):
            yield {"post_title":elem.text}


c = CrawlerProcess({
    'USER_AGENT': 'Mozilla/5.0',
})
c.crawl(StackBotSpider)
c.start()
