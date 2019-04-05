from . import views
from django.urls import path


urlpatterns = [
    path('home/', views.home, name='home'),
    path('login/', views.login_user, name='login'),
    path('signup/', views.signup_user, name='signup'),
    path('details/', views.details, name='details'),
    path('logout/', views.logout_user, name='logout'),

]