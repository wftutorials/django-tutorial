from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views

urlpatterns = [
    path('', views.hello, name="hello"),
    path('list/', views.list, name="emp_list"),
    path('create/', views.create, name="emp_create"),
    path('update/<id>/', views.update, name="emp_update"),
    path('view/', views.view, name="emp_view"),
    path('help/', views.help, name="emp_help"),
    path('api/', views.api, name="emp_api"),
    path('welcome/', views.welcome, name="emp_welcome"),
    path('faq/', views.faq, name="emp_faq"),
    path('help/', views.help, name="emp_help"),
    path('save/',views.saveemployee, name="emp_save"),
    path('display/', views.display, name="emp_display"),
    path('remove/', views.remove, name="emp_remove"),
    path('update/', views.update, name="emp_update"),
    path('login/',LoginView.as_view(template_name="employees/login.html"),name="emp_login"),
    path('logout/',views.logout_view,name="emp_logout"),
    
]