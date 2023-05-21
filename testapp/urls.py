from django.urls import path
from . import views


urlpatterns = [
    path('', views.EmployeeAPIView.as_view(), name='emp'),
    path('<int:id>/', views.EmployeeDetailAPIView.as_view(), name='empdetail'),
]
