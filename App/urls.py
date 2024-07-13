from django.urls import path
from .views import image_upload_view, dashboard
app_name = "App"
urlpatterns = [
    path('predict/', image_upload_view, name='image_upload'),
    path('', dashboard, name='dashboard'),
    
]