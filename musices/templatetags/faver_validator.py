from django import template
from users.models import User
from musices.models import Music
from favorites.models import UserMusicFavorite


register = template.Library()


@register.simple_tag(name='faver_validator')
def faver_validator(user_id, music_id):
    try:
        user = User.objects.get(id=user_id)
        music = Music.objects.get(id=music_id)
        if user is not None:
            try:
                faver = UserMusicFavorite.objects.get(
                    user = user,
                    music = music
                )
                if faver is not None:
                    return True
                else:
                    return False
            except:
                return False
    except:
        return False