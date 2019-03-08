from django.urls import path

from . import views

urlpatterns = [
	path('status/', views.statusView, name='status'),
	path('status/<str:node>/', views.nodeStatusView, name='nodeStatus'),
	path('getStorageService/<str:uuid>/', views.getStorageService, name='getStorageService'),
	path('uploadPhoto/', views.uploadPhoto, name='uploadPhoto'),
]
