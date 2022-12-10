# from django.http import HttpResponse
from django.shortcuts import render
# from .models import Question

def upload(request):
    # return HttpResponse("안녕하세요 오신것을 환영합니다.")
    return render(request, 'upload.html')

def check(request):
    return render(request, 'check.html')

def final_check(request):
    return render(request, 'final_check.html')