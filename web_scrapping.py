import requests
from bs4 import BeautifulSoup
import pandas as pd


URL = "https://books.toscrape.com/"
page = requests.get(URL)


soup = BeautifulSoup(page.content, "html.parser")
print(soup.prettify())


rows = soup.find_all('ol', class_ = 'row')
books = soup.find_all('li', class_ = 'col-xs-6 col-sm-4 col-md-3 col-lg-3')
articles = soup.find_all('article', class_ = 'product_pod')
images = soup.find_all('div', class_ = 'image_container')
rating_three = soup.find_all('p', class_ = 'star-rating Three')


titles = []
prices = []
in_stock = []
star_rating = []

for book in books:
    # print(book)
    title = book.h3.a['title']
    price = book.find('p', class_ = 'price_color').contents[0]

    if book.find('p', class_ = 'star-rating One'):
        star_rating.append(1)
    elif book.find('p', class_ = 'star-rating Two'):
        star_rating.append(2)
    elif book.find('p', class_ = 'star-rating Three'):
        star_rating.append(3)
    elif book.find('p', class_ = 'star-rating Four'):
        star_rating.append(4)
    elif book.find('p', class_ = 'star-rating Five'):
        star_rating.append(5)

    if book.find('p', "instock availability"):
        is_in_stock = True
        if is_in_stock:
            in_stock.append(is_in_stock)
        else:
            in_stock.append(False)

    titles.append(title)
    prices.append(price)


df = pd.DataFrame({'title': titles, 'price': prices, 'in_stock': in_stock, 'star_rating': star_rating})
print(df)