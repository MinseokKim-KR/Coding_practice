# # import requests
# # from bs4 import BeautifulSoup
# #
# # url = 'https://mirrorprotocol.app/#/trade'
# #
# # response = requests.get(url)
# # print("Response : ", response)
# # if response.status_code == 200:
# #     html = response.text
# #     print("html")
# #     print(html)
# #     soup = BeautifulSoup(html, 'html.parser')
# #     title = soup.select_one('#s_content > div.section > ul > li:nth-child(1) > dl > dt > a')
# #     print(title)
# # else :
# #     print(response.status_code)
# """
# # import requests  # 웹 페이지의 HTML을 가져오는 모듈
# # from bs4 import BeautifulSoup  # HTML을 파싱하는 모듈
# #
# # # 웹 페이지를 가져온 뒤 BeautifulSoup 객체로 만듦
# # response = requests.get('https://mirrorprotocol.app/#/trade')
# # soup = BeautifulSoup(response.content, 'html.parser')
# #
# # table = soup.find('div', {'class': "Table_wrapper__zaoYv Table_radius__xySlm"})  # <table class="table_develop3">을 찾음
# # # table = soup.find('table')  # <table class="table_develop3">을 찾음
# # print(table)
# # data = []  # 데이터를 저장할 리스트 생성
# # for tr in table.find_all('tr'):  # 모든 <tr> 태그를 찾아서 반복(각 지점의 데이터를 가져옴)
# #     tds = list(tr.find_all('td'))  # 모든 <td> 태그를 찾아서 리스트로 만듦
# #     # (각 날씨 값을 리스트로 만듦)
# #     for td in tds:  # <td> 태그 리스트 반복(각 날씨 값을 가져옴)
# #         if td.find('a'):  # <td> 안에 <a> 태그가 있으면(지점인지 확인)
# #             point = td.find('a').text  # <a> 태그 안에서 지점을 가져옴
# #             temperature = tds[5].text  # <td> 태그 리스트의 여섯 번째(인덱스 5)에서 기온을 가져옴
# #             humidity = tds[9].text  # <td> 태그 리스트의 열 번째(인덱스 9)에서 습도를 가져옴
# #             data.append([point, temperature, humidity])  # data 리스트에 지점, 기온, 습도를 추가
# #
# # print(data)  # data 표시. 주피터 노트북에서는 print를 사용하지 않아도 변수의 값이 표시됨
# """
#
# from selenium import webdriver
# from bs4 import BeautifulSoup
# import time
# import pandas as pd
# import os
# ## Chrome의 경우 | 아까 받은 chromedriver의 위치를 지정해준다.
# driver = webdriver.Chrome('./chromedriver')
# driver.get('https://mirrorprotocol.app/#/trade')
#
#
# ## url에 접근한다.
# time.sleep(6)
# soup = BeautifulSoup(driver.page_source, 'html.parser')
#
# stocks = soup.select('#mirror > div > div.Container_container__lHqDY > article > div > table > tbody > tr')
# index = []
# premium = []
# for stock in stocks[1:]:
#     name = stock.select_one('td:nth-child(1) > article > header > h1').text
#     price = stock.select_one('td:nth-child(4) > span').text
#     # row = {
#     #     'name': name,
#     #     'Primeum': price
#     # }
#     # print(name, price)
#     index.append(name)
#     premium.append(price)
#
#
# df = pd.DataFrame(data=premium, columns=index)
#
# # .to_csv
# # 최초 생성 이후 mode는 append
# if not os.path.exists('output.csv'):
#     df.to_csv('output.csv', index=False, mode='w', encoding='utf-8-sig')
# else:
#     df.to_csv('output.csv', index=False, mode='a', encoding='utf-8-sig', header=False)
#
# # from selenium import webdriver
# # from bs4 import BeautifulSoup
# #
# #
# # driver = webdriver.Chrome()
# # url = 'https://finance.naver.com/sise/sise_market_sum.nhn'
# # driver.get(url)
# #
# # soup = BeautifulSoup(driver.page_source, 'html.parser')
# #
# # stocks = soup.select('#contentarea > div.box_type_l > table.type_2 > tbody > tr')
# # print(stocks)


from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd
import os
import datetime

driver = webdriver.Chrome('./chromedriver')
driver.get('https://mirrorprotocol.app/#/trade')
time.sleep(6)

while 1:
    soup = BeautifulSoup(driver.page_source, 'html.parser')
    stocks = soup.select('#mirror > div > div.Container_container__lHqDY > article > div > table > tbody > tr')
    Time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('Now Time : ', Time)
    index = ['time']
    premium = [Time]
    for stock in stocks[1:]:
        name = stock.select_one('td:nth-child(1) > article > header > h1').text
        price = float(stock.select_one('td:nth-child(4) > span').text.replace('%',''))
        index.append(name)
        premium.append(price)
    df = pd.DataFrame(data=premium, index=index)
    df = df.transpose()
    if not os.path.exists('output.csv'):
        df.to_csv('output.csv', index=False, mode='w', encoding='utf-8-sig')
    else:
        df.to_csv('output.csv', index=False, mode='a', encoding='utf-8-sig', header=False)
    driver.refresh()
    time.sleep(60)