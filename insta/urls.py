from django.urls import path
from . import views
 
urlpatterns = [
    path('', views.feed, name="feed"),
    path('upload/', views.upload, name="upload"),
    path('like/<int:post_id>/', views.like_post, name="like"),
    path('comment/<int:post_id>/', views.comment_post, name="comment"),
    path('profile/<str:username>/', views.profile, name="profile"),
    path('follow/<str:username>/', views.follow_user, name="follow"),
 
    # Auth
    path('login/', views.login_view, name="login"),
    path('logout/', views.logout_view, name="logout"),
    path('register/', views.register, name="register"),
]