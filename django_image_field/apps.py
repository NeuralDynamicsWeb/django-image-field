#region				-----External Imports-----
from django.utils.translation import ugettext_lazy as _
from django.apps import AppConfig
#endregion

#region				-----Internal Imports-----
#endregion

class ImageConfig(AppConfig):
    default_auto_field='django.db.models.BigAutoField'
    verbose_name=_("Image application")
    name='django_image_field'
