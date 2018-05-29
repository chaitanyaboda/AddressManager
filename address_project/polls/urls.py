from django.conf.urls import url
from django.urls import path
from rest_framework.documentation import include_docs_urls
from . import views

# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [

    path('', views.index, name='index'),
    url(r'^company/?$', views.company_list),  # get and post for create and fetch list
    url(r'^pincode/(?P<min_count>[0-9]+)$', views.pincode_list),  # get postal codes with more than min_count companies
    url(r'^company/(?P<name>[a-zA-Z0-9]+)$', views.company_detail),
    url(r'^docs/', include_docs_urls(title='AddresStorage'))
]
