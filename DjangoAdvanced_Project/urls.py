from django.contrib import admin
from django.urls import path, include

from popularpeople import views
from popularpeople.views import page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('popularpeople.urls')),
    path("__debug__/", include("debug_toolbar.urls")),
]


handler404 = page_not_found