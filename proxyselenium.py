from http_request_randomizer.requests.proxy.requestProxy import RequestProxy
req_proxy = RequestProxy() #you may get different number of proxy when  you run this at each time
proxies = req_proxy.get_proxy_list() #this will create proxy list
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from ipshuffleselenium import get_proxies
from itertools import cycle

from selenium import webdriver

proxies = get_proxies()
proxy_pool = cycle(proxies)


def get_proxy():
    return next(proxy_pool)


PROXY = get_proxy()
webdriver.DesiredCapabilities.CHROME['proxy'] = {
    "httpProxy": PROXY,
    "ftpProxy": PROXY,
    "sslProxy": PROXY,

    "proxyType": "MANUAL",

}
driver = webdriver.Chrome()
driver.get('https://www.google.com/search?source=hp&ei=qNEdXrTwLKzDlwS-yYmoDw&q=what+is+my+ip&oq=what+is+my+ip&gs_l=psy-ab.3..0l10.688.2639..2928...0.0..0.181.2298.0j13......0....1..gws-wiz.......0i131.GntNYHwoCt8&ved=0ahUKEwi05JODqIPnAhWs4YUKHb5kAvUQ4dUDCAY&uact=5')
setattr(driver.desired_capabilities.proxy, get_proxy())
driver.get('https://www.google.com/search?source=hp&ei=qNEdXrTwLKzDlwS-yYmoDw&q=what+is+my+ip&oq=what+is+my+ip&gs_l=psy-ab.3..0l10.688.2639..2928...0.0..0.181.2298.0j13......0....1..gws-wiz.......0i131.GntNYHwoCt8&ved=0ahUKEwi05JODqIPnAhWs4YUKHb5kAvUQ4dUDCAY&uact=5')
driver.close()

ind = [] #int is list of Indian proxy
for proxy in proxies:
    if proxy.country == 'India':
        ind.append(proxy)