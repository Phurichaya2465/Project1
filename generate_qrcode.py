import qrcode

input_URL = "https://www.facebook.com/"

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=15,
    border=4,
)

qr.add_data(input_URL)
qr.make(fit=True)

img = qr.make_image(fill_color="#5579c6", back_color="white")
img.save("face_qrcode.png")

print(qr.data_list)
