from django.urls import path, include
from comment import views

urlpatterns = [
    path('all/', views.comments_list),
    path('<int:pk>/', views.user_comments)
]