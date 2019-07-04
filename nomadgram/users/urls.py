from django.urls import path
from . import views


app_name = "users"
urlpatterns = [
    path('explore/', views.ExploreUser.as_view(), name= 'explore_users')
]
