import qrcode as qr

print("chk 1")
img = qr.make("This is harry")
print("chk 2")
img.save("txt.png")

print("end")
