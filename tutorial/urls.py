from django.urls import path, include
from rest_framework.routers import DefaultRouter
#from tutorial.quickstart import views
from .quickstart.views import InvoiceViewSet, InvoiceDetailViewSet

router = DefaultRouter()
router.register(r'invoices', InvoiceViewSet)
router.register(r'invoicedetails', InvoiceDetailViewSet)

urlpatterns = [
    path('', include(router.urls)),
]