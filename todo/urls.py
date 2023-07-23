from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import *

router =DefaultRouter()
router.register('user',Show_User)
router.register('todos',Show_Todo)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('auth/', include("rest_framework.urls")),
]
