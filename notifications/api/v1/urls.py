from django.urls import path

from notifications.api.v1 import views

app_name = 'notifications'

list_create = {'get': 'list', 'post': 'create'}
retrieve_update_delete = {'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}

urlpatterns = [
    path('messages/', views.MessageViewSet.as_view(list_create), name="list-create-message"),
    path('messages/<int:pk>/', views.MessageViewSet.as_view(retrieve_update_delete)),
    path('customers/', views.CustomerViewSet.as_view(list_create), name="list-create-customers"),
    path('customers/<int:pk>/', views.CustomerViewSet.as_view(retrieve_update_delete)),
    path('groups/', views.GroupViewSet.as_view(list_create)),
    path('groups/<int:pk>/', views.GroupViewSet.as_view(retrieve_update_delete)),
    path('devices/', views.DeviceViewSet.as_view(list_create)),
    path('devices/<int:pk>/', views.DeviceViewSet.as_view(retrieve_update_delete)),
    path('notifications/', views.NotificationViewSet.as_view(list_create), name="list-create-notification"),
    path('notifications/<int:pk>/', views.NotificationViewSet.as_view(retrieve_update_delete)),
]
