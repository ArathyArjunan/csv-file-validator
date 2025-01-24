from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import FileUploadViewset

router = DefaultRouter(trailing_slash=True)
router.register("file-upload",FileUploadViewset,basename="csv-uplod")
urlpatterns = [
    
]+router.urls
