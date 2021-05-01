#region				-----External Imports-----
from django.db.models import (Model, ForeignKey, ImageField, CASCADE,
PositiveIntegerField, BooleanField, ManyToManyField, SET_NULL)
from django.utils.translation import ugettext_lazy as _
from multiselectfield import MultiSelectField
#endregion

class ImageSubSetting(Model):
    #region            -----Help Widgets-----
    extensions=["DIB", "JPEG", "PNG", "WEBP", "BMP", "EPS", "SPIDER"]
    choices=[(id, format) for id, format in enumerate(extensions, 1)]
    #endregion

    #region            -----Information-----
    height=PositiveIntegerField(default=0, verbose_name=_("Height"),
    help_text=_("Height of the current image in pixels"))
    width=PositiveIntegerField(default=0, verbose_name=_("Width"),
    help_text=_("Width of the current image in pixels"))
    apply=BooleanField(default=False, verbose_name=_("Apply"),
    help_text=_("Apply uploaded watermark on image"))
    formats=MultiSelectField(blank=False, choices=choices,
    verbose_name=_("Formats images convert to"),null=True)
    #endregion

    #region              -----Metadata-----
    class Meta(object):
        verbose_name_plural=_("Settings")
        verbose_name=_("Setting")
    #endregion

class GeneralSetting(Model):
    #region            -----Information-----
    watermark=ImageField(max_length=1000, blank=True, null=True,
    verbose_name=_("Image to apply above other images"), 
    upload_to="watermark/")
    #endregion

    #region              -----Relation-----
    settings=ManyToManyField("ImageSubSetting", blank=False,
    verbose_name=_("Settings for all images in database"))
    #endregion

    #region              -----Metadata-----
    class Meta(object):
        verbose_name_plural=_("Image settings")
        verbose_name=_("Image setting")
    #endregion

class InnerImage(Model):
    #region            -----Information-----
    original=ImageField(max_length=1000, blank=False, null=True, 
    upload_to="original/", verbose_name=_("Original image"))
    marked=ImageField(max_length=1000, blank=True, null=True, 
    upload_to="marked/", verbose_name=_("Marked image"))
    #endregion

    #region              -----Relation-----
    parent=ForeignKey("Image", on_delete=CASCADE, null=True, 
    related_name="children")
    #endregion

class Image(Model):
    #region            -----Information-----
    order=PositiveIntegerField(default=0, blank=True, null=True)
    original=ImageField(max_length=1000, blank=False, null=True, 
    upload_to="original/", verbose_name=_("Original image"))
    #endregion

    #region              -----Metadata-----
    class Meta(object): ordering=["order"]
    #endregion