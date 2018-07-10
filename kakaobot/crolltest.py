### 상윤 크롤링 학식부터 시작

"""
import requests
from bs4 import BeautifulSoup

ssy = requests.get("http://www.kyonggi.ac.kr/webRestMenu.kgu?mzcode=K00M04038500&restGb=suwon").text
keywords=BeautifulSoup(ssy,"lxml")
#keywords=keywords.select(" .text_center")
keywords=keywords.select_one(".table_t1")
ssy2=keywords.select_one("td")
print(ssy2)
"""

import requests
from bs4 import BeautifulSoup

r = requests.get("http://www.kyonggi.ac.kr/webRestMenu.kgu?mzcode=K00M04038500&restGb=suwon")
c = r.content
#print(c)
html = BeautifulSoup(c,"html.parser")

keywords=html.select(" .text_center")
#ssy3 = html.find("div",{"class":"text_center"})
#ssy = html.find(".text_center")
#ssy2= ssy.find("tr")
print(keywords)

tr=html.find("tr")
#print(tr)
td=tr.find_all("td")
#print(td)
"""
for tr in td:
    div = tr.find("div",{"class":"text_center"})
    print(div)
"""    