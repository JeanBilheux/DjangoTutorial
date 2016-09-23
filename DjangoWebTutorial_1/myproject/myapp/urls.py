from django.conf.urls import include, url

from .views import hello, viewArticle, viewArticles

urlpatterns = [
    url(r'^hello/', hello, name='hello'),
    url(r'^article/(?P<articleID>[\d]+)/$', viewArticle, name='article'),
    url(r'^articles/(?P<month>\d{2})/(?P<year>\d{4})', viewArticles, name='articles'),
]
