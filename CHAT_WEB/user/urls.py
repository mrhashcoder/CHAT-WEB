from django.urls import path,include
from django.contrib.auth import views as auth_views
from user import views
from chatdata import urls

urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name="user/login.html"), name='login'),
    path('signup/',views.signup,name ='signup'),
    path('logout/',views.log_out,name = 'logout'),
    path('',include(urls))
]
