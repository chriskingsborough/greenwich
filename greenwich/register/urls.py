from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^', views.register, 'register/registration.html'),
    url(r'create_account', views.create_account, name='create_account')
]