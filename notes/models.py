from django.db import models
from django.core.validators import MinLengthValidator, URLValidator
from django.urls import reverse_lazy


class Note(models.Model):
    title = models.CharField(max_length=100, validators=[
                             MinLengthValidator(2, "Title must be longer than 1 character")], help_text="Enter title of the note")
    body = models.CharField(
        max_length=1000, help_text="Enter body of the note")
    link = models.URLField(
        blank=True, validators=[URLValidator(schemes=['http', 'https'])], error_messages={'invalid': 'URL must start with http or https'}, help_text="Enter an optional URL beginning with http or https")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse_lazy('notes:detail', args=[self.pk])
