from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

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

        # 18강 // HelloWorld 객체에 있는 모든것들을 hello_world_list에 저장
        #hello_world_list = HelloWorld.objects.all()

        # 16강 // context={} >> data 꾸러미의 일종으로 POST로 request를 받으면 POST METHOD!!!라는 이름의 text데이터를 render해주라는 의미
        # 17강 // hello_world_input에 입력된 text를 POST로 받을 경우 new_hello_world 변수로 보내 저장한다.
        # 18강 // 웹페이지를 새로고침 했을 때 마지막 입력값이 계속 나오는걸 막기 위해 HttpResponseaRedirect를 사용해서 해당 이슈를 막아야 함.
        # 18강 // reverse 함수를 활용해서 accountapp:hello_world의 주소를 자동으로 입력해 줘야 함.
            # 18강 // reverse 함수는 장고 urls.py 파일 urlpatterns에서 정의된 이름을 입력하면 자동으로 해당 url을 연결시켜 줌.
                    # 13번 라인부터 33번 라인 코드를 읽어보면  hello_world_input에 입력된 값을 POST로 accountapp models.py의 HelloWorld를 통해 DB에 추가한 뒤 HttpResponseRedirect 함수와 reverse함수를 이용해 accountapp urls.py에서 정의된 hello_world의 이름을 가진 url로 보낸다.
        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        hello_world_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
