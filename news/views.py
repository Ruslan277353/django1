from django.shortcuts import render

from news.models import NewsModel


def home_page(request):
    news = NewsModel.objects.all()
    context = {'news': news}
    return render(request, template_name='index.html', context=context)
