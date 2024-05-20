from django.db import models
from users.models import User

    



class UserMusicFavorite(models.Model):
    
    user = models.ForeignKey(
        User,
        verbose_name="کاربر",
        on_delete=models.CASCADE,
        related_name="musices_faver"
    )
    
    music = models.ForeignKey(
        'musices.Music',
        verbose_name="آهنگ",
        on_delete=models.CASCADE,
        related_name="music_faver"
    )
    
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['created']
        verbose_name = "موزیک"
        verbose_name_plural = "موزیک ها"
        
    
    def __str__(self):
        return f'{self.music.title}'



class UserAlbumFavorite(models.Model):
    
    user = models.ForeignKey(
        User,
        verbose_name="کاربر",
        on_delete=models.CASCADE,
        related_name="albums_faver"
    )
    
    albume = models.ForeignKey(
        'alboms.Albom',
        verbose_name="آلبوم",
        on_delete=models.CASCADE,
        related_name="albome_faver"
    )
    
    created = models.DateTimeField(auto_now_add=True)
    
    
    class Meta:
        ordering = ['created']
        verbose_name = "آلبوم"
        verbose_name_plural = "آلبوم ها"
        
    
    def __str__(self):
        return f'{self.user}'