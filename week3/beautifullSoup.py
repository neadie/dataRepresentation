"""
Created on Thu Oct  8 21:57:53 2020

@author: sinead
"""
import requests
from bs4 import BeautifulSoup
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print (page)
print("-------------------")
print (page.content)
soup1 = BeautifulSoup(page.content, 'html.parser')
print("-------------------")
print (soup1.prettify())
