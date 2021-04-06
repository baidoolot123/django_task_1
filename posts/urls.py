from django.urls import path 
from .views import main_page, about, contacts, gallery, contactform

urlpatterns = [
    path('',main_page, name = 'main_page'),
    path('about/', about, name='about'),
    path('contacts/', contacts, name='contacts'),
    path('gallery/', gallery, name='gallery'),
    path('contactform/', contactform, name='contactform')
]



