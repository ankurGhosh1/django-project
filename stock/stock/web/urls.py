from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import logout


urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('signup-auth/', views.signupAuth, name="signup"),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('endpoint/', views.stockapi, name="stockapi"),
    path('profile/', views.profile, name="profile"),
    path('watchlist/', views.watchlist, name="watchlist"),
    path('upload/', views.upload, name="upload"),
    path('<slug:searchText>/', views.stock, name='stock')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)