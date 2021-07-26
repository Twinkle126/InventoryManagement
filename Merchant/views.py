from Merchant.models import Buyer, Seller
from django.http import HttpResponse
from django.template.loader import get_template
from django.shortcuts import redirect, render
from rest_framework import viewsets
from .serializers import BuyerSerializer, SellerSerializer
from rest_framework.response import Response

# from .form import SellerForm, BuyerForm
from xhtml2pdf import pisa
from django.views.generic import View
from io import BytesIO

# Create your views here.
class BuyerViewSet(viewsets.ModelViewSet):

    serializer_class = BuyerSerializer
    queryset = Buyer.objects.all().order_by("-created_at")
    http_method_names = ["get", "post", "delete", "put"]

    def create(self, request, *args, **kwargs):
        import ipdb

        ipdb.set_trace()
        if request.data.get('id'):
            return super(BuyerViewSet, self).update(request, *args, **kwargs)
        else:
            return super(BuyerViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, pk=None):
        queryset = Buyer.objects.get(pk=pk)
        return Response(queryset)


class SellerViewSet(viewsets.ModelViewSet):

    serializer_class = SellerSerializer
    queryset = Seller.objects.all().order_by("-created_at")
    http_method_names = ["get", "post", "delete", "put"]

    def create(self, request, *args, **kwargs):
        if request.data.get('id'):
            return super(SellerViewSet, self).update(request, *args, **kwargs)
        else:
            return super(SellerViewSet, self).create(request, *args, **kwargs)

    def retrieve(self, request, pk=None):
        queryset = Seller.objects.get(pk=pk)
        return Response(queryset)


class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
        context = {
            "buyer_name": 'Twinkle',
            "buyer_add": "John Cooper, Ghaziabad",
            "buyer_no": 9845676545,
        }
        pdf = render_to_pdf('Buyer/invoice.html', context)
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


def render_pdf_view(request):
    template_path = 'Buyer/main.html'
    context = {'buyer': 'buyer object'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def render_to_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None


def buyer_view(request):
    return render(request, "Buyer/index.html")


def seller_view(request):
    return render(request, "Seller/index.html")


# def buyer_view(request):
#     context = {}
#     form2 = BuyerForm(request.POST)

#     if form2.is_valid():
#         form2.save()
#         # return redirect('/merchant/seller_view')

#     context['form2'] = form2
#     return render(request, "Buyer/index.html", context)


# def seller_view(request):
#     context = {}
#     form3 = SellerForm(request.POST)

#     if form3.is_valid():
#         form3.save()
#         return redirect('/product/product_view')

#     context['form3'] = form3
#     return render(request, "Seller/index.html", context)
