from django.db import models



class Music(models.Model):
    
    title = models.CharField(
        verbose_name="عنوان",
        max_length=200,
        unique=True
    )
    
    slug = models.SlugField(
        verbose_name="اسلاگ",
        max_length=200,
        unique=True
    )
    artist = models.CharField(
        verbose_name="آرتیست",
        max_length=200
    )
    
    Composer = models.CharField(
        verbose_name="آهنگساز",
        max_length=200
    )
    
    Songwriter = models.CharField(
        verbose_name="ترانه سرا",
        max_length=200
    )
    
    Regulators = models.CharField(
        verbose_name="تنظیم کننده",
        max_length=200
    )
    
    image = models.ImageField(
        upload_to="Musices/files/images",
        verbose_name="تصویر موزیک"
    )
    
    banner = models.ImageField(
        upload_to="Musices/files/banner",
        verbose_name="بنر موزیک"
    )
    
    music_file = models.FileField(
        upload_to="Musices/files/mp3",
        verbose_name="فایل موزیک"
    )
    
    text = models.TextField(
        verbose_name="متن"
    )

    release_date = models.DateField(
        verbose_name="تاریخ اکران"
    )

    likes = models.IntegerField(
        verbose_name="لایک ها",
        default=0
    )
    
    music_time = models.CharField(
        verbose_name="زمان موزیک",
        max_length=20,
    )
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['release_date']
        verbose_name = "موزیک"
        verbose_name_plural = "موزیک ها"
        
    def __str__(self):
        return f'{self.title} از {self.artist}'