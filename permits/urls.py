from django.urls import path
from . import views

urlpatterns = [
    path('api/permits/', views.permit_response, name='permit_response'),
]
