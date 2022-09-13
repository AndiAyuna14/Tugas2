from django.shortcuts import render
from katalog.models import CatalogItem
# TODO: Create your views here.
def show_catalog(request):
    data_barang_catalog = CatalogItem.objects.all()
    context = {
        'list_katalog' : data_barang_catalog,
        'nama' : "Andi Ayuna Rymang",
        'npm' : "2106637265"
    }
    return render(request, "katalog.html", context)
