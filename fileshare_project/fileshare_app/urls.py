
from django.urls import path
from .views import upload_file, file_list, file_share,upload_success,download_file

urlpatterns = [
    path('upload/', upload_file, name='file_upload'),
    path('list/', file_list, name='file_list'),
    path('share/<int:file_id>/', file_share, name='file_share'),

    # path('upload/', upload_file, name='upload_file'),
    path('upload/success/', upload_success, name='upload_success'),
    # path('share/<int:file_id>/', share_file, name='share_file'),
    # path('download/<int:file_id>/', download_file, name='download_file'),
    path('download/<str:filename>/', download_file, name='download_file'),
]