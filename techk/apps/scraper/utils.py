from bs4 import BeautifulSoup
import requests
import re

URL_BASE = 'http://books.toscrape.com/'

def book_info(book):
    req = requests.get(book['url'])
    soup = BeautifulSoup(req.text,'lxml')

    breadcrumb = soup.find('ul',{'class': 'breadcrumb'})
    category = breadcrumb.findAll('li')[2].a.text
    article = soup.find('article',{'class': 'product_page'})
    title =  article.find('h1').text
    price_string = article.find('p',{'class': 'price_color'}).text
    price = price_string[2:]
    stock_string = article.find('p',{'class': 'instock availability'}).text
    stock =  int((re.findall('\d+',stock_string))[0])
    desc = article.find('p',{'class':None})
    description = desc.text if desc else None
    table = article.find('table',{'class': 'table table-striped'})
    upc = table.find('td').text

    body = {'category':category,'title':title,'price':price,'stock':stock,'product_description':description,'upc':upc}
    return body

def page_books(page):
    req = requests.get(page)
    soup = BeautifulSoup(req.text, "lxml")
    articles = soup.findAll("article", {"class": "product_pod"})
    data = []

    for art in articles:
        link = art.a['href']
        link_format = URL_BASE + 'catalogue/' + link
        title = art.h3.a['title']
        data.append({'url': link_format,'title': title})
    return data

def pages_t():
    count = 1
    req = requests.get(URL_BASE)
    soup = BeautifulSoup(req.text, "lxml")
    current = soup.find("li", {'class': 'current'}).text
    total = int((re.findall('\d+', current))[1])
    data = []
    while count <= total:
        data.append(URL_BASE + f"catalogue/page-{count}.html")
        count += 2
        break
    return data

def categories():
    req = requests.get(URL_BASE)
    soup = BeautifulSoup(req.text, "lxml")
    categories = soup.find("div", {"class": "side_categories"})
    list = categories.findAll('li')
    data = []
    for val in list:
        if (val.a.text):
            text = val.a.text.strip()
            data.append(text)
    return data
