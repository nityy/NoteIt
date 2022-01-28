from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.


class Note(models.Model):
    title = models.CharField(max_length=100, validators=[
                             MinLengthValidator(2, "Title must be longer than 1 character")])
    body = models.CharField(max_length=1000)

    def __str__(self):
        return self.title
