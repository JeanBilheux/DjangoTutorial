"""readit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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

from .views import list_books, AuthorList, BookDetail, AuthorDetail

urlpatterns = [
    url(r'^authors/$', AuthorList.as_view(), name='authors'),
    url(r'^authors/(?P<pk>[/w/-]+)', AuthorDetail.as_view(), name='author-detail'),
    url(r'^books/(?P<pk>[\w\-]+)', BookDetail.as_view(), name='book-detail'),
    url(r'^books/$', list_books, name='books_url'),
    ]   
