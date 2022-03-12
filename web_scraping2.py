from bs4 import BeautifulSoup
import re

with open('index2.html','r') as e:
    doc=BeautifulSoup(e,'html.parser')

#find() --> if we use this we can change the value
#find_all() --> we can't change value 
'''
tag=doc.find("option")
print(tag.attrs)
tag['value'] = 'django'
tag['selector'] = 'fa   lse'
print(tag)
'''
#tag = doc.find_all(['p','div','li'])
tag= doc.find(['option'],text='Undergraduate')
tag['value'] =' Val'
print(tag)

tags=doc.find_all(class_='btn-item')
print(tags)

'''
from bs4 import BeautifulSoup
import requests

url='https://www.newegg.ca/gigabyte-geforce-rtx-3080-ti-gv-n308tgaming-oc-12gd/p/N82E16814932436?Description=3080&cm_re=3080-_-14-932-436-_-Product'
result=requests.get(url)
doc=BeautifulSoup(result.text,'html.parser')
x1=doc.find(['script'],src="https://c1.neweggimages.com/WebResource/Scripts/WWW/ProductDetail-22c748bc.js")
print(x1)
x1['src']='https//google.com/'
print(x1)
'''

#saving modified html