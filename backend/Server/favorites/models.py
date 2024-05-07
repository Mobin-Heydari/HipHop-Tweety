from django.db import models
from alboms.models import Albom
from musices.models import Music
from users.models import User




class UserFavorite(models.Model):
    
    user = models.ForeignKey(
        User,
        verbose_name="کاربر",
        on_delete=models.CASCADE,
        related_name="user_favorites"
    )
    
    count = models.IntegerField(
        default=0,
        verbose_name="تعداد علاقه مندی ها"
    )
    
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['user']
        verbose_name = "علاقمندی های کاربر"
        verbose_name_plural = "علاقه مندی های کاربران"
        
    
    def __str__(self):
        return f'علاقمندی های کاربر : {self.user.username}'
    


class UserAlbomeFaver(models.Model):
    
    user_favorite = models.ForeignKey(
        UserFavorite,
        on_delete=models.CASCADE,
        verbose_name="علاقمندی های کاربر",
        related_name="user_albome_faver"
    )
    
    
    albome = models.ForeignKey(
        Albom,
        verbose_name="آلبوم",
        on_delete=models.CASCADE,
        related_name="albome_faver"
    )
    
    created = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering = ['created']
        verbose_name = "علاقمندی آلبوم های کاربر"
        verbose_name_plural = "علاقمندی آلبوم های کاربران"
        
    
    def __str__(self):
        return f'{self.albome.title}'


class UserMusicFaver(models.Model):
    
    user_favorite = models.ForeignKey(
        UserFavorite,
        on_delete=models.CASCADE,
        verbose_name="علاقمندی های کاربر",
        related_name="user_music_faver"
    )
    
    music = models.ForeignKey(
        Music,
        verbose_name="آهنگ",
        on_delete=models.CASCADE,
        related_name="music_faver"
    )
    
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created']
        verbose_name = "علاقمندی موزیک های کاربر"
        verbose_name_plural = "علاقمندی موزیک های کاربران"
        
    
    def __str__(self):
        return f'{self.music.title}'