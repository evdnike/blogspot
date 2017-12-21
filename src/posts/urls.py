from django.conf.urls import url
from posts import views

urlpatterns = [
    url(r'^$', views.show_posts, name='posts'),
    url(r'^about/$', views.about, name='about'),
    url(r'^post/(?P<id>\d+)/$', views.get_post, name='post'),
    url(r'^createpost/$', views.create_post, name='create_post'),
    url(r'^post/add/(?P<id>\d+)/$', views.add_comment, name='add_comment'),
    url(r'^page/(\d+)/$', views.show_posts),
    url(r'^post/(?P<id>\d+)/page/(?P<number>\d+)/$', views.get_post)
    
]