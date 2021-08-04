from django.urls import path

from accountapp.views import hello_world, AccountCreateView

app_name = "accountapp"



urlpatterns = [
    # 21강 // 11번 라인은 함수형 veiw에서 쓰이는 타입
    path('hello_world/', hello_world, name='hello_world'),
    # 21강 // 13번 라인은 Class형 view에서 쓰이는 타입. 여기서 AccountCreateView는 accountapp view파일에 있는 AccountCreateView 함수임.
    path('create/', AccountCreateView.as_view(), name='create'),
]