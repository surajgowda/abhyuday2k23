import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
html = requests.get('https://pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html.text,'html.parser')
imgs = bs.find_all('tr').findChildren()
for img in imgs:
    print(img)