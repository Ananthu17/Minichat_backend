from django.urls import path,include
from . import views
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

urlpatterns = [
    path('signup', views.Registerview.as_view()),
    path(r'api-token-auth/', obtain_jwt_token),
    path(r'api-token-refresh/', refresh_jwt_token),
    path('users/', views.UserListView.as_view()),
    path('findchat/',views.ChatRetriveView.as_view())
]