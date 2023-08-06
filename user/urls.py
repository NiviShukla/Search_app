from django.urls import path
from . import views


urlpatterns = [
    path('login/', views.custom_login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]
