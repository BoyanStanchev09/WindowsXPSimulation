from django.urls import path

from folders.views import FolderView, ShortCutRedirectView

urlpatterns = [
    path('', FolderView.as_view(), name='folder_root'),
    path('shortcut/<int:pk>/', ShortCutRedirectView.as_view(), name='shortcut'),
    path('<slug:slug>/', FolderView.as_view(), name='folder_view'),
]
