from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.regView,name='reg'),
    path("regdata/",views.regData,name='regdata'),
    path("loginpage/",views.loginView,name='loginpage'),
    path("logindata/",views.loginData,name='logindata'),
    path("about/",views.about , name='about'),
    path("service/",views.service, name='service'),
    path("contact/",views.contact, name='contact'),
]
