from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from authApp import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)
router.register(r'tasks', views.TaskView, basename='tasks')

urlpatterns = [
  path('login/', TokenObtainPairView.as_view()),
  path('refresh/', TokenRefreshView.as_view()),
  path('user/', views.UserCreateView.as_view()),
  path('user/<int:pk>/', views.UserDetailView.as_view())
]

urlpatterns += router.urls
