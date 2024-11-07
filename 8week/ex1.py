from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

url = 'https://www.google.co.kr/'
driver = webdriver.Chrome()
driver.get(url)
time.sleep(3)

search_box = driver.find_element(By.CSS_SELECTOR, '#APjFqb')
search_box.send_keys("KBO 한국시리즈")
search_box.send_keys(Keys.RETURN)
time.sleep(20)

## web Crawling
## 웹 브라우저를 통해 데이터를 접근, 가져오는 기술
## 1.수동 조작 => 작동 시나리오
## 2. selenium 사용 => 작동  
##               자동화 
## 1 - 데이터 사이트 접속(webdriver.브라우저), 접근
## 2- 엘리먼트 찾기(CSS selector(개발자 도구)를 사용해서 복사) 
## 3- 마우스(element.click) , 키 입력(element.send_keys) 
## 3. 데이터 크롤링 <div name='ABC'>Hello<div> 
##                get attirbute("name") e.text()