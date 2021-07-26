from Invoice.serializers import InvoiceSerializer
from django.shortcuts import render, redirect
from .form import InvoiceForm
from .models import Invoice
from rest_framework import viewsets
from rest_framework.response import Response

# Create your views here.


class InvoiceViewSet(viewsets.ModelViewSet):

    serializer_class = InvoiceSerializer
    queryset = Invoice.objects.all().order_by("-created_at")
    http_method_names = ["get", "post", "delete", "put"]

    def create(self, request, *args, **kwargs):
        if request.data.get('id'):
            return super(InvoiceViewSet, self).update(request, *args, **kwargs)
        else:
            return super(InvoiceViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, pk=None):
        queryset = Invoice.objects.get(pk=pk)
        return Response(queryset)

    def invoice_view(request):
        context = {}
        form_invoice = InvoiceForm(request.POST, request.FILES)

        if form_invoice.is_valid():
            form_invoice.save(request.POST)
            return redirect('/invoice')
        else:
            form_invoice = InvoiceForm()

        context['form_invoice'] = form_invoice
        return render(request, "Invoice/index.html", context)
