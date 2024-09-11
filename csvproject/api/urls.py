from django.urls import path
from .views import upload_csv
app_name = "api"
urlpatterns = [
    path("", upload_csv, name='upload_csv'),
]
