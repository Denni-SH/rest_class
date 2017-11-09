from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from rest_framework_swagger.views import get_swagger_view

from . import views

router = DefaultRouter()
router.register(r'products',views.ProductViewSet)
router.register(r'categories',views.CategoryViewSet)
schema_view = get_swagger_view(title = "API Doc")

urlpatterns = [
    # url(r'^products/$', views.ProductCreateAPIView.as_view()),
    # url(r'^products/create/$', views.ProductCreateAPIView.as_view()),
    # url(r'^products/(?P<pk>\d+)/$', views.ProductUpdateAPIView.as_view()),
    # url(r'^categories/(?P<pk>\d+)/$', views.CategoryUpdateAPIView.as_view()),
    # url(r'^categories/$', views.CategoryCreateAPIView.as_view()),
    url(r'^api/', include(router.urls)),
    url(r'^doc/', schema_view),

]
