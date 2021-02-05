import qrcode

qr = qrcode.QRCode(version=1,
                    error_correction=qrcode.constants.ERROR_CORRECT_L,
                    box_size=1000,
                    border=2)

qr.add_data("http://127.0.0.1:5500/claseImg/index.html")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")

img.save("Precaria_en_QR.png")