from django.contrib import admin
from django.urls import path, register_converter
from popularpeople import views
from popularpeople.converters import FourDigitYearConverter

register_converter(FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('addpage/', views.addpage, name='add_page'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.login, name='login'),
    path('post/<int:post_id>/', views.show_post, name='post'),
]

# Custom 404 error handler
handler404 = 'popularpeople.views.page_not_found'

