from django.urls import path
from .views import EmployeeAPIView, DetailAPIView, EmployeeListCreateView, apifunc
from rest_framework.authtoken.views import obtain_auth_token #inbuilt authtoken package
from django.conf import settings
from django.conf.urls.static import static

app_name='employee_data'
urlpatterns = [
    path('', EmployeeAPIView.as_view(), name='list'), 
    path('authtoken/', obtain_auth_token, name='token'), #in-built authtoken package url

    # path('emp_detail/<int:pk>', employee_detail, name='detail'),
    # path('detail/', request_data, name='detail'),
    path('emp_detail/<int:id>', DetailAPIView.as_view(), name='detail'),
    path('emplist_create/', EmployeeListCreateView.as_view(), name='list-create'),
    path('api', apifunc, name='api')
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
     
