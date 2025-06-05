# dictionary_app/models.py

from django.db import models

class SearchLog(models.Model):
    word = models.CharField(max_length=255)
    searched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.word
