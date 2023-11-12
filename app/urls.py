from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'vhosts', views.VhostViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'permissions', views.PermissionViewSet)
router.register(r'queues', views.QueueViewSet)
router.register(r'exchanges', views.ExchangeViewSet)
router.register(r'bindings', views.BindingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('generator/', views.schema_generator, name='generator'),
]

