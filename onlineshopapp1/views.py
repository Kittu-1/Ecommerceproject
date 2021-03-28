from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied
from rest_framework.filters import SearchFilter,OrderingFilter
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

from onlineshopapp1.models import ProductModel, OrderModel, OrderItemsModel
from onlineshopapp1.serializers import ProductSerializer, OrderSerializer, OrderItemsSerializer


class Products_List(viewsets.ReadOnlyModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer
    search_fields = ['id', 'Title']
    filter_backends = (SearchFilter, OrderingFilter)
    # permission_classes = ('AllowAny')

class Product_Details(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

class IsAuthorized(permissions.BasePermission):

    def has_object_permission(self, request, view, object):
        return object.User == request.User

class Orders_List(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = (IsAuthorized,)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return OrderModel.objects.filter(user=user)
        raise PermissionDenied()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class Orders_Details(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = (IsAuthorized,)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return OrderModel.objects.filter(user=user)
        raise PermissionDenied()

    def perform_create(self, serializer):
        serializer.save(User=self.request.user)


class ListOfOrderItems(viewsets.ReadOnlyModelViewSet):
    serializer_class = OrderItemsSerializer
    permission_classes = (IsAuthorized,)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return OrderItemsModel.objects.filter(user=user)
        raise PermissionDenied()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class DetailsOfOrderItems(viewsets.ModelViewSet):
    serializer_class = OrderItemsSerializer
    permission_classes = (IsAuthorized,)

    def get_queryset(self):
        user = self.request.user
        if user.is_authenticated:
            return OrderItemsModel.objects.filter(user=user)
        raise PermissionDenied()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)