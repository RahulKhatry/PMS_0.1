from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from Employee import views
from rest_framework import routers
from Employee.views import EmployeeList

urlpatterns = [
    # Examples:
    # url(r'^$', 'CreateEmployee.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
        url(r'^Employees/', include('Employee.urls')),
        url(r'^records/', include('Records.urls')),
        #url(r'^/id$', include('rest_framework.urls', namespace = 'rest_framework'))
   
]

