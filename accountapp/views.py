from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.



def hello_world(request):

    if request.method == "POST":
        # context={} >> data 꾸러미의 일종으로 POST로 request를 받으면 POST METHOD!!!라는 이름의 text데이터를 render해주라는 의미..
        return render(request, 'accountapp/hello_world.html', context={'text': 'POST METHOD!!!'})
    else:
        return render(request, 'accountapp/hello_world.html', context={'text': 'GET METHOD!!!'})
