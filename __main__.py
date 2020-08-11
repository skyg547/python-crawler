import time
from datetime import datetime
from itertools import count

from bs4 import BeautifulSoup
from selenium.webdriver.chrome import webdriver
from selenium import webdriver

from collection import crawler
import pandas as pd


def crawling_pelicana():
    results = []

    for page in count(start=1, step=1):
        url = 'https://pelicana.co.kr/store/stroe_search.html?page=%d&branch_name=&gu=&si=' %page
        html = crawler.crawling(url=url)
        # print(html)

        bs = BeautifulSoup(html, 'html.parser')
        tag_table = bs.find('table', attrs={'class': ['table', ' mt20']})
        tag_tbody = tag_table.find('tbody')
        tags_tr = tag_tbody.findAll('tr')

        # 끝 검출
        if len(tags_tr) == 0:
            break

        for tag_tr in tags_tr:

            strings = list(tag_tr.strings)
            name = strings[1]
            address = strings[3]
            sidogu = address.split()[0:2]

            t = (name, address) + tuple(sidogu)
            results.append(t)


    # store
    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gigun'])
    table.to_csv('results/pelicana.csv', encoding='utf-8', mode='w', index=True)
    print(results)


def crawing_goobne():
    results = []
    url = 'http://www.goobne.co.kr/store/search_store.jsp'

    # 첫 페이지 로딩
    wd = webdriver.Chrome('D:\\bit\\pycahrm\\chromedriver.exe')
    wd.get(url)
    time.sleep(3)

    for page in count(start=1, step=1):
        # 자바스크립트 실행
        script = 'store.getList(%d)' %page
        wd.execute_script(script)
        print(f'{datetime.now()} : success for request[{script}]')
        time.sleep(2)
        # 자바스크립트 실행결과 HTML(동적으로 렌더링 된 HTML) 가져오기
        html = wd.page_source
        print(html)

        # parsing with bs4
        bs = BeautifulSoup(html, 'html.parser')
        tag_tbody = bs.find('tbody', attrs=({'id':'store_list'}))
        tags_tr = tag_tbody.findAll('tr')

        if tags_tr[0].get('class') is None:
            break;

        for tag_tr in tags_tr:
            strings = list(tag_tr)
            name = strings[1]
            address = strings[6]
            sidogu = address.split()[0:2]

            t = (name,address) + tuple(sidogu)

            print(t)

        results.append(t)
    wd.quit()
    # store
    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gigun'])
    table.to_csv('results/goobne.csv', encoding='utf-8', mode='w', index=True)
    print(results)


def crawing_kyochon():

    results = []

    for sido1 in range(1, 17):
        for sido2 in count(start=1, step=1):

            url = 'http://www.kyochon.com/shop/domestic.asp?sido1=%d&sido2=%d&txtsearch=' % (sido1, sido2)

            html = crawler.crawling(url=url)

            if html is None:
                break
            # print(html)

            bs = BeautifulSoup(html, 'html.parser')
            tag_ul = bs.find('ul', attrs={'class': 'list'})
            tags_span = tag_ul.findAll('span', attrs={'class': 'store_item'})

            for tag_span in tags_span:
                strings = list(tag_span.strings)

                name = strings[1];
                address = strings[3].strip('\r\n\t')
                sidogu = address.split()[0:2]

                t = (name, address) + tuple(sidogu)
                # print(t)
                results.append(t)

    # store
    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gigun'])
    table.to_csv('results/kyochon.csv', encoding='utf-8', mode='w', index=True)
    print(results)


def crawing_nene():
    results = []

    for page in count(start=1, step=1):
        url = 'https://nenechicken.com/17_new/sub_shop01.asp?page=%d&ex_select=1&ex_select2=&IndexSword=&GUBUN=A' % page
        html = crawler.crawling(url=url)
        # print(html)

        bs = BeautifulSoup(html, 'html.parser')
        tag_div = bs.findAll('div')

        # 끝 검출
        if len(tags_tr) == 0:
            break

        for tag_tr in tags_tr:
            strings = list(tag_tr.strings)
            name = strings[1]
            address = strings[3]
            sidogu = address.split()[0:2]

            t = (name, address) + tuple(sidogu)
            results.append(t)

        # store
    table = pd.DataFrame(results, columns=['name', 'address', 'sido', 'gigun'])
    table.to_csv('results/pelicana.csv', encoding='utf-8', mode='w', index=True)
    print(results)


if __name__ == '__main__':
    # pelicana
    # crawling_pelicana()

    # nene
    # crawing_nene()

    # kyochon
    #crawing_kyochon()

    #goobne
    crawing_goobne()