from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import openpyxl
import urllib
import requests

f = open('united.txt', 'r')
lines = f.readlines()

wb = openpyxl.Workbook()
sheet = wb.active
sheet.append(["영화명", "관객수(한국)","평점(한국)","주연 배우"])

for line in lines:
    url = 'https://movie.daum.net/main'
    driver = webdriver.Chrome('/Users/hee/Downloads/chromedriver')
    driver.get(url)
    time.sleep(2)
    
    left_idx = line.find('(')
    movie_title = line[:left_idx]
    movie_year = line[left_idx + 1 : -2]
    
    search_box = driver.find_element(By.CSS_SELECTOR, 'input.tf_keyword')
    search_box.send_keys(movie_title)
    search_box.send_keys(Keys.RETURN)
    time.sleep(2)
    

    try:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        content = soup.find('ul', 'list_searchresult')
        div_list = content.find_all('div', 'item_related')
        for i in range(0, len(div_list)):
            m_year = div_list[i].find('dl', 'desc_info').text[-5 : -1]
            if m_year == movie_year:
                tit_item = div_list[i].find('strong', 'tit_item')
                a_item = tit_item.select("a.link_tit")
                href = a_item[0].attrs['href']
                m_url = 'https://movie.daum.net' + href
                request = requests.get(m_url)
                html = request.text
                soup2 = BeautifulSoup(html, 'html.parser')
                detail_cont = soup2.find('div', 'detail_cont')
                inner_cont = detail_cont.find_all('div', 'inner_cont')[1]
                people_cont=inner_cont.find_all('dl','list_cont')[1].text
                score_cont=inner_cont.find_all('dl','list_cont')[0].text
                start_sidx=score_cont.find('점')
                start_pidx=people_cont.find('객')
                end_pidx=people_cont.find('명')
                #mainContent > div > div.box_detailinfo > div.contents > div:nth-child(3) > ul > li:nth-child(1) > div > div > span.subtit_item
                ##mainContent > div > div.box_detailinfo > div.contents > div:nth-child(3) > ul > li:nth-child(4) > div > div > span.subtit_item
                li = soup2.find_all('li', {'role' : 'presentation'})[1]
                a_item=li.select("a.link_tabmenu")
                a_url = 'https://movie.daum.net' + a_item[0].attrs['href']
                driver1 = webdriver.Chrome('/Users/hee/Downloads/chromedriver')
                driver1.get(a_url)
                actor = driver1.find_elements(By.XPATH, '//*[@id="mainContent"]/div/div[2]/div[2]/div[2]/ul')
                actor_list=actor[0].text.encode('utf-8').decode('ascii','ignore')
                actor_list=actor_list.replace('\n','')
                actor_list=actor_list.strip()
                print(movie_title,people_cont[start_pidx+1:end_pidx],score_cont[start_sidx+1:],actor_list)

                sheet.append([movie_title + '(' + movie_year + ')',people_cont[start_pidx+1:end_pidx],score_cont[start_sidx+1:],actor_list])
                '''if len(inner_cont) > 10:
                    start_idx = inner_cont.find('점')
                    last_idx = inner_cont.find('명')
                    print(movie_title, inner_cont[start_idx + 1 : last_idx])
                    sheet.append([movie_title + '(' + movie_year + ')', inner_cont[start_idx + 1 : last_idx]])
                    break;
                    '''
    except: continue

wb.save("korea_open_movie_list(US)_indirect.xlsx")
f.close()
