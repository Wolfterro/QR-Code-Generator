import random
import string

from django.http import HttpResponseNotAllowed, JsonResponse
from django.views import View
from django.conf import settings

from Generator.qrmaker import QRMaker
from Generator.models import Tags, QRCode

# Create your views here.
# =======================
class GenerateQRCodeView(View):
    def generate_random_key(self):
        return ''.join(random.SystemRandom().choice(string.digits + string.ascii_lowercase) for i in range(10))

    def generate_qr_code(self, request):
        title = request.POST.get('title')
        description = request.POST.get('description')
        message_to_qr = request.POST.get('message_to_qr')
        tags = request.POST.getlist('tags[]')

        if title and message_to_qr:
            rnd_key = self.generate_random_key()

            filename = "%s%s.%s" % (settings.QRCODE_SAVE_PATH, rnd_key, settings.QRCODE_FORMAT)
            qr = QRMaker(message_to_qr)
            img = qr.make()
            img.save(filename)

            qrcode = QRCode.objects.create(
                name_id=rnd_key,
                title=title,
                description=description,
                image=filename
            )
            for tag_name in tags:
                if len(tag_name) <= 0:
                    break

                tag = Tags.objects.get_or_create(name=tag_name)[0]

                qrcode.tags.add(tag)
                qrcode.save()

            return qrcode
        else:
            return None

    def get(self, request, *args, **kwargs):
        return HttpResponseNotAllowed(permitted_methods=["POST"])

    def post(self, request, *args, **kwargs):
        qrcode = self.generate_qr_code(request)
        response = {"status": "FAIL"}

        if qrcode:
            tags = []
            for tag in qrcode.tags.all():
                tags.append(tag.name)

            response['status'] = "OK"
            response['qrcode_name_id'] = qrcode.name_id
            response['qrcode_title'] = qrcode.title
            response['qrcode_description'] = qrcode.description
            response['qrcode_tags'] = tags
            response['qrcode_filename'] = "%s.%s" % (qrcode.name_id, settings.QRCODE_FORMAT)
            response['qrcode_image_url'] = qrcode.get_image_url()
            response['qrcode_page_url'] = qrcode.get_page_url()

        return JsonResponse(response)
