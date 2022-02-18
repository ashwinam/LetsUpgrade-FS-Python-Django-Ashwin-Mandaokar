import qrcode
d = "hello"
img = qrcode.make(d)
type(img)
img.save(d+".jpg")