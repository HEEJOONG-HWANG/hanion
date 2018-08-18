
---------------------------------
 #kakaobot.py  (상윤 ver)
---------------------------------

import os
from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup
from PIL import Image

im = Image.open('test1.jpg')
# im.save('python.jpg')

req = requests.get(
    "http://www.kyonggi.ac.kr/webRestMenu.kgu?mzcode=K00M04038500&restGb=suwon")
html = req.text
soup = BeautifulSoup(html, 'html.parser')
soup_ssy = soup.find_all(attrs={'class': 'text_center'})
'''
for i in soup_ssy:
    print(i.text)
'''

app = Flask(__name__)


@app.route('/keyboard')
def Keyboard():
    dataSend = {
<<<<<<< HEAD
        "type" : "buttons",
        "buttons" : ["대화하기!", "도움말", "학사일정"]
=======
        "type": "buttons",
        "buttons": ["대화하기!", "도움말"]
>>>>>>> 2b762c6f0b3eb3c6d4aaff52779c54d50378a89b
    }
    return jsonify(dataSend)


@app.route('/message', methods=['POST'])
def Message():
    dataReceive = request.get_json()
    content = dataReceive['content']
    if content == u"대화하기!":
        dataSend = {
            "message": {
                "text": "명령어 목록!\n1. 스쿨버스 \n2. 학식 \n3. 캠퍼스맵 \n4. 연락처 \n5. 자유게시판\n6. 도서관\n7. 교육과정 \n8. 쿠티스 링크\n9. 인재개발처\n10. 동아리관련\n11. 박물관\n12. 강의시간표"
            }
        }
    elif u"스쿨버스" in content:
        dataSend = {
            "message": {
                "text": "고양이버스, 학생통학버스, 통근버스, 방학통학버스 중 필요하신 키워드를 입력해주세요."
            }
        }
<<<<<<< HEAD
    elif content == u"학사일정":
        dataSend = {
            "message": {
                #학사일정 url을 못찾았어요......
            }
        }
    elif u"안녕" in content:
=======
    elif u"고양이버스" in content:
>>>>>>> 2b762c6f0b3eb3c6d4aaff52779c54d50378a89b
        dataSend = {
            "message": {
                "text": "https://www.kyonggi.ac.kr/webService.kgu?menuCode=K00M04002302"
            }
        }
    elif u"학생통학버스" in content:
        dataSend = {
            "message": {
                "text": "https://www.kyonggi.ac.kr/webService.kgu?menuCode=K00M04002303"
            }
        }
    elif u"방학통학버스" in content:
        dataSend = {
            "message": {
                "text": "https://www.kyonggi.ac.kr/webService.kgu?menuCode=K00M04002300"
            }
        }
    elif u"통근버스" in content:
        dataSend = {
            "message": {
                "text": "https://www.kyonggi.ac.kr/webService.kgu?menuCode=K00M04002301"
            }
        }
    elif u"학식" in content:
        dataSend = {
            "message": {
                "https://www.kyonggi.ac.kr/webRestMenu.kgu?mzcode=K00M04025700&restGb=suwon"
            }
        }
    elif u"캠퍼스맵" in content:
        dataSend = {
            "message": {
                "photo": {
                    "url": "http://www.kyonggi.ac.kr/web/images/kgu/contents/tour_img_new.jpg",
                    # "url": "/home/ubuntu/hanion/kakaobot/test1.jpg",
                    "width": 800,
                    "height": 512,
                    "text": "1.진리관(대학본부/관광대학) : 정문우측건물\n2.교육관 : 정문에서 우측으로 200m\n3.조리실습동 : 정문에서 우측으로(진리관 뒷편길 이용)\n4.성신관(체육대학) : 정문에서 우측으로 350m\n5.애경관/체육대학 : 정문에서 우측으로 300m\n6.체육관 : 정문에서 우측으로 250m 후 아랫길로 100m 애경관 뒷편\n7.중앙도서관 : 정문에서 정면으로 120m\n8.예지관(인문대학/경상대학) : 정문에서 정면으로 250m\n9.덕문관/법과대학/사회과학대학 : 정문에서 정면으로 250m 후 오른편길로 50m\n10. E-스퀘어 : 정문에서 정면으로 320m(학생식당 및 학생복지공간)\n11.감성코어 : 정문에서 정면으로 120m 후 중앙도서관 옆길로 50m(카페테리아)\n12.광교관(자연과학대학) : 정문에서 정면으로 450m, 혹은 중앙도서관 뒷길로 550m\n13.집현관(공학관) : 정문에서 정면으로 500m, 혹은 중앙도서관 뒷길로 500m\n14.육영관(자연과학관) : 정문에서 정면으로 550m, 혹은 중앙도서관 뒷길로 550m\n15.공과대학 : 정문에서 정면으로 650m, 혹은 후문에서 정면으로 150m 후 우측으로 200m\n16.공학실습동 : 중앙도서관 뒷길로 500m 후 집현관 뒷길 50m\n17.리서치센터 : 정문에서 정면으로 650m 후 공과대학 뒷편, 혹은 후문에서 정면으로 150m 후 우측으로 250m\n18.산학협력단(창업보육센터) : 정문에서 정면으로 550m\n19.종합강의동 : 정문에서 정면으로 350m 후 좌측길로 50m, 혹은 중앙도서관 뒷길로 450m\n20.교수연구동 : 정문에서 중앙도서관 뒷길로 300m\n21.학생회관 : 정문에서 중앙도서관 뒷길로 250m, 혹은 정문에서 좌측으로 200m후 우측으로 100m, 제1복지관 뒤\n22.제1복지관 : 정문에서 좌측으로 200m후 우측으로 100m\n23.어울림관 : 정문에서 좌측으로 200m후 우측으로 100m, 제1복지관 좌측 건물\n24.박물관 : 정문에서 좌측으로 200m후 우측으로 100m, 제1복지관 우측 건물"
                }
            }

        }
    elif u"캠퍼스맵설명" in content:
        dataSend = {
            "message": {
                "text": "1.진리관(대학본부/관광대학) : 정문우측건물\n2.교육관 : 정문에서 우측으로 200m\n3.조리실습동 : 정문에서 우측으로(진리관 뒷편길 이용)\n4.성신관(체육대학) : 정문에서 우측으로 350m\n5.애경관/체육대학 : 정문에서 우측으로 300m\n6.체육관 : 정문에서 우측으로 250m 후 아랫길로 100m 애경관 뒷편\n7.중앙도서관 : 정문에서 정면으로 120m\n8.예지관(인문대학/경상대학) : 정문에서 정면으로 250m\n9.덕문관/법과대학/사회과학대학 : 정문에서 정면으로 250m 후 오른편길로 50m\n10. E-스퀘어 : 정문에서 정면으로 320m(학생식당 및 학생복지공간)\n11.감성코어 : 정문에서 정면으로 120m 후 중앙도서관 옆길로 50m(카페테리아)\n12.광교관(자연과학대학) : 정문에서 정면으로 450m, 혹은 중앙도서관 뒷길로 550m\n13.집현관(공학관) : 정문에서 정면으로 500m, 혹은 중앙도서관 뒷길로 500m\n14.육영관(자연과학관) : 정문에서 정면으로 550m, 혹은 중앙도서관 뒷길로 550m\n15.공과대학 : 정문에서 정면으로 650m, 혹은 후문에서 정면으로 150m 후 우측으로 200m\n16.공학실습동 : 중앙도서관 뒷길로 500m 후 집현관 뒷길 50m\n17.리서치센터 : 정문에서 정면으로 650m 후 공과대학 뒷편, 혹은 후문에서 정면으로 150m 후 우측으로 250m\n18.산학협력단(창업보육센터) : 정문에서 정면으로 550m\n19.종합강의동 : 정문에서 정면으로 350m 후 좌측길로 50m, 혹은 중앙도서관 뒷길로 450m\n20.교수연구동 : 정문에서 중앙도서관 뒷길로 300m\n21.학생회관 : 정문에서 중앙도서관 뒷길로 250m, 혹은 정문에서 좌측으로 200m후 우측으로 100m, 제1복지관 뒤\n22.제1복지관 : 정문에서 좌측으로 200m후 우측으로 100m\n23.어울림관 : 정문에서 좌측으로 200m후 우측으로 100m, 제1복지관 좌측 건물\n24.박물관 : 정문에서 좌측으로 200m후 우측으로 100m, 제1복지관 우측 건물"
            }
        }

    elif content == u"연락처":
        dataSend = {
            "message": {
                "text": "융합교양대학, 휴먼인재융합대학, 지식정보서비스대학, 융합과학대학, 창의공과대학, 중 필요하신 키워드를 입력해주세요."
            }
        }
    elif u"융합교양대학" in content:
        dataSend = {
            "message": {
                "text": "교직학부, 교양학부 중 필요하신 키워드를 입력해주세요."
            }
        }
    elif content == u"교직학부":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010100&orgCd=K010213"
            }
        }
    elif content == u"교양학부":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010000&orgCd=K010101"
            }
        }

    elif u"유아교육과" in content:
        dataSend = {
            if { u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010110&orgCd=K010212"
                     }
                }
            }
            elif { u"교육과정" in content:
                  dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01011001&orgCd=K010212"
                    }
                }
            }
    elif u"국어국문학과" in content:
        dataSend = {
            if { u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010101&orgCd=K010201"
                    }
                }
            }
            elif { u"교육과정" in content:
                   dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01010101&orgCd=K010201"
                    }
                }
            }
        }
    elif u"영어영문학과" in content:
        dataSend = {
            if{ u"연락처" in content:
                dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010105&orgCd=K010203"
                    }
                }
            }
            elif { u"교육과정" in content:
                   dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01010501&orgCd=K010203"
                        }
                    }
                }
            }

    elif u"중어중문학과" in content:
        dataSend = {
            if { u"연락처" in contnet:
                 dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010104&orgCd=K010208"
                }
            }
        }
            elif { u"교육과정" in content:
                   dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01010401&orgCd=K010208"
                        }
                    }
                }
            }
    elif u"사학과" in content:
        dataSend = {
            if { u"연락처" in contnet:
                 dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010108&orgCd=K010209"
                }
            }
        }
            elif { u"교육과정" in content:
                   dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01010801&orgCd=K010209"
                        }
                    }
                }
            }

    elif u"문헌정보학과" in content:
        dataSend = {
            if { u"연락처" in contnet:
                 dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010109&orgCd=K010210"
                }
            }
        }
            elif { u"교육과정" in content:
                   dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01010901&orgCd=K010210"
                        }
                    }
                }
            }

    elif u"문예창작학과" in content:
        dataSend = {
            if { u"연락처" in contnet:
                 dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010102&orgCd=K010211"
                }
            }
        }
            elif { u"교육과정" in content:
                   dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01010201&orgCd=K010211"
                        }
                    }
                }
            }
    elif u"독어독문전공" in content:
        dataSend = {
            if { u"연락처" in contnet:
                 dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010106&orgCd=K010205"
                }
            }
        }
            elif { u"교육과정" in content:
                   dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01010601&orgCd=K010205"
                        }
                    }
                }
            }
    elif u"불어불문전공" in content:
        dataSend = {
            if { u"연락처" in contnet:
                 dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010107&orgCd=K010206"
                }
            }
        }
            elif { u"교육과정" in content:
                   dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01010701&orgCd=K010206"
                        }
                    }
                }
            }
    elif u"일어일문전공" in content:
        dataSend = {
            if { u"연락처" in contnet:
                 dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010103&orgCd=K010207"
                }
            }
        }
            elif { u"교육과정" in content:
                   dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01010301&orgCd=K010207"
                        }
                    }
                }
            }
    elif u"러시아어문전공" in content:
        dataSend = {
            if { u"연락처" in contnet:
                 dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010111&orgCd=K010214"
                }
            }
        }
            elif { u"교육과정" in content:
                   dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01011101&orgCd=K010214"
                        }
                    }
                }
            }
    elif u"서양화미술경영학과" in content:
        dataSend = {
            if { u"연락처" in contnet:
                 dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010921&orgCd=K011017"
                }
            }
        }
            elif { u"교육과정" in content:
                   dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01092101&orgCd=K011017"
                        }
                    }
                }
            }
    elif u"입체조형학과" in content:
        dataSend = {
            if { u"연락처" in contnet:
                 dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010919&orgCd=K011015"
                }
            }
        }
            elif { u"교육과정" in content:
                   dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01091901&orgCd=K011015"
                        }
                    }
                }
            }
    elif u"한국화서예학과" in content:
        dataSend = {
            if { u"연락처" in contnet:
                 dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010920&orgCd=K011016"
                }
            }
        }
            elif { u"교육과정" in content:
                   dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01092001&orgCd=K011016"
                        }
                    }
                }
            }
    elif u"산업디자인전공" in content:
        dataSend = {
            if { u"연락처" in contnet:
                 dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010906&orgCd=K011002"
                }
            }
        }
            elif { u"교육과정" in content:
                   dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01090601&orgCd=K011002"
                        }
                    }
                }
            }
    elif u"시각정보디자인전공" in content:
        dataSend = {
            if { u"연락처" in contnet:
                 dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010905&orgCd=K011001"
                }
            }
        }
            elif { u"교육과정" in content:
                   dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01090501&orgCd=K011001"
                        }
                    }
                }
            }
    elif u"장신구금속디자인전공" in content:
        dataSend = {
            if { u"연락처" in contnet:
                 dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M010907&orgCd=K011003"
                }
            }
        }
            elif { u"교육과정" in content:
                   dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01090701&orgCd=K011003"
                        }
                    }
                }
            }
    elif u"스포츠건강과학전공" in content:
        dataSend = {
            if { u"연락처" in contnet:
                 dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguSbjInfo.kgu?mzcode=K00M011001&orgCd=K011102"
                }
            }
        }
            elif { u"교육과정" in content:
                   dataSend = {
                "message": {
                    "text": "http://www.kyonggi.ac.kr/curriculumSrv.kgu?mzcode=K00M01100101&orgCd=K011102"
                        }
                    }
                }
            }

    elif u"박물관" in content:
        dataSend = {
            "message": {
                "text": "http://museum.kyonggi.ac.kr/index.html"
            }
        }

    elif content == u"건학이념":
        dataSend = {
            "message": {
                "photo": {
                    "url": "http://www.kyonggi.ac.kr/uploads/09651eab-35a7-4443-8a5c-7b4f56b636f1.jpg",
                    # "url": "/home/ubuntu/hanion/kakaobot/test1.jpg",
                    "width": 535,
                    "height": 512
                }
            }

        }

    elif u"메뉴" in content:
        req = requests.get(
            "http://www.kyonggi.ac.kr/webRestMenu.kgu?mzcode=K00M04038500&restGb=suwon")
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        for tag in soup.find_all(attrs={'class': 'text_center'}):
            dataSend = {
                "message": {
                    "text": "%s" % tag.text.strip()
                }

            }
    elif content == u"메뉴링크":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/webRestMenu.kgu?mzcode=K00M04038500&restGb=suwon"
            }
        }
        # 크롤링해서 제공할 예정
    elif content == u"연락처링크":
        dataSend = {
            "message": {
                "text": "http://www.kyonggi.ac.kr/kguTel.kgu?mzcode=K00M00020400"
            }
        }
        # 크롤링해서 제공할 예정
    elif u"연락처" in content:
        req = requests.get(
            "http://www.kyonggi.ac.kr/kguTel.kgu?mzcode=K00M00020400")
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        for tag in soup.find_all(attrs={'class': 'table_t4'}):
            dataSend = {
                "message": {
                    "text": "%s" % tag.text.strip()
                }

            }
            # 이하 동문

    elif u"인재개발처" in content:
        dataSend = {
            "message": {
                "text": "http://job.kyonggi.ac.kr/"
            }
        }

    elif u"도서관" in content:
        dataSend = {
            "message": {
                "text": "1. 공지사항\n http://library.kyonggi.ac.kr/bbs/list/1\n"
                        "2. 소장 자료검색\n http://library.kyonggi.ac.kr/search/tot\n"
                        "3. 열람실 좌석현황\n http://libgate.kyonggi.ac.kr/roomstatus/index.asp\n"
                        "4. 대출\n http://library.kyonggi.ac.kr/myloan/list\n"
                        "5. 희망도서\n http://library.kyonggi.ac.kr/purchaserequest/write\n"
                        "6. 도서관 시설예약\n http://library.kyonggi.ac.kr/roomreserve/dateList/1"
            }
        }

    elif u"쿠티스" in content:
        dataSend = {
            "message": {
                "text": "http://kutis.kyonggi.ac.kr/webkutis/"
            }
        }

    elif u"꺼져" in content:
        dataSend = {
            "message": {
                "text": "볼일 끝났으면 썩 꺼져!"
            }
        }
<<<<<<< HEAD
    else: ##예외처리 추가해줘야 할 부분 방식 생각해보기
        #메세지 텍스트로 "오타나 띄어쓰기를 주의해주세요" // "지원하지 않는 메뉴입니다" 이러고 도움말로 넘어가는거 어때요?
=======
    else:  # 예외처리 추가해줘야 할 부분 방식 생각해보기
>>>>>>> 2b762c6f0b3eb3c6d4aaff52779c54d50378a89b
        dataSend = {
            "message": {
                "text": content
            }
        }
    return jsonify(dataSend)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)

######################################################
