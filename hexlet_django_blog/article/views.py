from django.shortcuts import render
from django.http import HttpResponse
from django.views import View



class IndexView(View):
     def get(self, request, *args, **kwargs):
         return HttpResponse('<h1>Welcome to My Django Blog!</h1>')



# def index(request, tags, article_id):
#     return render(request, 'articles/index.html', context={
#         'app_name': '"hexlet_django_blog"',
#     })
