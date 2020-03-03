from django.urls import path

from . import views
app_name = 'qfauth'
urlpatterns = [
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('register/',views.register_view,name='register'),
    path('img_captcha/',views.img_captcha,name='img_captcha'),
    path('cache/',views.cache_test,name='cache'),
]