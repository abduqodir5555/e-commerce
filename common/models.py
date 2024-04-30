from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.core.validators import FileExtensionValidator, URLValidator

from common.utils import check_instagram_url


# Create your models here.


class Media(models.Model):
    class MEDIA(models.TextChoices):
        IMAGE = "image", _("Image")
        FILE = "file", _("File")
        VIDEO = "video", _("Video")
        MUSIC = "music", _("Music")
    file = models.FileField(_("File"), upload_to="files/", validators=[
        FileExtensionValidator(allowed_extensions=['jpg', 'png', 'jpeg', 'gif', 'mp4', 'mp3', 'flac', 'doc', 'pdf'])])
    type = models.CharField(_("Type"), max_length=30, choices = MEDIA.choices)

    def __str__(self):
        return str(self.id) + ' ' + str(self.file.name.split("/")[-1])

    def clean(self):
        if self.type == self.MEDIA.IMAGE:
            if not self.file.name.endswith(('.jpeg', '.jpg', '.png')):
                raise ValidationError("File type is not image")
        elif self.type == self.MEDIA.FILE:
            if not self.file.name.endswith(('.doc', '.pdf')):
                raise ValidationError("File type is not file")
        elif self.type == self.MEDIA.VIDEO:
            if not self.file.name.endswith('.mp4'):
                raise ValidationError("File type is not video")
        elif self.type == self.MEDIA.MUSIC:
            if not self.file.name.endswith(('.mp3', '.flac')):
                raise ValidationError("File type is not music")

    def save(self, *args, **kwargs):
        self.clean()
        super(Media, self).save(*args, **kwargs)

class Settings(models.Model):
    home_image = models.ForeignKey(Media, on_delete=models.SET_NULL, null=True, blank=True)
    home_title = models.CharField(_("Title"), max_length=120)
    home_subtitle = models.CharField(_("subtitle"), max_length=120)

    def __str__(self):
        return self.home_title


class Country(models.Model):
    name = models.CharField(_("Name"), max_length=30)
    code = models.CharField(_("Code"), max_length=2)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countries")


class Region(models.Model):
    name = models.CharField(_("name"), max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class OurInstagramStory(models.Model):
    image = models.ForeignKey(Media, on_delete=models.CASCADE)
    story_link = models.URLField(_("Story link"), validators=[check_instagram_url])

    def __str__(self):
        return f"{self.id} - {self.story_link}"


class CustomerFeedback(models.Model):
    description = models.TextField(_("Info"))
    rank = models.IntegerField(_("Rank"))
    customer_name = models.CharField(_("Customer Name"), max_length=60)
    customer_position = models.CharField(_("Customer Position"), max_length=60)
    customer_image = models.ForeignKey(Media, on_delete = models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.customer_name
