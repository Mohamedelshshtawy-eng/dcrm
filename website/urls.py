from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    # path('',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.regiser_user,name='regiser')
]