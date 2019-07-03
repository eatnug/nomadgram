from django.urls import path, include
from . import views
app_name="images"

urlpatterns = [
    path('all/',views.ListAllImages.as_view(), name='all_images')

]