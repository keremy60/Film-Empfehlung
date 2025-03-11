from django.test import TestCase, Client
from django.urls import reverse
from .models import Movie
import os
from django.conf import settings
from unittest.mock import patch

class MovieModelTest(TestCase):
    def test_str_method(self):
        """Testet, ob __str__ den Titel zurückgibt."""
        movie = Movie.objects.create(
            title="Test Movie",
            genre="Action",
            rating=8.5,
            poster_url="https://example.com/test.jpg"
        )
        self.assertEqual(str(movie), "Test Movie")


class MoviesViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        # Erstelle Testfilme in der Testdatenbank
        self.movie_action = Movie.objects.create(
            title="Test Action Movie",
            genre="Action",
            rating=7.5,
            poster_url="https://example.com/action.jpg"
        )
        self.movie_drama = Movie.objects.create(
            title="Test Drama Movie",
            genre="Drama",
            rating=8.0,
            poster_url="https://example.com/drama.jpg"
        )

    def test_get_index(self):
        """
        Testet, ob ein GET-Request an die Startseite (Index) den
        erwarteten Inhalt (z.B. "Filmempfehlungen") zurückgibt.
        """
        # Hier wird angenommen, dass die URL der movies-View "/" ist.
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Filmempfehlungen")

    def test_post_movies_view(self):
        """
        Testet, ob ein POST-Request mit Genre 'Action' nur Actionfilme anzeigt.
        """
        response = self.client.post("/", {"genre": "Action"})
        self.assertEqual(response.status_code, 200)
        # Sollte den Actionfilm enthalten
        self.assertContains(response, "Test Action Movie")
        # Sollte den Drama-Film nicht enthalten
        self.assertNotContains(response, "Test Drama Movie")


class TestStaticFileViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    @patch("os.path.exists")
    def test_static_file_found(self, mock_exists):
        """
        Simuliert, dass die CSS-Datei gefunden wird und prüft die Rückgabe.
        """
        mock_exists.return_value = True
        response = self.client.get("/test_static/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Gefunden:", response.content.decode())

    @patch("os.path.exists")
    def test_static_file_not_found(self, mock_exists):
        """
        Simuliert, dass die CSS-Datei nicht gefunden wird und prüft die Rückgabe.
        """
        mock_exists.return_value = False
        response = self.client.get("/test_static/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("Datei nicht gefunden", response.content.decode())
