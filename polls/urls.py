from django.conf.urls import url
from . import views


urlpatterns = [
  url(r'^$',views.index,name='home'),
  url(r'^orden/$',views.order,name='orden'),
  url(r'^compra/$',views.orders,name='compra'),



]