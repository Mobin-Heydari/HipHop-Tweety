from django.db import models
from django.urls import reverse


class Event(models.Model):
    
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
    
    description = models.TextField(verbose_name="توضیحات")
    
    image = models.ImageField(
        verbose_name="تصویر",
        upload_to="Events/images/"
    )
    
    event_url = models.URLField(
        verbose_name="لینک",
        max_length=200
    )
    
    event_date = models.DateField(
        verbose_name="تاریخ"
    )
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['event_date']
        verbose_name = "اتفاق"
        verbose_name_plural = "اتفاقات"
        
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("events:event_detail", kwargs={"slug": self.slug})
    

class EventSection(models.Model):
    
    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        verbose_name="اتفاق",
        related_name="event_section"
    )
    
    title = models.CharField(
        verbose_name="عنوان",
        max_length=200,
        blank=True,
        null=True
    )

    description = models.TextField(
        verbose_name="توضیحات",
        blank=True,
        null=True
    )
    
    image = models.ImageField(
        verbose_name="تصویر",
        upload_to="Events/Desciption/images/",
        blank=True,
        null=True
    )
    
    video = models.FileField(
        verbose_name="ویدیو",
        upload_to="Events/Desciption/video/",
        blank=True,
        null=True
    )
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "توضیح اتفاق"
        verbose_name_plural = "توضیحات اتفاق"