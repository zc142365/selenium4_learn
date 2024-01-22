import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

opts = Options()
opts._binary_location = "./chrome.exe"

svc = Service(executable_path="./chromedriver.exe")

driver = webdriver.Chrome(service=svc, options=opts)
URL = 'https://www.dell.com/support/home/ko-kr'
driver.get(URL)

time.sleep(5)
driver.quit()
