"""
파이썬으로 크롤링 하기 준비 
환경 : visual studio code
교제 : 파이썬으로 배우는 웹 크롤러, 파이써으로 웹크롤러 만들기
"""
from urllib.request import urlopen # urllib라이브러리에서 파이썬 모듈 requst를 읽어 open함수 하나만 임포트
html=urlopen("https://search.naver.com/search.naver?where=nexearch&query=%EC%B9%B4%EB%A6%AC%EC%9A%B0%EC%8A%A4&sm=top_lve&ie=utf8")
#오픈하려는 주소 (나중에 api 주소 입력과 변수설정 추가해서 사용할듯)
print(html.read()) #데이터 읽어드림 (파싱하기 전에 출력 확인)
