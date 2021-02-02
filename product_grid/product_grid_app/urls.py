"""product_grid URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('products/<int:product_id>', views.product_desc, name="product_desc"),
    path('products/<int:product_id>/edit/', views.product_edit, name="product_edit"),
    path('edit_product', views.edit_product),
    path('products/<int:product_id>/delete/', views.product_delete, name="product_delete"),
    path('products/new', views.product_add, name="product_add"),
    path('add_a_product', views.add_a_product),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)