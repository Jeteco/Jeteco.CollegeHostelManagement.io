"""college_solution URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from college import views
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home , name='home'),
    path('showdata/<int:pro_id>', showdata),
    path('signup', views.signup, name='signup'),
    # path('comment_show', views.comment_show, name='comment_show'),
    path('loginup', views.loginup, name='loginup'),
    path('logoutup', views.logoutup, name='logoutup'),
    path('contact', views.contact, name='contact'),
    path('student', views.student, name='student'),
    path('details', views.details, name='details'),
    path('hostel', views.hostel, name='hostel'),
    path('messup', views.messup, name='messup'),
    path('need', views.need, name='need'),
    path('index', views.index, name='index'),
    path('entry', views.entry, name='entry'),
    path('detail_update/<int:pro_id>',detail_update),

    # path('addstud', views.addstud, name='addstud'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
