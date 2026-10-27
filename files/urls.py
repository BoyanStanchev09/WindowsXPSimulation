from django.urls import path

from files.views import FileView

urlpatterns = [
    path('<slug:slug>/', FileView.as_view(), name='file_view'),
]
