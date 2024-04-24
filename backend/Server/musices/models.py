from django.db import models



class Music(models.Model):
    
    name = models.CharField(
        verbose_name="نام",
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

    class Meta:
        ordering = ['release_date']
        verbose_name = "کاربر"
        verbose_name_plural = "کاربر ها"
        