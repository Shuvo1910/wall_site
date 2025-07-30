from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.homepage,name = 'home'),
    path('raw', views.raw_data,name = 'raw'),
    path('login', views.login,name = 'login'),
    path('signup', views.signup,name = 'signup'),
    path('desktop/', views.desktop_page, name='desktop'),
    path('mobile/', views.mobile_page, name='mobile'),
    path('login_auth', views.login_auth,name = 'login_auth'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('index_2', views.index_2, name='index_2'),
    
]