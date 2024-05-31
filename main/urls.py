from django.contrib import admin
from django.urls import path,include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.utils.text import slugify
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('home', views.home,name='home'),
    path('', views.first,name='first'),
    path('register/',views.register,name='register'),
    path('login/',views.login_view,name='login'),
    path('logout_view/', views.logout_view,name='logout_view'),
    path('ft', views.followtopic,name='followtopic'),
    # path('o', views.o,name='o'),
    # path('a', views.a,name='a'),
    path('first', views.first,name='first'),
    path('explore/', views.explore,name='explore'),
    path('notifications', views.notifications,name='notifications'),
    path('profile/<slug:username>/', views.profile_view,name='profile'),
    path('search/<slug:username>/', views.search,name='search'),
    path('savepost', views.savepost,name='savepost'),
    # path('follow', views.follow,name='follow'),
    # path('search/demo/follow', views.follow, name='follow'),
    path('follow/<str:username>/', views.follow_user, name='follow_user'),
    path('unfollow/<str:username>/', views.unfollow_user, name='unfollow_user'),
    path('editprofile/', views.editprofile, name='editprofile'),
    path('register/', views.register, name='register'),
    path('message/', views.message, name='message'),
    path('delete_post/<int:post_id>/', views.delete_post, name='delete_post'),



    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)