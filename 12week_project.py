import matplotlib.pyplot as plt
import matplotlib
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

list_name = []
list_number = []
for i in dic.find_elements_by_css_selector('h3'):
    counting += 1
    category = i.text
    category = category.split(' ',1)[0]
    list_name.append(category)
    number= i.find_element_by_css_selector('span').text
    number = number.split(' / ')
    del number[0]
    number = ''.join(number)
    number = number.replace('건','')
    number = number.replace(',','')
    number = int(number)
    list_number.append(number)

    if counting == 3:
        break

matplotlib.rcParams["axes.unicode_minus"]=False
plt.rc('font', family='Malgun Gothic')

x = np.arange(len(list_name))
y = list_number
plt.bar(x, y, color="red")
plt.xticks(x, list_name)
plt.title('사전 검색 기록')
plt.xlabel('사전 종류')
plt.ylabel('검색 건 수')
plt.grid(True)
plt.show()