"""Rest_Api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import store.views
import store.api_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', store.views.index, name="list-products"),
    path('cart', store.views.cart, name="shopping-cart"),
    path('products/<int:id>', store.views.show, name='show-product'),

    path('api/products', store.api_views.ProductList.as_view()),
    path('api/products/new', store.api_views.ProductCreate.as_view()),
    path('api/products/<int:id>/destroy', store.api_views.ProductDestroy.as_view()),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
