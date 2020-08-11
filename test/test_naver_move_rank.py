from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from collection import crawler


def ex01():
    request = Request('https://movie.naver.com/movie/sdb/rank/rmovie.nhn')
    response = urlopen(request)
    html = response.read().decode('cp949')
    # print(html)

    bs = BeautifulSoup(html, 'html.parser')
    divs = bs.findAll('div', attrs={'class': 'tit3'})
    # print(divs)

    for index, div in enumerate(divs):
        print(index, div.a.text, div.a['href'], sep=':')


def proc_error(e):
    print('crawling error', e)


def proc_naver_rank(data):
    bs = BeautifulSoup(data, 'html.parser')
    divs = bs.findAll('div', attrs={'class': 'tit3'})

    for index, div in enumerate(divs):
        print(index, div.a.text, div.a['href'], sep=':')


def ex02():
    html = crawler.crawling(
        url='https://movie.naver.com/movie/sdb/rank/rmovie.nhn',
        encoding='cp949',
        error=proc_error,
        # proc1=proc_naver_rank
    )
    print(html)


if __name__ == '__main__':
    # ex01()
    ex02()
