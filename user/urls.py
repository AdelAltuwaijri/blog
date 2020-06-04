from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from user import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [ 
    path('registration/',views.user_registration,name='registration'),
    path('login/',views.user_login,name='login'),
    path('logout/',views.user_logout,name='logout'),
    path('profile/',views.profile,name='profile'),
    path('profile_update/',views.profile_update,name='profile_update'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)