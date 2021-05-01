#region				-----External Imports-----
from django.contrib.admin import (ModelAdmin, register)
from django.forms import Media
#endregion

#region				-----Internal Imports-----
from .models import (GeneralSetting, ImageSubSetting)
#endregion


_image_form_media = Media(
    css={
        'all': (
            'django_image_field/admin/parler_admin.css',
        )
    },
    js={
        'all': (
            'django_image_field/admin/dropzone.js',
            'django_image_field/admin/index.js'
        )
    }
)


@register(ImageSubSetting)
class ImageSubSettingAdmin(ModelAdmin):
    list_filter=[]

@register(GeneralSetting)
class GeneralSettingAdmin(ModelAdmin): pass


class BaseImageFieldAdmin(ModelAdmin):
    @property
    def media(self):
        return base_media + _image_form_media