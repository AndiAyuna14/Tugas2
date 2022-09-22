from django.shortcuts import render
from mywatchlist.models import MyWatchList

from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    data_movie = MyWatchList.objects.all()
    sudah_ditonton = 0
    belum_ditonton = 0
    for movie in data_movie:
        if movie.watched == "Sudah ditonton":
            sudah_ditonton += 1
        else:
            belum_ditonton += 1
    context = {
        'list_movies': data_movie,
        'nama': "Andi Ayuna Rymang",
        'npm': "2106638265",
        'film_sudah_ditonton':sudah_ditonton,
        'film_belum_ditonton':belum_ditonton,
    }
    return render(request, "mywatchlist.html", context)

def show_json(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml(request):
    data = MyWatchList.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_xml_by_id(request, id):
    data = MyWatchList.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")