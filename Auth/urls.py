from django.urls import path
from .views import RegisterView, LoginView, LogoutView, RetrieveView,UpdateView,DeleteView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('list/', RetrieveView.as_view(), name='retrieve'),
    path('update/<int:pk>/', UpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', DeleteView.as_view(), name='delete')
]
