from django.contrib.auth.forms import UserCreationForm

class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        # 25강 // UserCreationForm을 사용하고 있는 페이지 진입 시 6번 코드로 초기화 시킨다.
        super().__init__(*args, **kwargs)

        # 25강 // 6번 코드로 초기화 시킨 뒤 9번 코드로 username이 있는 필드를 disabled시킨다.
        self.fields['username'].disabled = True