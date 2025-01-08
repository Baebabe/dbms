from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_view, name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('register/', views.register, name='register'),
    path('accounts/profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.admin_dashboard, name='dashboard'),
    path('user/edit/<int:id>/', views.admin_user_edit, name='admin_user_edit'),
]

