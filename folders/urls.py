from django.urls import path

from folders.views import FolderView

urlpatterns = [
    path('', FolderView.as_view(), name='folder_root'),
    path('<slug:slug>/', FolderView.as_view(), name='folder_view'),
]
