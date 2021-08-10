from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from accountapp.views import hello_world, AccountCreateView, AccountDetailView

app_name = "accountapp"



urlpatterns = [
    # 21강 // 11번 라인은 함수형 veiw에서 쓰이는 타입
    path('hello_world/', hello_world, name='hello_world'),

    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    # 21강 // 13번 라인은 Class형 view에서 쓰이는 타입. 여기서 AccountCreateView는 accountapp view파일에 있는 AccountCreateView 함수임.
    path('create/', AccountCreateView.as_view(), name='create'),
    # 24강 // detail view의 경우 특정유저의 primary key(ID)가 필요한대 primary key는 특정유저에게 부여된 고유 키값임 like user token > primary key는 20번 라인에서 <int/pk에 해당함.>
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
]