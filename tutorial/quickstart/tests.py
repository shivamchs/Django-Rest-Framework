from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Invoice, InvoiceDetail
from .serializers import InvoiceSerializer, InvoiceDetailSerializer
import requests

class InvoiceAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_invoice_and_details(self):
        # Create an invoice
        invoice_data = {'date': '2024-02-18', 'customer_name': 'Test Customer'}
        response = self.client.post('/invoices/', invoice_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Invoice.objects.count(), 1)
        self.assertEqual(Invoice.objects.get().customer_name, 'Test Customer')

        # Create invoice details for the created invoice
        invoice_id = response.data['id']
        
        invoice_detail_data = {'invoice_id': invoice_id, 'description': 'Test Description', 'quantity': 1, 'unit_price': '10.00', 'price': '10.00'}
        response = self.client.post('/invoicedetails/', invoice_detail_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(InvoiceDetail.objects.count(), 1)
        self.assertEqual(InvoiceDetail.objects.get().description, 'Test Description')
        
        