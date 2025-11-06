from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, permissions
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import RegisterSerializer, UserSerializer, PostSerializer, UserInfoSerializer
from .models import Post, UserInfo
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import redirect

def home(request):
    return redirect('/login/')

def register_page(request):
    return render(request, 'api/register.html')

def login_page(request):
    return render(request, 'api/login.html')

def profile_page(request):
    return render(request, 'api/profile.html')


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

class AddUserInfoView(generics.CreateAPIView):
    serializer_class = UserInfoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ListUserInfoView(generics.ListAPIView):
    serializer_class = UserInfoSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return UserInfo.objects.filter(user=self.request.user).order_by('-created_at')

