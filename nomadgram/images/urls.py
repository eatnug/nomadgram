from django.urls import path, include
from . import views
app_name="images"

urlpatterns = [
    path('images/',views.ListAllImages.as_view(), name='all_images'),
    path('comments/', views.ListAllComments.as_view(), name='all_comments'),
    path('likes/', views.ListAllLikes.as_view(), name='all_likes')
]