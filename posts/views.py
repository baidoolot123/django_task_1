from django.shortcuts import render
from .models import Post 
from django.core.mail import send_mail
from django.conf import settings 

# Create your views here.

def main_page(request):
    return render(request, 'base.html')



def contactform(request):
    if request.method == 'POST':
        message = request.POST ['message']

        send_mail('Контакты пользователей:', 
                    message, settings.EMAIL_HOST_USER, 
                    ['baidoolot@gmail.com'], fail_silently=False)
    return render(request, 'contact_form.html')



def about(request):
    with open('posts/texts/about.txt', 'r') as file:
        data = file.read()
    return render(request, 'about.html', {'data': data})

def contacts(request):
    with open('posts/texts/contacts.txt', 'r') as file1:
        data1 = file1.read() 
    return render(request, 'contacts.html', {'data1': data1})

def gallery(request):
    posts = Post.objects.all()
    return render(request, 'gallery.html', {"posts": posts})

