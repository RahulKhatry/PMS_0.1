from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from Employee import views
from views import EmployeeList, EmployeeDetail

urlpatterns = [
    # Examples:
    # url(r'^$', 'CreateEmployee.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^api/$', views.EmployeeList.as_view()),
    url(r'^api/(?P<pk>[0-9]+)/$', views.EmployeeDetail.as_view()),

    ]

urlpatterns = format_suffix_patterns(urlpatterns, allowed=['json', 'html'])