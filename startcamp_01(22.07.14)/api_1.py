""" import requests

url = 'https://api.agify.io/?name=jun'
#requests.get('url') #url에 정보를 달라는(get) 요청(requests)을 보내줘
#print(requests.get('url').json()) #url에 정보를 달라는(get) 요청(requests)을 보내줘 정보(json)만 보여줘 #파이썬의 딕셔너리처럼 사용할수 있는 json()

response = requests.get(url).json() #서버에게 요청을 보낸후 서버의 응답 데이터를 변수에 저장
 """
""" 
#이름만 출력하고 싶어요
print(response.get("name")) # jun
#s나이만 출력하고 싶어요
print(response.get("age")) # 50
#get(key) ==> 딕셔너리의 해당 키에 매칭되는 값을 가져온다.
 """

import requests #pip.install.requests 를 사용해서 requests 라이브러리를 다운받는다

url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1021' #사용하고싶은 url 입력

response = requests.get(url).json() #print(requests.get('url').json()) #url에 정보를 달라는(get) 요청(requests)을 보내줘 정보(json)만 보여줘 #파이썬의 딕셔너리처럼 사용할수 있는 json()

for i in range(1,7): # 1~6까지
    key = f"drwtNo{i}" #drwtNo1~drwtNo6 까지를 받음
    print(response.get(key)) #key값만 출력

    sum(iterable)