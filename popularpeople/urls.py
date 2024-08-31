from django.contrib import admin
from django.urls import path, register_converter


from popularpeople import views
from popularpeople.converters import FourDigitYearConverter
from django.conf import settings
from django.conf.urls.static import static

register_converter(FourDigitYearConverter, "year4")

urlpatterns = [
    path('', views.PeopleHome.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('addpage/', views.AddPage.as_view(), name='add_page'),
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('login/', views.login, name='login'),
    path('post/<slug:post_slug>/', views.ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', views.PeopleCategory.as_view(), name='category'),
    path('tag/<slug:tag_slug>/', views.show_tag_postlist, name='tag')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Custom 404 error handler
handler404 = 'popularpeople.views.page_not_found'

admin.site.site_header = "Admin Panel"
admin.site.index_title = 'Popular People Web Application'
