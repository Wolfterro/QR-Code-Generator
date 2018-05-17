from django.shortcuts import render
from django.views import View
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.contrib.auth import logout, update_session_auth_hash
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm

from Generator.models import QRCode
from Website.forms import CreateQRCodeForm, MyAccountForm

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


class AccountView(View):
    template_name = 'account.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            return HttpResponseRedirect("/")

        user = User.objects.get(username=request.user.username)
        data = {'username': user.username,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email}

        form = MyAccountForm(initial=data)
        context = {"form": form}

        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            context = {"warning": "Erro!",
                       "message": "Nenhum usuário logado!"}
            return render(request, 'warning.html', context=context)

        form = MyAccountForm(data=request.POST, instance=request.user)
        if form.is_valid():
            user = form.save()

            context = {"warning": "Sucesso!",
                       "message": "As informações do usuário foram atualizadas com sucesso!"}
            return render(request, 'warning.html', context=context)
        else:
            context = {"warning": "Erro!",
                       "message": "Verifique os dados inseridos e tente novamente!"}
            return render(request, 'warning.html', context=context)


class ChangePasswordView(View):
    template_name = 'password.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            context = {"warning": "Erro!",
                       "message": "Nenhum usuário logado!"}
            return render(request, 'warning.html', context=context)

        form = PasswordChangeForm(request.user)
        context = {"form": form}

        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        if request.user.is_anonymous:
            context = {"warning": "Erro!",
                       "message": "Nenhum usuário logado!"}
            return render(request, 'warning.html', context=context)

        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)

            context = {"warning": "Sucesso!",
                       "message": "A senha do usuário foi atualizada com sucesso!"}
            return render(request, 'warning.html', context=context)
        else:
            context = {"warning": "Erro!",
                       "message": "Verifique os dados inseridos e tente novamente!"}
            return render(request, 'warning.html', context=context)


class LogoutView(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)