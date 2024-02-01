from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate, login, logout
from .serializers import UserSerializer
from .serializers import LoginSerializer
from rest_framework import generics
from django.contrib.auth.models import User


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'detail': 'Registration successful.'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return Response({'detail': 'Login successful.'}, status=status.HTTP_200_OK)
            else:
                return Response({'detail': 'Invalid login credentials.'}, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        logout(request)
        return Response({'detail': 'Logout successful.'}, status=status.HTTP_200_OK)

class RetrieveView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UpdateView(generics.RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class DeleteView(generics.DestroyAPIView):  # Change from RetrieveUpdateAPIView to DestroyAPIView
    queryset = User.objects.all()
    serializer_class = UserSerializer
