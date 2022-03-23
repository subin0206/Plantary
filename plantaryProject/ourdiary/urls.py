from django.urls import path
from django.conf.urls import url
from .import views, forms


urlpatterns = [
    path('ourdiary/', views.ourdiary, name = 'ourdiary'),
    path('<int:ourdiary_id>/',views.detail, name="detail"),
    path('like/', views.post_like, name="post_like"),

    url(r'^(?P<pk>\d+)/comment/$', views.add_comment, name='add_comment'),
    url(r'^(?P<id>\d+)/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^(?P<id>\d+)/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
#git
    path('new/', views.new, name = 'new'),
    path('create/',views.create, name = 'create'),
    path('mylist/',views.mylist, name = 'mylist'),
    path('<int:ourdiary_id>/update',views.update, name = 'update'),
    path('<int:ourdiary_id>/delete',views.delete, name = 'delete'),
    
]