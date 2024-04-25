from django.db import models
from musices.models import Music


class Albom(models.Model):
    title = models.CharField(
        verbose_name="عنوان آلبوم",
        max_length=200
    )
    
    slug = models.SlugField(
        verbose_name="اسلاگ آلبوم",
        max_length=200
    )
    
    singer = models.CharField(
        verbose_name="خواننده",
        max_length=100
    )
    
    image = models.ImageField(
        upload_to="alboms/files/images/",
        verbose_name="تصویر آلبوم",
    )
    
    banner = models.ImageField(
        upload_to="alboms/files/banners/",
        verbose_name="تصویر آلبوم",
    )
    
    release_date = models.DateField(
        verbose_name="تاریخ اکران"
    )
    
    likes = models.IntegerField(
        verbose_name="تعداد لایک ها"
    )
    
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['release_date', 'created']
        verbose_name = "آلبوم"
        verbose_name_plural = "آلبوم ها"

    def __str__(self):
        return f'آهنگ {self.title} از {self.singer}'

    

class MusicAlbom(models.Model):
    albome = models.ForeignKey(
        Albom,
        on_delete=models.CASCADE,
        related_name="albom_musics",
        verbose_name="آلبوم"
    )
    
    music = models.ForeignKey(
        Music,
        on_delete=models.CASCADE,
        related_name="albom_musics",
        verbose_name="موزیک های آلبوم"
    )
    
    def __str__(self):
        return f'آلبوم {self.music.title} از {self.albome.title}'  