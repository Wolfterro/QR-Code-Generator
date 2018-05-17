from django.contrib import admin
from django.utils.html import format_html

from Generator.models import Tags, QRCode

# Register your models here.
# ==========================
@admin.register(Tags)
class TagsAdmin(admin.ModelAdmin):
    pass


@admin.register(QRCode)
class QRCodeAdmin(admin.ModelAdmin):

    def show_image(self, obj):
        html = '<img src="%s" width="250" height="250" alt="QR Code" style="background-color: #fff;"/>'
        return format_html(html % (obj.get_image_url()))

    def show_url(self, obj):
        html = '<a href="%s" target="_blank">%s</a>' % (obj.get_page_url(), obj.get_page_url())
        return format_html(html)

    show_image.short_description = "QR Code"
    show_url.short_description = "URL"

    readonly_fields = ['created', 'show_image', 'show_url', ]

