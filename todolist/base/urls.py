from django.urls import path,include
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.taskList,name="taskList"),
    path('updateTask/<str:pk>/',views.updateTask,name="updateTask"),
    path('delete/<str:pk>/',views.deleteTask,name="delete"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)