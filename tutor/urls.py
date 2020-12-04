from django.contrib import admin
from django.urls import path, include
from profiles.views import (home_view)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('',home_view),
    path('admin/', admin.site.urls),
    path('api/profiles/', include('profiles.api.urls')),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/', include('rest_framework.urls')),
    path('register/', include('jwtauth.urls'), name='jwtauth'),
    
]
