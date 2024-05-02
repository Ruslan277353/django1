from django.shortcuts import render, redirect

from news.models import NewsModel
from django.views.generic import FormView
from news.forms import RegisterForm
from django.contrib import messages

def home_page(request):
    news = NewsModel.objects.all()
    context = {'news': news}
    return render(request, template_name='index.html', context=context)

def search_news(request):
    if request.method == 'POST':
        get_news = request.POST.get('search_news')

        try:
            exact_new = NewsModel.objects.get(title__icontains=get_news)
            print(f'Yeaah we found for you this news {exact_new}')
            return redirect(f'news/{exact_new.id}')
        except:
            print('Not Found')
            return redirect('/')

def single_new(request, id):
    new = NewsModel.objects.get(id=id)
    context = {'new': new}
    return render(request, 'single-new.html', context=context)

class MyFormView(FormView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = '/login'

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Неверное имя пользователя или пароль.')
    return render(request, 'login.html')