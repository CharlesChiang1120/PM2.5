import requests
import os
import time
import ssl
import datetime
import json
from bs4 import BeautifulSoup


# used to fix Python SSL CERTIFICATE_VERIFY_FAILED
if (not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context
####################################

def main():

    starttime = datetime.datetime.now()

    print('\033[32m熱門景點')
    print('')
    scenery()
    time.sleep(5)

    print('\033[36m住宿地點')
    print('')
    accommodation()
    time.sleep(5)

    print('\033[35m美食搜尋')
    print('')
    restaurant()
    time.sleep(5)

    print('\033[32m熱門景點')
    print('')
    scenery_dict()
    print('')
    time.sleep(5)

    print('\033[36m住宿地點')
    print('')
    accomodation_dict()
    print('')
    time.sleep(5)

    print('\033[35m美食搜尋')
    print('')
    restaurant_dict()
    print('')
    endtime = datetime.datetime.now()
    print(endtime - starttime)

def scenery():#列出景點名稱跟網址

    resource_path = r'./scenery'
    if not os.path.exists(resource_path):
        os.mkdir(resource_path)

    page = 1

    while page < 21:

        Taoyuan_scenery_URL = 'https://travel.tycg.gov.tw/zh-tw/travel?sortby=Hits&page=%s'%page
        res = requests.get(url=Taoyuan_scenery_URL)

        try:

            if res:
                soup = BeautifulSoup(res.text,'html.parser')
                Basic_content = soup.findAll('div',class_="info-card-item")

                for _ in Basic_content:

                    if 'h3':
                        scenery_title = _.h3.text

                    if 'href':
                        scenery_url = 'https://travel.tycg.gov.tw' + _.a['href']

                    if 'p':
                        scenery_info = _.p.text

                        print('景點名稱:',scenery_title)
                        print('景點網址:',scenery_url)
                        print('')

                    with open(r'%s/%s.txt' % (resource_path, scenery_title), 'w', encoding='utf-8') as w:
                        w.write(scenery_info)

        except Exception:
            return None

        page +=1

        time.sleep(1)

def accommodation():#列出住宿地點跟網址

    resource_path = r'./accommodation'
    if not os.path.exists(resource_path):
        os.mkdir(resource_path)

    page = 1

    while page < 24:

        Taoyuan_accommodation_URL = 'https://travel.tycg.gov.tw/zh-tw/accommodation?sortby=Hits&page=%s' % page
        res = requests.get(url=Taoyuan_accommodation_URL)

        try:

            if res:
                soup = BeautifulSoup(res.text, 'html.parser')
                accommodation_content = soup.findAll('div', class_="info-card-item")

                for _ in accommodation_content:

                    if 'h3':
                        accommodation_title = _.h3.text

                    if 'href':
                        accommodation_url = 'https://travel.tycg.gov.tw' + _.a['href']

                    if 'p':
                        accommodation_info = _.p.text

                        print('飯店名稱:', accommodation_title)
                        print('飯店網址:', accommodation_url)
                        print('')

                    with open(r'%s/%s.txt' % (resource_path, accommodation_title), 'w', encoding='utf-8') as w:
                        w.write(accommodation_info)

        except Exception:
            return None

        page += 1

        time.sleep(1)



def restaurant():#列出餐廳地點跟網址

    resource_path = r'./food'
    if not os.path.exists(resource_path):
        os.mkdir(resource_path)

    page = 1

    while page < 50:

        Taoyuan_restaurant_URL = 'https://travel.tycg.gov.tw/zh-tw/consume?sortby=Hits&page=%s'%page
        res = requests.get(url=Taoyuan_restaurant_URL)

        try:

            if res:
                soup = BeautifulSoup(res.text,'html.parser')
                Basic_content = soup.findAll('div',class_="info-card-item")

                for _ in Basic_content:

                    if 'h3':
                        restaurant_title = _.h3.text

                    if 'href':
                        restaurant_url = 'https://travel.tycg.gov.tw' + _.a['href']

                    if 'p':
                        restaurant_info = _.p.text

                        print('餐廳名稱:',restaurant_title)
                        print('餐廳網址:',restaurant_url)
                        print('')

                    with open(r'%s/%s.txt' % (resource_path, restaurant_title), 'w', encoding='utf-8') as w:
                        w.write(restaurant_info)

        except Exception:
            return None

        page +=1

        time.sleep(1)

def scenery_dict():#將桃園觀光網站的景點資訊變成字典

    page = 1
    sceneries = []

    while page < 21:

        Taoyuan_scenery_URL = 'https://travel.tycg.gov.tw/zh-tw/travel?sortby=Hits&page=%s' % page
        res = requests.get(url=Taoyuan_scenery_URL)

        try:

            if res:
                soup = BeautifulSoup(res.text, 'html.parser')
                info = soup.findAll('div', class_='info-blk')

                for i in info:

                    scenery = dict()

                    scenery['Title'] = [s for s in i.stripped_strings][0]#景點的名稱
                    scenery['Time'] = [s for s in i.stripped_strings][1]#景點的開放時間

                    try:
                        if 'p':#景點的郵遞區號
                            scenery['zip'] = [s for s in i.find('p', 'icon-location').stripped_strings][0][0:3]
                    except Exception:
                        scenery['zip'] = 'None'

                    try:
                        if 'p':#景點的地址
                            scenery['address'] = [s for s in i.find('p', 'icon-location').stripped_strings][0][4:]
                    except Exception:
                        scenery['address'] = 'None'

                    try:
                        if 'span':#景點的評論
                            scenery['Comment'] = [s for s in i.find('span', 'icon-review').stripped_strings][0]
                    except Exception:
                        scenery['Comment'] = 'None'

                    try:
                        if 'span':#景點的瀏覽人次
                            scenery['Browse'] = [s for s in i.find('span', 'icon-view').stripped_strings][0] + '人次'
                    except Exception:
                        scenery['Browse'] = 'None'

                    print(scenery)

                    sceneries.append(scenery)

        except Exception:
            return None

        with open('scenery.json', 'w', encoding='utf-8') as f:
            json.dump(sceneries, f, indent=2, sort_keys=False, ensure_ascii=False)

        page += 1

        time.sleep(1)


def accomodation_dict():#將桃園觀光網站的住宿資訊變成字典

    page = 1
    accomodations = []

    while page < 24:

        Taoyuan_accommodation_URL = 'https://travel.tycg.gov.tw/zh-tw/accommodation?sortby=Hits&page=%s' % page
        res = requests.get(url=Taoyuan_accommodation_URL)

        try:

            if res:
                soup = BeautifulSoup(res.text, 'html.parser')
                info = soup.findAll('div', class_='info-blk')

                for i in info:

                    accomodation = dict()

                    accomodation['Title'] = [s for s in i.stripped_strings][0]
                    accomodation['Time'] = [s for s in i.stripped_strings][1]

                    try:
                        if 'p':
                            accomodation['zip'] = [s for s in i.find('p', 'icon-location').stripped_strings][0][0:3]
                    except Exception:
                        accomodation['zip'] = 'None'

                    try:
                        if 'p':
                            accomodation['address'] = [s for s in i.find('p', 'icon-location').stripped_strings][0][4:]
                    except Exception:
                        accomodation['address'] = 'None'

                    try:
                        if 'span':
                            accomodation['Comment'] = [s for s in i.find('span', 'icon-review').stripped_strings][0]
                    except Exception:
                        accomodation['Comment'] = 'None'

                    try:
                        if 'span':
                            accomodation['Browse'] = [s for s in i.find('span', 'icon-view').stripped_strings][0] + '人次'
                    except Exception:
                        accomodation['Browse'] = 'None'

                    print(accomodation)

                    accomodations.append(accomodation)

        except Exception:
            return None

        with open('accomodation.json', 'w', encoding='utf-8') as f:
            json.dump(accomodations, f, indent=2, sort_keys=False, ensure_ascii=False)

        page += 1

        time.sleep(1)


def restaurant_dict():#將桃園觀光網站的餐廳資訊變成字典

    page = 1
    restaurants = []

    while page < 50:

        Taoyuan_restaurant_URL = 'https://travel.tycg.gov.tw/zh-tw/consume?sortby=Hits&page=%s'%page
        res = requests.get(url=Taoyuan_restaurant_URL)

        try:

            if res:

                soup = BeautifulSoup(res.text, 'html.parser')
                info = soup.findAll('div', class_='info-blk')

                for i in info:

                    restaurant = dict()

                    restaurant['Title'] = [s for s in i.stripped_strings][0]
                    restaurant['Time'] = [s for s in i.stripped_strings][1]


                    try:
                        if 'p':
                            restaurant['zip'] = [s for s in i.find('p', 'icon-location').stripped_strings][0][0:3]
                    except Exception:
                        restaurant['zip'] = 'None'

                    try:
                        if 'p':
                            restaurant['address'] = [s for s in i.find('p', 'icon-location').stripped_strings][0][4:]
                    except Exception:
                        restaurant['address'] = 'None'

                    try:
                        if 'span':
                            restaurant['Comment'] = [s for s in i.find('span', 'icon-review').stripped_strings][0]
                    except Exception:
                        restaurant['Comment'] = 'None'

                    try:
                        if 'span':
                            restaurant['Browse'] = [s for s in i.find('span', 'icon-view').stripped_strings][0] + '人次'
                    except Exception:
                        restaurant['Browse'] = 'None'

                    print(restaurant)

                    restaurants.append(restaurant)

        except Exception:
            return None

        with open('restaurant.json', 'w', encoding='utf-8') as f:
            json.dump(restaurants, f, indent=2, sort_keys=False, ensure_ascii=False)

        page += 1

        time.sleep(1)



if __name__ == '__main__':
    main()