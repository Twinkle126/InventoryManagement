from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.template.loader import get_template
from django.forms import modelformset_factory
from django.views.generic.base import TemplateView
from Invoice.form import InvoiceForm
from xhtml2pdf import pisa
from django.views.generic import View, ListView
from .models import Item
from .form import ItemForm
from io import BytesIO
from rest_framework import viewsets
from .serializers import ProductSerializer
from rest_framework.response import Response

# Create your views here.
class ItemViewSet(viewsets.ModelViewSet):

    serializer_class = ProductSerializer
    queryset = Item.objects.all().order_by("-created_at")
    http_method_names = ["get", "post", "delete", "put"]

    def create(self, request, *args, **kwargs):
        import ipdb

        ipdb.set_trace()
        if request.data.get('id'):
            return super(ItemViewSet, self).update(request, *args, **kwargs)
        else:
            return super(ItemViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


def product_view(request):
    return render(request, "Product/index.html")

    # context = {}
    # invoice = InvoiceForm(request.POST)
    # if invoice.is_valid():
    #     invoice.save()
    # # creating a formset
    # ItemFormSet = modelformset_factory(
    #     ItemForm,
    #     fields=("product_name", "quantity", "base_price", "tax", "invoice", "amount"),
    #     extra=1,
    # )
    # formset = ItemFormSet(request.POST)

    # if formset.is_valid():
    #     formset.save()

    # new_orders = []
    # for order_form in formset:
    #     print("Item", order_form)
    #     order = Item(
    #         invoice=invoice,
    #     )
    # new_orders.append(order)

    # Item.objects.bulk_create(new_orders)
    # ============
    # check if form data is valid
    # form = ItemForm(request.POST, request.FILES)

    # if form.is_valid():
    #     cleanform = form.save(commit=False)
    #     cleanform.save()
    #     return redirect('invoice')

    # else:
    #     form = ItemForm()

    # context['form'] = form


class ProductListView(ListView):
    model = Item
    template_name = 'Product/product_list.html'


class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        # context = {
        #     "seller": ,
        #     "buyer": ,
        #     "product": ,
        # }
        pdf = render_to_pdf('main_invoice.html')
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = "Invoice_%s.pdf" % ("12341231")
            content = "inline; filename='%s'" % (filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename='%s'" % (filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def product_render_pdf_view(request, *args, **kwargs):
    pk = kwargs.get('pk')
    item = get_object_or_404(Item, pk=pk)
    print(item.invoice.seller)
    context = {
        "seller": item.invoice.seller,
        "buyer": item.invoice.buyer,
        "product": item,
    }
    pdf = render_to_pdf('main_invoice.html', context)
    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        filename = "Invoice_%s.pdf" % ("12341231")
        content = "inline; filename='%s'" % (filename)
        download = request.GET.get("download")
        if download:
            content = "attachment; filename='%s'" % (filename)
        response['Content-Disposition'] = content
        return response
    return HttpResponse("Not found")
