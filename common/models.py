from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.

class Media(models.Model):
    class MEDIA(models.TextChoices):
        IMAGE = "image", _("Image")
        FILE = "file", _("File")
        VIDEO = "video", _("Video")
        MUSIC = "music", _("Music")
    file = models.FileField(_("File"), upload_to="files/")
    type = models.CharField(_("Type"), max_length=30, choices = MEDIA.choices)

    def __str__(self):
        return self.id

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


class Region(models.Model):
    name = models.CharField(_("name"), max_length=30)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class OurInstagramStory(models.Model):
    image = models.ForeignKey(Media, on_delete=models.CASCADE)
    story_link = models.URLField(_("Story link"))

    def __str__(self):
        return f"{self.id} - {self.story_link}"


class CustomerFeedBack(models.Model):
    description = models.TextField(_("Info"))
    rank = models.IntegerField(_("Rank"))
    customer_name = models.CharField(_("Customer Name"), max_length=60)
    customer_position = models.CharField(_("Customer Position"), max_length=60)
    customer_image = models.ForeignKey(Media, on_delete = models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.customer_name
