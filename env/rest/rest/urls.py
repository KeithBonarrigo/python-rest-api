from django.contrib import admin
from django.conf.urls import include, url
from rest_framework import routers
from restapp.views import TaskViewSet
from restapp import views

#router = routers.DefaultRouter()
router = routers.SimpleRouter()
router.register(r'task', TaskViewSet)
router.register(r'completed_task', views.CompletedViewSet)
router.register(r'due_task', views.DueTaskViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^admin/', admin.site.urls),
]