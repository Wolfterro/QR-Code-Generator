from django.db import models
from django.conf import settings

# Create your models here.
# ========================
class Tags(models.Model):
    name = models.CharField(max_length=100, default=None)

    def __str__(self):
        return self.name


class QRCode(models.Model):
    name_id = models.CharField(max_length=16, default=None)
    title = models.CharField(max_length=100, default=None)
    description = models.CharField(max_length=200, default=None, blank=True, null=True)
    image = models.ImageField()
    tags = models.ManyToManyField(Tags)

    def __str__(self):
        return "%s - [%s]" % (self.title, self.name_id)

    def get_page_url(self):
        return "/qrcode/%s" % (self.name_id)

    def get_image_url(self):
        return "/%s%s.%s" % (settings.QRCODE_SAVE_PATH, self.name_id, settings.QRCODE_FORMAT)
