from django.urls import path, include
from . import views

app_name="images"

urlpatterns = [
    path('', views.feed.as_view(), name='feed'),
    path('<int:image_id>/like/',views.LikeImage.as_view(), name='like_image'),
    path('<int:image_id>/unlike/',views.UnLikeImage.as_view(), name='like_image'),
    path('<int:image_id>/comments/', views.CommentOnImage.as_view(), name='comment_image'),
    path('comments/<int:comment_id>/' ,views.Comment.as_view(), name = 'comment')
]