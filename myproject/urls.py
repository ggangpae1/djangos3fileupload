from django.contrib import admin
from django.urls import path


from fileupload import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('fileupload/', views.fileUpload, name="fileupload"),
    path('', views.main, name="main")
]
