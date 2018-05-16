from django.shortcuts import render
from django.views import View
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.contrib.auth import logout
from django.conf import settings

from Generator.models import QRCode
from Website.forms import CreateQRCodeForm

# Create your views here.
# =======================
class QRCodeView(View):
    template_name = 'qrcode-view.html'

    def get(self, request, *args, **kwargs):
        name_id = kwargs['name_id']
        try:
            qrcode = QRCode.objects.get(name_id=name_id)
        except QRCode.DoesNotExist:
            return HttpResponseNotFound("404 - Not found")

        tags = []
        for tag in qrcode.tags.all():
            tags.append(tag.name)

        context = {
            "qrcode_image_url": qrcode.get_image_url(),
            "qrcode_title": qrcode.title,
            "qrcode_tags": tags,
            "qrcode_created": qrcode.created,
            "qrcode_author": qrcode.author,
            "qrcode_description": qrcode.description
        }

        return render(request, template_name=self.template_name, context=context)


class HomeView(View):
    template_name = 'home.html'

    def get(self, request, *args, **kwargs):
        form = CreateQRCodeForm()
        context = {"form": form}

        return render(request, self.template_name, context=context)


class TopQRCodesView(View):
    template_name = 'top.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={})


class LatestQRCodesView(View):
    template_name = 'latest.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={})


class AboutView(View):
    template_name = 'about.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={})


class SignUpView(View):
    template_name = 'signup.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, context={})


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)