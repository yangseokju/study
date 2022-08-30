from django.shortcuts import render
import random

# Create your views here.
def index(request):
    # request : 사용자의 요청 정보가 담겨있다.
    # HTTP 요청을 수신하고 HTTP 응답을 반환하는 함수 작성
    # Template에게 HTTP 응답 서식을 맡김
    return render(request, "index.html")
    # 1. request
    # : 응답을 생성하는 데 사용되는 요청 객체
    # 2. template_name
    # : 템플릿의 전체 이름 또는 템플릿 이름의 경로
    # 3. context
    # : 템플릿에서 사용할 데이터(딕셔너리 타입으로 작성)

def greeting(request):
    # 데이터를 생성
    foods = ["사과","바나나","코코넛"]
    info = {"name":"양석주"}

    # 각 데이터들을 큰 딕셔너리로 묶어준다
    context ={
        "foods": foods,
        "info" : info
    }
    return render(request, "greeting.html",context)

def dinner(request):
    foods = ["족발","햄버거","치킨","초밥"]
    pick = random.choice(foods)
    numbers = random.randrange(1,100)
    
    context = {
        "pick":pick,
        "foods":foods,
        "numbers":numbers
    }
    return render(request,"dinner.html")

def throw(request):
    return render(request,"throw.html")

def catch(request):
    message = request.GET.get('message')
    context = {
        'message' : message,
    }
    return render(request,"catch.html",context)

def hello(request, name):
    context = {
        'name':name,
    }
    return render(request,'hello.html',context)