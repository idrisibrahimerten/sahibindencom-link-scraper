# -*- coding: utf-8 -*-
"""

@author: IdrisIbrahimERTEN
"""
import requests
import time
from lxml import html
from time import sleep

links = []

def get_xpath_element_link(elements):
    if elements:
        return  ['https://www.sahibinden.com{}'.format(el.get('href')) for el in elements]
    else:
        return None

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36'}

client = requests.session()

def linkCikar(search_word, page=0):
	url = "https://www.sahibinden.com/vasita?query_text_mf={}&query_text={}".format(search_word, search_word) # link buraya eklenecek.


	r = client.head(url, headers=headers)

	print('page status code ', r.status_code)

	print('Go to ', url)

	page = client.get(url, headers=headers)

	print('Page opened successfully')
	# print(page.content)
	tree = html.fromstring(page.content)

	scrapeLink = get_xpath_element_link(tree.xpath("//a[@class = ' classifiedTitle' ]"))

	print('scrapedLink ', scrapeLink)

	for link in  scrapeLink:
		time.sleep(3)
		links.append(link)
        
        
linkCikar('passat', page=1)
print(links)