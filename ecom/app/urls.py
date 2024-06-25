from app import views
from django.urls import path

urlpatterns = [
    path('', views.home , name="home"),
    path('changepass', views.changepass , name="changepass"),
    path('profile', views.profile , name="profile"),
    path('home', views.home , name="home"),
    path('login', views.loginpage , name="login"),
    path('signup', views.signup , name="signup"),
    path('logout', views.logoutpage , name="logout"),
    path('aboutus', views.aboutus , name="aboutus"),
    path('upd_prof', views.upd_prof , name="upd_prof"),
    path('courses', views.courses, name="courses"),
    path('contact', views.contact, name="contact"),
]