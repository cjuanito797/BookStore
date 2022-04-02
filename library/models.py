from django.db import models
from io import BytesIO
from PIL import Image

from django.core.files import File

# Create your models here.
class category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('name', )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'


class Book(models.Model):
    category = models.ForeignKey(category, related_name='Books', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    summary = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    coverArt = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_added', )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.category.slug}/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url

    def get_cover_art(self):
        if self.coverArt:
            return 'http://127.0.0.1:8000' + self.coverArt.url
        else:
            if self.image:
                self.coverArt = self.make_cover_art(self.image)
                self.save()

                return 'http://127.0.0.1:8000' + self.coverArt.url
            else:
                return ''

    def make_cover_art(self, image, size=(300, 200)):
        img = Image.open(image)
        img.convert('RGB')
        img.thumbnail(size)

        thumbs_io = BytesIO()
        img.save(thumbs_io, 'JPEG', quality=85)

        cover_art = File(thumbs_io, name=image.name)
        return cover_art
