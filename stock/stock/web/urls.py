from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signup-auth/', views.signupAuth, name="signup"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name="profile"),
    path('<slug:searchText>/', views.stock, name='stock')
]