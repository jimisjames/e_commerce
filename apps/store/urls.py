from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^practice$', views.practice),
    url(r'^$', views.home),
    url(r'^cart$', views.cart),
    url(r'^reg$', views.reg),
    url(r'^clear$', views.clear),
    url(r'^email$', views.email),
    url(r'^admin$', views.admin),
    url(r'^contact$', views.contact),
    url(r'^checkout$', views.checkout),
    url(r'^products$', views.products),
    url(r'^products/(?P<search>.+)$', views.products),
    url(r'^login_page$', views.login_page),
    url(r'^login$', views.login),
    url(r'^login/(?P<checkout>.+)$', views.login),
    url(r'^status/(?P<order_id>.+)$', views.status),
    url(r'^logout$', views.logout),
    url(r'^add_to_cart/(?P<id>\d+)$', views.add_to_cart),
    url(r'^item_page/(?P<id>\d+)$', views.item_page),
    url(r'^new_product/$', views.new_product),
    url(r'^new_product/(?P<id>\d+)$', views.new_product),
    url(r'^remove/(?P<id>\d+)$', views.remove),
    url(r'^remove/item/(?P<id>\d+)$', views.remove_item),
    url(r'^view/(?P<id>\d+)$', views.view),
    url(r'^view/order/(?P<order_id>.+)$', views.view_order),
    url(r'^edit/(?P<id>\d+)$', views.edit),
    url(r'^level/(?P<id>\d+)$', views.level),
    url(r'^in_stock/(?P<id>\d+)$', views.in_stock),
    url(r'^new_photo/(?P<id>\d+)$', views.new_photo),
    url(r'^delete/product/(?P<id>\d+)$', views.delete_product),
    url(r'^delete/order/(?P<order_id>.+)$', views.delete_order),
    url(r'^delete/photo/(?P<id>\d+)/(?P<product_id>\d+)$', views.delete_photo),
    
]
