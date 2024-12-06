from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductListAPIView, category_list , CategoryListAPIView , CategoryListAPIViewDecorator,ProductListCreateView,  ProductDetailView , ProductListCreateViewDeco,ProductDetailViewDeco , ProductViewSet



# Create a router and register our viewset with it.
router = DefaultRouter()
router.register(r'products', ProductViewSet)

product_list = ProductViewSet.as_view({'get': 'list', 'post': 'create'})
product_detail = ProductViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'})


urlpatterns = [
     path('categories/', category_list, name='category-list'),
    path('api/products/', ProductListAPIView.as_view(), name='product-list-api'),
    path('api/category/', CategoryListAPIView.as_view(), name='Category-list-api'), # For list and POST
    path('api/category/<int:pk>/', CategoryListAPIView.as_view()),  # For detail, PUT, PATCH, DELETE
    path('api/category/deco/', CategoryListAPIViewDecorator),  
    path('api/category/deco/<int:pk>/', CategoryListAPIViewDecorator),  
    path('generic/products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('generic/products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('generic/products/deco/', ProductListCreateViewDeco.as_view(), name='product-listd-deco-create'),
    path('generic/products/deco/<int:pk>/', ProductDetailViewDeco.as_view(), name='product--deco-detail'),
    path('view/', include(router.urls), name='product--viewset--deco-detail'),
    path('view/simple/products/', product_list, name='product-list'),
    path('view/simple/products/<int:pk>/', product_detail, name='product-detail'),



   
]
