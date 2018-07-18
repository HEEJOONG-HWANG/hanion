# -*- coding: utf-8 -*-
 
#---------------------------------
# kakaobot.py  (상윤 ver)
#---------------------------------
 
import os
from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

req = requests.get("http://www.kyonggi.ac.kr/webRestMenu.kgu?mzcode=K00M04038500&restGb=suwon")
html = req.text
soup = BeautifulSoup(html, 'html.parser')
soup_ssy = soup.find_all(attrs={'class':'text_center'})
'''
for i in soup_ssy:
    print(i.text)
'''   

app = Flask(__name__)
 
@app.route('/keyboard')
def Keyboard():
    dataSend = {
        "type" : "buttons",
        "buttons" : ["대화하기!", "도움말"]
    }
    return jsonify(dataSend)
 
@app.route('/message', methods=['POST'])
def Message():
    dataReceive = request.get_json()
    content = dataReceive['content']
    if content == u"대화하기!":
        dataSend = {
            "message": {
                "text": "명령어 목록!\n1. 도움말\n2. 메뉴\n3. 연락처"
            }
        }
    elif content == u"도움말":
        dataSend = {
            "message": {
                "text": "이제 곧 정식 버전이 출시될거야. 조금만 기다려~~~"
            }
        }
    elif u"안녕" in content:
        dataSend = {
            "message": {
                "text": "안녕~~ 반가워 ㅎㅎ"
            }
        }
    elif content == u"test":
        dataSend = {
            "type" : "buttons",
             "buttons" : ["창의공대", "자연과학대"]
            }
            
    elif u"메뉴" in content:
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/webRestMenu.kgu?mzcode=K00M04038500&restGb=suwon"
            }
        }
        #크롤링해서 제공할 예정
    elif u"연락처" in content:
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguTel.kgu?mzcode=K00M00020400"
            }
        }    
        #이하 동문
    elif u"저기" in content:
        dataSend = {
            "message": {
                "text": "볼일 끝났으면 썩 꺼져!"
            }
        }
    else: ##예외처리 추가해줘야 할 부분 방식 생각해보기
        dataSend = {
            "message": {
                "text": content
            }
        }
    return jsonify(dataSend)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 5000)


#####################################################