from django.http import HttpResponse
from django.shortcuts import render
from accountapp.models import HelloWorld


# Create your views here.


def hello_world(request):

    if request.method == "POST":
        # 17강 // hellow_world_input의 이름으로 POST방식으로 request를 받을 경우 temp변수에 저장시킨다는 의미
        temp = request.POST.get('hello_world_input')

        # 17강 // accountapp폴더 > Models.py에 있는 HelloWorld class 추가
        # 17강 // HelloWorld객체를 통해 새로 생성된 친구를 new_hello_world에 추가
        new_hello_world = HelloWorld()
        # 17강 // new_hello_world에서 생성된 text를 temp에 저장
        new_hello_world.text = temp
        new_hello_world.save()

        # 16강 // context={} >> data 꾸러미의 일종으로 POST로 request를 받으면 POST METHOD!!!라는 이름의 text데이터를 render해주라는 의미
        # 17강 // hello_world_input에 입력된 text를 POST로 받을 경우 new_hello_world 변수로 보내 저장한다.
        return render(request, 'accountapp/hello_world.html', context={'hello_world_output': new_hello_world})
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD!!!'})
