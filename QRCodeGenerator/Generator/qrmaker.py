import qrcode
import qrcode.image.svg

class QRMaker(object):
    def __init__(self, message_to_qr):
        self.message_to_qr = message_to_qr
        self.qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            image_factory=qrcode.image.svg.SvgPathImage
        )

    def make(self):
        self.qr.add_data(self.message_to_qr)
        self.qr.make(fit=True)

        return self.qr.make_image(fill_color="black", back_color="white")