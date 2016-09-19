from django.conf.urls import include, url

from .views import hello, viewArticle

urlpatterns = [
    url(r'^hello/', hello, name='hello'),
    url(r'^articles/(?P<articleID>[\d]+)/', viewArticle, name='article_id'),
]
