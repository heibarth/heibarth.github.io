import qrcode

img = qrcode.make("https://www.facebook.com/Mr.WildDuck/")
img.save("First try.png")