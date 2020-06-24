#
import bcrypt
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from django.views.decorators.csrf import csrf_exempt

from ..forms import SignUpForm
from ..models import UserInfo

# @csrf_exempt
def post(request):
    return JsonResponse({"message" : "응답완료"})
    # data = request.POST
    # form = SignUpForm(data)
    # print(form)
    # print(data)
    # try:
    #
    #     #    DB에 존재하는 이메일인 경우
    #     if UserInfo.objects.filter(email=data['email']).exists():
    #         return JsonResponse({"message": "EMAIL_EXISTED"}, status=400)
    #
    #     # if form.is_valid():
    #     #     #   입력 form이 비어있는 경우
    #     #     # if data['email'] == '' or data['password'] == '' or data['username'] == '' or data['gender'] == '':
    #     #     #     return JsonResponse({"message": "EMPTY_EMAIL"})
    #     #
    #     #     #   비밀번호 암호화
    #     #     password = data['password'].encode('utf-8')
    #     #     password_crypt = bcrypt.hashpw(password, bcrypt.gensalt())
    #     #     password_crypt = password_crypt.decode('utf-8')
    #     #
    #     #     #   계정 회원가입
    #     #     UserInfo(
    #     #         email=data['email'],
    #     #         password=password_crypt,
    #     #         username=data['username'],
    #     #         gender=data['gender']
    #     #     ).save()
    #     #
    #     #     # #   저장 성공시 회원가입 성공 페이지가 렌더링
    #     #     return render(request=request, template_name='toy_api/signup_success.html')
    #     # else:
    #     #     form = SignUpForm()
    #     # return render(request, 'toy_api/signup.html', {
    #     #     'form': form,  # 검증 실패시 form.error에 오류 정보를 저장해 함께 렌더링
    #     # })
    #     return JsonResponse({"message": "응답완료"})
    # except KeyError:
    #     #   잘못된 전송 데이터 키를 받은 경우
    #     return JsonResponse({"message": "INVALID_KEYS"})

# class SignupView(View):
#     # success_url = 'toy_api/signup'
#
#     # Get 방식으로 toy_api/signup/ 접속시
#     def get(self, request):
#         # toy_api/signup.html 템플릿 렌더
#         form = SignUpForm()
#         return render(request, 'toy_api/signup.html', {'form': form})
#
#     # Post 방식으로 toy_api/signup/ 회원가입 데이터 전송시
#     #
#     def post(self, request):
#         data = request.POST
#         # form = SignUpForm(data)
#         # print(form)
#         print(data)
#         try:
#
#             #    DB에 존재하는 이메일인 경우
#             if UserInfo.objects.filter(email=data['email']).exists():
#                 return JsonResponse({"message": "EMAIL_EXISTED"}, status=400)
#
#             # if form.is_valid():
#             #     #   입력 form이 비어있는 경우
#             #     # if data['email'] == '' or data['password'] == '' or data['username'] == '' or data['gender'] == '':
#             #     #     return JsonResponse({"message": "EMPTY_EMAIL"})
#             #
#             #     #   비밀번호 암호화
#             #     password = data['password'].encode('utf-8')
#             #     password_crypt = bcrypt.hashpw(password, bcrypt.gensalt())
#             #     password_crypt = password_crypt.decode('utf-8')
#             #
#             #     #   계정 회원가입
#             #     UserInfo(
#             #         email=data['email'],
#             #         password=password_crypt,
#             #         username=data['username'],
#             #         gender=data['gender']
#             #     ).save()
#             #
#             #     # #   저장 성공시 회원가입 성공 페이지가 렌더링
#             #     return render(request=request, template_name='toy_api/signup_success.html')
#             # else:
#             #     form = SignUpForm()
#             # return render(request, 'toy_api/signup.html', {
#             #     'form': form,  # 검증 실패시 form.error에 오류 정보를 저장해 함께 렌더링
#             # })
#             return JsonResponse({"message" : "응답완료"})
#         except KeyError:
#             #   잘못된 전송 데이터 키를 받은 경우
#             return JsonResponse({"message": "INVALID_KEYS"})
