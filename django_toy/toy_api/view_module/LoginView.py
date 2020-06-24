from django.http import JsonResponse
from django.views import View
import json

# 로그인 페이지 대응 뷰

class LoginView(View):

    def post(self, request):
        # 직렬화된 데이터 디코드
        data = json.loads(request.body.decode('utf-8'))
        # user = UserInfo.object
        username = data['username']
        password = data['password']
        salt = data['salt']
        print(f'username : {username}\npassword : {password}\nsalt : {salt}\n')
        # if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.en)
        print(username)
        return JsonResponse({'username': username, 'password': password, 'salt':salt})
    # def post(self, request):
    #     data = json.loads(request.body)
    #
    #     try:
    #         # 이메일 확인
    #         if UserInfo.objects.filter(email=data['email']).exists():
    #             user = UserInfo.objects.get(email=data['email'])
    #
    #             if bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
    #                 # 토큰 발행
    #                 token = jwt.encode({'email': data['email']}, secret_key_loader(), algorithm='HS256')
    #                 token = token.decode('utf-8')
    #                 return JsonResponse({'token': token}, status=200)
    #             else:
    #                 return HttpResponse(status=401)
    #         return HttpResponse(status=400)
    #     except KeyError:
    #         return JsonResponse({"message": "INVALID_KEY"})
