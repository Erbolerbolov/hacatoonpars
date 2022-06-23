# from itertools import product
# from urllib import response
# import requests
# from bs4 import BeautifulSoup
# import csv

# from main import get_html

# url = 'https://kg.wildberries.ru/catalog/obuv/detskaya/dlya-malchikov'

# def html(url):
#     response = requests.get(url)
#     return response.text

# def get_soup(html):
#     soup = BeautifulSoup(html,"lxml")
#     return soup

# def get_last_page_number(soup):
#     pagination_list = soup.find("div", class_="pageToInsert").find_all("a")
#     item = pagination_list[-2]
#     # last = item.find("a")
#     return int(item.text)

# def get_product_cards(soup):
#     product_list = soup.find("a", class_="product-card__main")
#     products = product_list.find_all("div", class_="product-card")
#     return products

# def get_data_from_card(products):
#     for product in products:
#         try:
#             title = product.find("strong", class_="brand-name").text
#             print(title)
#         except:
#             title = " "
#         try:
#             price = product.find("ins", class_="lower-price")
#             print(price)
#         except:
#             price = " "
#         try:
#             image = product.find("div").find("img").get("src")
#         except:
#             image = " "
#         data ={"title": title, "price": price, "image": image}
#         write_to_csv(data)
# def write_to_csv(data):
#     with open("obuv.csv", "a") as file:
#         write = csv.writer(file)
#         write.writerow((data["title"], data["price"], data["image"]))

# def main():
#     html = get_html(url)
#     soup = get_soup(html)
#     last_page_num = get_last_page_number(soup)
#     for page in range(1,last_page_num+1):
#         page_url = url + "&page=" + str(page)
#         html = get_html(page_url)
#         soup = get_soup(html)
#         cards = get_product_cards (soup)
#         get_data_from_card(cards)
# main()

# html = get_html(url)
# soup = get_soup(html)
# products = get_product_cards(soup)
# get_data_from_card(products)
    
