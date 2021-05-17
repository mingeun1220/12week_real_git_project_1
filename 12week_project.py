import time
from selenium import webdriver
import numpy as np

word=input("찾고 싶은 단어를 입력하시오 : ")

URL = 'https://dict.naver.com/'
driver = webdriver.Chrome(executable_path='./chromedriver.exe')
driver.get(url=URL)

search_box=driver.find_element_by_name("dicQuery")
search_box.send_keys(word)

search_btn=driver.find_element_by_class_name("btn_search")
search_btn.click()

dic = driver.find_element_by_class_name("search_result_area")

count = 0
counting = 0
for i in dic.find_elements_by_css_selector('div'):
    count += 1
    m = i.find_element_by_css_selector('h3')
    try:
        n = i.find_element_by_css_selector('ul')
    except:
        n = i.find_element_by_css_selector('dl')
    c = m.find_element_by_css_selector('span').text
    print(m.text)
    print(n.text)
    print("")

    if count == 3:
        break