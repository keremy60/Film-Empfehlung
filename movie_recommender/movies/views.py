from django.shortcuts import render
from .models import Movie
from django.http import HttpResponse
from django.conf import settings
import os

def movies(request):
    if request.method == "POST":
        genre = request.POST.get("genre")
        movies = Movie.objects.filter(genre__icontains=genre)
        return render(request, "results.html", {"movies": movies, "genre": genre})
    
    return render(request, "index.html")

# verfügbarkeit der css-datei prüfen
def test_static(request):
    file_path = os.path.join(settings.BASE_DIR, 'movies', 'static', 'css', 'style.css')
    if os.path.exists(file_path):
        return HttpResponse(f'Gefunden: {file_path}', content_type="text/plain")
    return HttpResponse('Datei nicht gefunden', content_type="text/plain")