from django.db import models
from musices.models import Music
from users.models import User
from genres.models import Genre
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse 


class Albom(models.Model):
    
    title = models.CharField(
        verbose_name="عنوان آلبوم",
        max_length=200
    )
    
    slug = models.SlugField(
        verbose_name="اسلاگ آلبوم",
        max_length=200
    )
    
    genre = models.ForeignKey(
        Genre,
        on_delete=models.CASCADE,
        verbose_name="ژانر",
        related_name="albome_genre"
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
    
    def get_absolute_url(self):
        return reverse("albomes:albome_detail", kwargs={"slug": self.slug})

    

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


class Comment(models.Model):
    
    albome = models.ForeignKey(
        Albom,
        on_delete=models.CASCADE,
        related_name="albome_comments",
        verbose_name="آلبوم"
    )
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_albome_comments",
        verbose_name="کاربر"
    )
    
    title = models.CharField(
        verbose_name="عنوان",
        max_length=100
    )
    
    text = models.TextField(
        verbose_name="متن"
    )
    
    score =models.IntegerField(
         default=1,
         verbose_name="امتیاز",
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created']
        verbose_name = "نظر آلبوم"
        verbose_name_plural = "نظرات آلبوم"
    
      
    def __str__(self):
        return f'نظر کاربر:{self.user.username} درمورد آلبوم {self.albome.title} از {self.albome.singer}'
    

class CommentReply(models.Model):
    
    comment = models.ForeignKey(
        Comment,
        on_delete=models.CASCADE,
        related_name="albome_comment_replies",
        verbose_name="نظر"
    )
    
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="user_albome_replies",
        verbose_name="کاربر",
    )
    
    reply = models.TextField(
        verbose_name="پاسخ"
    )
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "پاسخ"
        verbose_name_plural = "پاسخ ها"
        
    
    def __str__(self):
        return f'{self.user.username}--{self.comment.id}'