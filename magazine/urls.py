from django.conf.urls import url
from magazine.views import (base_view,
                            category_view,
                            product_view,
                            cart_view,
                            add_to_cart_veiw,
                            remove_from_cart_veiw,
                            change_item_qty, checkout_view, order_create_view)
urlpatterns = [
    url(r'^$', base_view, name = 'base'),
    url(r'^category/(?P<category_slug>[-\w]+)/$',category_view, name = 'category_detail'),
    url(r'^product/(?P<product_slug>[-\w]+)/$',product_view, name = 'product_detail'),
    url(r'^cart/$', cart_view, name = 'cart'),
    url(r'^add_to_cart/$', add_to_cart_veiw, name='add_to_cart'),
    url(r'^remove_from_cart/$', remove_from_cart_veiw, name ='remove_from_cart'),
    url(r'^change_item_qty/$', change_item_qty, name='change_item_qty'),
    url(r'^chechout/$', checkout_view, name='checkout'),
    url(r'^order/$', order_create_view, name='create_order')

]