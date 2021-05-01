#region				-----External Imports-----
from django.contrib.admin import (ModelAdmin, register)
#endregion

#region				-----Internal Imports-----
from .models import (GeneralSetting, ImageSubSetting)
#endregion

@register(ImageSubSetting)
class ImageSubSettingAdmin(ModelAdmin):
    list_filter=[""]

@register(GeneralSetting)
class GeneralSettingAdmin(ModelAdmin): pass