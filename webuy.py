"""
A library to scrape webuy.com (CeX)
"""
import sys
import json
import requests
from bs4 import BeautifulSoup as bs
from pprint import pprint
import sys

# Change this to match the store you want to monitor
# You can get this from the webpage

STORE_ID = {
    'storeName': 'Guildford',
    'storeId': 208
}


# BASE_URL="https://uk.webuy.com/"
requests.adapters.DEFAULT_RETRIES = 5
BASE_URL="https://wss2.cex.uk.webuy.io/v3/boxes?storeIds=[{}]&categoryIds=[{}]&firstRecord=1&count=50&sortBy=boxname&sortOrder=desc"
CAT_URL="https://wss2.cex.uk.webuy.io/v3/categories?productLineIds=[70,81,92,91,8,49,59,6,33,29,67,74,39,79,7,10,26,54,17,40,78,13,14,32,25,28,15,61,62,76,27,21,16,51,80,65,18,23,84,83,19,85,71,68,60,73,64,63,75]"
STORE_URL="https://wss2.cex.uk.webuy.io/v3/stores"
HEADERS = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}


class WebuyProduct:
    prodTitle=None
    prodPrice=None

    def __init__(self, **kwargs):
        self.prodTitle=kwargs.get('boxName')
        self.prodPrice=float(kwargs.get('sellPrice'))

    def __lt__(self, other):
        return self.prodTitle < other.prodTitle

    def __gt__(self, other):
        return self.prodTitle > other.prodTitle
    
    def __eq__(self, other):
        return self.prodTitle == other.prodTitle

    def __repr__(self):
        return self.prodTitle

class WebuyCategory:
    categoryId = None
    categoryName = None

    def __init__(self, **kwargs):
        self.categoryName=kwargs.get('categoryName', 'Unnamed Category')
        self.categoryId=kwargs.get('categoryId', None)

    def __str__(self):
        return "{} <{}>".format(self.categoryName, self.categoryId)

class WebuyStore:
    storeLocation = None
    storeName = None
    storeId = None

    def __init__(self, **kwargs):
        self.storeLocation = kwargs.get('storeLocation')
        self.storeName = kwargs.get('storeName')
        self.storeId = kwargs.get('storeId')

    def __str__(self):
        return "{} <{}>".format(self.storeName, self.storeId)

    def category_list(self, cat, sort=True):
        """
        return a list of all objects in a particular category
        """
        url = BASE_URL.format(self.storeId, cat.categoryId)
        page = requests.get(url, headers=HEADERS)
        response = json.loads(page.text)['response'].get('data')
        res = []
        if response:
            for item in response['boxes']:
                res.append(WebuyProduct(**item))
        if sort:
            res.sort()
        return res

def get_store_name(store_data):
    """
    grabs input to choose a store name
    """
    # build a list
    regions = {}
    for store in store_data:
        if store['regionName'] not in regions.keys():
            regions[store['regionName']] = []
        regions[store['regionName']].append(store)

    i = 1
    print("Choose a region:")
    region_list = list(regions.keys())
    region_list.sort()
    for region in region_list:
        print("{:>2} {}".format(i, region))
        i = i + 1
    region = int(input("Number: ").strip()) - 1

    i = 1

    store_list = regions[region_list[region]]
    store_list.sort()
    for store in store_list:
        print(store['storeName'])


def main():
    """
    run a little demo
    """
    # load categories...
    page = requests.get(CAT_URL, headers=HEADERS)
    cats_data = json.loads(page.text)['response'].get('data')['categories']
    # page = requests.get(STORE_URL, headers=HEADERS)
    # store_data = json.loads(page.text)['response'].get('data')['stores']
    # pprint(store_data)
    # get_store_name(store_data)
    cats = []



    for catId in [1049, 1055, 1059, 51, 1103, 1052, 1037, 972]:
        cat = next(item for item in cats_data if item["categoryId"] == catId)
        cats.append(WebuyCategory(categoryName=cat["categoryFriendlyName"],categoryId=catId))

    print(f"Got {len(cats)} categories")
    gld = WebuyStore(storeName='Guildford', storeId=208)

    for cat in cats:
        print(cat)
        print(len(str(cat))*"=")
        for item in gld.category_list(cat):
            print(f"{item.prodTitle:<60}{item.prodPrice:>10.2f}")
        print("\n\n")

if __name__ == '__main__':
    main()
