from django.urls import path, include
from rest_framework import routers
from . import views
from .api import TaskViewSet, RegisterAPI
from .api import RegisterAPI, LoginAPI, UserAPI
from knox import views as knox_views

urlpatterns = [
	path('task-list/', views.taskList, name="task-list"),
	path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
	path('task-create/', views.taskCreate, name="task-create"),
	path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
	path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
	path('api/auth', include('knox.urls')),
	path('api/auth/register', RegisterAPI.as_view()),
	path('api/auth/login', LoginAPI.as_view()),
	path('api/auth/user', UserAPI.as_view()),
	path('api/auth/logout', knox_views.LogoutView.as_view(), name='knox_logout'),
	path('', views.apiOverview, name="api-overview"),
	
]



router = routers.DefaultRouter()
router.register('api/tasks', TaskViewSet, 'tasks')

urlpatterns = router.urls

""" urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('task-list/', views.taskList, name="task-list"),
	path('task-detail/<str:pk>/', views.taskDetail, name="task-detail"),
	path('task-create/', views.taskCreate, name="task-create"),

	path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
	path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
]
 """