from datetime import time

from selenium import webdriver

wd = webdriver.chrome('D:\\bit\\pycahrm\\chromedriver.exe')
wd.get('http://www.google.com')

time.sleep(2)
html = wd.page_source
print(html)
wd.quit