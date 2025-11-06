from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from .views import home, register_page, login_page, profile_page, RegisterView, AddUserInfoView, ListUserInfoView
from rest_framework_simplejwt.views import TokenObtainPairView

urlpatterns = [
    # HTML pages
    path('', home),
    path('register/', register_page),
    path('login/', login_page),
    path('profile/', profile_page),

    # API
    path('api/register/', csrf_exempt(RegisterView.as_view())),
    path('api/login/', csrf_exempt(TokenObtainPairView.as_view())),
    path('api/userinfo/add/', csrf_exempt(AddUserInfoView.as_view())),
    path('api/userinfo/list/', ListUserInfoView.as_view()),
]
