"""django_demo_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from bbs import views as bbs_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', bbs_view.index, name='index'),
    path('password_reset/', bbs_view.password_reset, name='password_reset'),
    path('boards_list/', bbs_view.boards_list, name='boards_list'),
    path('boards_list_view/', bbs_view.BoardList.as_view(), name='boards_list_view'),
    path('boards/<pk>/', bbs_view.board_topics, name='board_topics'),
    path('boards/<pk>/new/', bbs_view.new_topic, name='new_topic'),
    path('boards/<pk>/topics/<topic_pk>/',
         bbs_view.topic_posts, name='topic_posts'),
]
