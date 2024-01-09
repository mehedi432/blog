from django.urls import path
from .views import *


urlpatterns = [
    path('', BlogHomeView.as_view(), name='home'),
]