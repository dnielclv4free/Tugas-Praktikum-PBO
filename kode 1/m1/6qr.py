import qrcode
img = qrcode.make('https://kbbi.web.id/anomali')
type(img)  # qrcode.image.pil.PilImage
img.save("absen.png")