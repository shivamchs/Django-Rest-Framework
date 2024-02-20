from rest_framework import serializers
from .models import Invoice, InvoiceDetail


# serializers.py
from rest_framework import serializers
from .models import Invoice, InvoiceDetail

class InvoiceDetailSerializer(serializers.ModelSerializer):
    # Add invoice_id field to accept invoice ID
    invoice_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = InvoiceDetail
        fields = ['id', 'invoice_id', 'description', 'quantity', 'unit_price', 'price']

    def create(self, validated_data):
        # Pop 'invoice_id' from validated data to associate with InvoiceDetail
        invoice_id = validated_data.pop('invoice_id')
        # Retrieve Invoice object based on provided invoice_id
        invoice = Invoice.objects.get(pk=invoice_id)
        # Create and return InvoiceDetail instance associated with Invoice
        return InvoiceDetail.objects.create(invoice=invoice, **validated_data)




# class InvoiceDetailSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = InvoiceDetail
#         fields = ['id', 'description', 'quantity', 'unit_price', 'price']

class InvoiceSerializer(serializers.ModelSerializer):
    details = InvoiceDetailSerializer(many=True, read_only=True)

    class Meta:
        model = Invoice
        fields = ['id', 'date', 'customer_name', 'details']

    def create(self, validated_data):
        details_data = validated_data.pop('details', [])
        invoice = Invoice.objects.create(**validated_data)
        for detail_data in details_data:
            InvoiceDetail.objects.create(invoice=invoice, **detail_data)
        return invoice
