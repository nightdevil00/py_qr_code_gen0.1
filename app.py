

import qrcode
# example data

data = input('What do you want to QR?')

# output file name
filename = "qr.png"
# generate qr code
img = qrcode.make(data)
# save img to a file
img.save(filename)
