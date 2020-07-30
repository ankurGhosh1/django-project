from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signup-auth/', views.signupAuth, name="signup"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name="profile"),
    path('upload/', views.upload, name="upload"),
    path('<slug:searchText>/', views.stock, name='stock')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)