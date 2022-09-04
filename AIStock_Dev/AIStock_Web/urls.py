from django.urls import path, include
from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'AIStock_Web'
urlpatterns = [
    # path('', views.common_view, name='common_view'),
    path('admin/', admin.site.urls),
    path('', views.test, name='test'),

]