from django.db import models

class Genre(models.Model):
    
    genre = models.CharField(
        verbose_name= "ژانر",
        max_length=200,
        unique=True
    )
    
    slug = models.SlugField(
        verbose_name= "اسلاگ",
        max_length=200,
        unique=True
    )
    
    image = models.ImageField(
        upload_to="Genres/images/",
        verbose_name="تصویر"
    )
    
    class Meta:
        ordering = ['genre']
        verbose_name = "ژانر"
        verbose_name_plural = "ژانر ها"

    
    def __str__(self):
        return self.genre
    
    
    def get_absolute_url(self):
        return reverse("genre_detail", kwargs={"slug": self.slug})
    