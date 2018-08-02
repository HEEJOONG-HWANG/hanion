# -*- coding: utf-8 -*-
import os
from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
from PIL import Image

im = Image.open('test1.jpg')


req = requests.get("http://www.kyonggi.ac.kr/webRestMenu.kgu?mzcode=K00M04038500&restGb=suwon")
html = req.text
soup = BeautifulSoup(html, 'html.parser')


app = Flask(__name__)


@app.route('/keyboard')
def Keyboard():
    dataSend = {
        "type": "buttons",
        "buttons": ["대화하기!", "도움말"]
    }
    return jsonify(dataSend)


@app.route('/message', methods=['POST'])
def Message():
    dataReceive = request.get_json()
    content = dataReceive['content']
    if content == u"대화하기!":
        dataSend = {
            "message": {

            }
        }
        elif content == u"지식재산학과":
        dataSend = {
            "message": {

            }
        }
        elif content == u"경영학과":
        dataSend = {
            "message": {
    elif u"연락처" in content:
        req = requests.get("http://www.kyonggi.ac.kr/kguTel.kgu?mzcode=K00M00020400")
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
    elif u"꺼져" in content:
        dataSend = {
            "message": {
                "text": "볼일 끝났으면 썩 꺼져!"
            }
        }

        dataSend = {
            "message": {
                 "text": content
            }
        }
    return jsonify(dataSend)
