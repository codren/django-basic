from django.shortcuts import render
from .models import User
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')

    elif request.method == 'POST':
        # username = request.POST['username']
        # password = request.POST['password']
        # re_password = request.POST['re-password']

        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        # if password != re_password:
        #     return HttpResponse('비밀번호가 다릅니다')

        res_data ={}

        if not (username and password and re_password):
            res_data['error'] = '모든 값을 입력하세요.'
        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:
            user = User(
                username=username,
                password=make_password(password)
            )
            user.save()

    return render(request, 'register.html', res_data)
