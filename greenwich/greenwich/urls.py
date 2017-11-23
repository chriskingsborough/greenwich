"""greenwich URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from reminder import views as reminder
from index import views as index

urlpatterns = [
    url(r'^$', index.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', index._login, name='login'),
    url(r'^logout/', index.logout),
    url(r'^create_user/', index.create_user),
    url(r'^sign_in/', index.sign_in, name='sign_in'),
    url(r'^create_reminder/', reminder.add_event),
    url(r'^view_reminders/', reminder.view_events),
    url(r'^edit_reminder/', reminder.edit_event),
    url(r'^view_reminder/', reminder.view_reminder),
    url(r'^delete_reminder/', reminder.delete_reminder)
]
