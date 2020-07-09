pip install beautifulsoup4
pip install lxml
pip install html5lib

import requests
from bs4 import BeautifulSoup
import csv 

csv_file=open('mycsv.csv','w')
csv_write=csv.writer(csv_file)
csv_write.writerow(['DATE','TITLE','LINK'])
source=requests.get('http://learn-c-with-aj.blogspot.com').text
soup=BeautifulSoup(source,'lxml')

for article in soup.find_all('article'):
    links=article.find('a',class_='timestamp-link')
    dates=links.text
    print(dates)
    titles=article.find('h3',class_='post-title')
    header=titles.text;
    print(header)
    link=links.get('href')
    print(link)
    csv_write.writerow([dates.strip(),header.strip(),link.strip()])

csv_file.close()
    