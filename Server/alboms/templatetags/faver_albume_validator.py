from django import template
from users.models import User
from alboms.models import Albom
from favorites.models import UserAlbumFavorite


register = template.Library()


@register.simple_tag(name='faver_albume_validator')
def faver_validator(albume_id, user_id):
    try:
        user = User.objects.get(id=user_id)
        albume = Albom.objects.get(id=albume_id)
        if user is not None:
            try:
                faver = UserAlbumFavorite.objects.get(
                    user = user,
                    albume = albume
                )
                if faver is not None:
                    return True
                else:
                    return False
            except:
                return False
    except:
        return False