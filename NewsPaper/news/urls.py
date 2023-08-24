from django.urls import path
from .views import PostList, PostDetail # importing the view which created

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
]