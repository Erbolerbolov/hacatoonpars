from itertools import product
from ssl import get_protocol_name
from urllib import response
import requests
from bs4 import BeautifulSoup
import csv

url = "https://systema.kg/85-cofe"

def get_html(url):
    response = requests.get(url)
    return response.text

def get_soup(html):
    soup = BeautifulSoup(html, "lxml")
    return soup

def get_last_page_number(soup):
    pagination_list = soup.find("ul", class_="page-list").find_all("li")
    item = pagination_list[-2]
    last = item.find("a").text.strip()
    return int(last)

def get_product_cards(soup):
    product_list = soup.find("div", class_="products")
    products = product_list.find_all("div", class_="js-product")
    return products 
    

def get_data_from_card(products):
    for product in products:
        try:
            title = product.find("h2").text
        except:
            title = " "
        try:
            price = product.find("div", class_="product-price-and-shipping").text.strip()
            print(price)
        except:
            price = " "
        try:
            image = product.find("a").find("img").get("src")
        except:
            image = " "
        
        data = {"title": title, "price": price, "image": image}
        write_to_csv(data)
        
    
def write_to_csv(data):
    with open("coffee.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow((data["title"], data["price"], data["image"]))

def main():
    html = get_html(url)
    soup = get_soup(html)
    last_page_num = get_last_page_number(soup)
    for page in range(1,last_page_num+1):
        page_url = url + "?page=" + str(page)
        html = get_html(page_url)
        soup = get_soup(html)
        cards = get_product_cards(soup)
        get_data_from_card(cards)
main()
    



html = get_html(url)
soup = get_soup(html)
# print(get_last_page_number(soup))
cards = get_product_cards(soup)
get_data_from_card(cards)


