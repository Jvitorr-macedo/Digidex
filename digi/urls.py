from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import (
    RegisterViewCreate,
    LoginView,
    DigiList,
    DigiCreate,
    DigiUpdate,
    DigiDetail,
    DigiDelete
)

app_name = 'digi'

urlpatterns = [
    path('', DigiList.as_view(), name='home'),
    path('register/', RegisterViewCreate.as_view(), name='register'),
    path('login/', LoginView.as_view(template_name='auth/login.html'), name='login'),
    path('create/', DigiCreate.as_view(), name='create'),
    path('update/<int:pk>/', DigiUpdate.as_view(), name='update'),
    path('detail/<int:pk>/', DigiDetail.as_view(), name='detail'),
    path('delete/<int:pk>/', DigiDelete.as_view(), name='delete'),
]
