from django.conf.urls import url
from magazine.views import base_view, category_view, product_view, cart_view, add_to_cart_veiw, remove_from_cart_veiw
urlpatterns = [
    url(r'^$', base_view, name = 'base'),
    url(r'^category/(?P<category_slug>[-\w]+)/$',category_view, name = 'category_detail'),
    url(r'^product/(?P<product_slug>[-\w]+)/$',product_view, name = 'product_detail'),
    url(r'^cart/$', cart_view, name = 'cart'),
    url(r'^add_to_cart/(?P<product_slug>[-\w]+)/$', add_to_cart_veiw, name='add_to_cart'),
    url(r'^remove_from_cart/(?P<product_slug>[-\w]+)/$', remove_from_cart_veiw, name ='remove_from_cart'),

]