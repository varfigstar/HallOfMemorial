from django.db import models


class ImageURL(models.Model):
    title = models.CharField(max_length=300, null=True)
    image = models.ImageField(upload_to="images", null=True)

    @property
    def url(self):
        return self.image.name

    def __str__(self):
        return self.image.name or ""


class Person(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    person_name = models.CharField(max_length=255)
    person_birth_date = models.DateField(null=True)
    person_arrest_date = models.DateField(null=True)
    person_death_date = models.DateField(null=True)
    mem_book_note = models.TextField(null=True)
    images = models.ManyToManyField(
        ImageURL, related_name="images", blank=True
    )




