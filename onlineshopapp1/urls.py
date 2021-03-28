from django.urls import path

from onlineshopapp1.views import Products_List, Product_Details,Orders_List, Orders_Details, ListOfOrderItems,DetailsOfOrderItems

urlpatterns = [
    path('products/', Products_List.as_view({'get': 'list'}), name='listofproducts'),
    path('product/<pk>',
         Product_Details.as_view(
             {'get': 'retrieve', 'post': 'create', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='detailsofproducts'),
    path('orders/', Orders_List.as_view({'get': 'list'}), name='listoforders'),
    path('order/<str:pk>',
         Orders_Details.as_view(
             {'get': 'retrieve', 'post': 'create', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='detailsoforders'),
    path('orderproduct/', ListOfOrderItems.as_view({'get': 'list'}), name='orderproductlist'),
    path('orderproduct/<str:pk>',
         DetailsOfOrderItems.as_view(
             {'get': 'retrieve', 'post': 'create', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}),
         name='detailsoforderproducts'),
]