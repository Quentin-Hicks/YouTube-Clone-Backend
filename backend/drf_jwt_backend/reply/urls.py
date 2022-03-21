from django.urls import path, include
from reply import views

urlpatterns = [
    path('', views.user_reply)
]