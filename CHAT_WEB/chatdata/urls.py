from django.urls import path,include
from chatdata import views

urlpatterns =[
    path('homepage/',views.homepage,name = 'homepage'),
    path('chatpage/(?P<reciver_id>\w{0,50})/$',views.chatpage, name='chatpage'),
    path('savemesg/(?P<reciver_id>\w{0,50})/$',views.savemesg,name = 'savemesg')
]
