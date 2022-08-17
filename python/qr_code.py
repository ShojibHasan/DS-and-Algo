import qrcode
qr = qrcode.QRCode(
    version=6,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=100,
    border=10,
)
import pyshorteners
s = pyshorteners.Shortener()
 

a = s.chilpit.short('http://localhost:8088/web#id=1&view_type=form&model=account.asset.asset&action=1034')
qr.add_data(a)
qr.make(fit=True)

img = qr.make_image()
img.save("some_file3.png")


# import qrcode
# from qrcode.image.pure import PymagingImage
# img = qrcode.make('Some data here', image_factory=PymagingImage)


# import qrcode
# from PIL import Image
# img = qrcode.make('http://localhost:8088/web#id=1&view_type=form&model=account.asset.asset&action=1034')
# qr = qrcode.QRCode(
#     version=1,
#     error_correction=qrcode.constants.ERROR_CORRECT_H,
#     box_size=10,
#     border=4,
# )


# import qrcode
# from PIL import Image

# img_bg = Image.open('data/src/lena.jpg')

# qr = qrcode.QRCode(box_size=2)
# qr.add_data('I am Lena')
# qr.make()
# img_qr = qr.make_image()

# pos = (img_bg.size[0] - img_qr.size[0], img_bg.size[1] - img_qr.size[1])

# img_bg.paste(img_qr, pos)
# img_bg.save('qr_lena.png')



from MyQR import myqr as mq
mq.run(words = a,
  version = 6,
  colorized = True,
  save_name = 'topcoder.png')




# from MyQR
# import myqr as mq
# mq.run(words = 'http://localhost:8088/web#id=1&view_type=form&model=account.asset.asset&action=1034',
#   version = 6,
#   colorized = True,
#   save_name = 'topcoder.png')
# import MyQR as mq
# mq.run(words = 'http://localhost:8088/web#id=1&view_type=form&model=account.asset.asset&action=1034',
       
#         version = 6,
#         colorized = True,
#         save_name = 'topcoder.png')


# import pyqrcode
# s = pyqrcode.create('http://localhost:8088/web#id=1&view_type=form&model=account.asset.asset&action=1034')
# url = pyqrcode.create(s)
# url.png('myqr.png', scale=6)


# from MyQR import myqr

# '''
# picture：Background picture
# colorized：False black and white，True color
# '''
# myqr.run(words='http://localhost:8088/web#id=1&view_type=form&model=account.asset.asset&action=1034',
#          version=1,
     
#          colorized=True,
#          save_name='goole_myqr.png')



import segno
qrcode = segno.make('http://localhost:8088/web#id=1&view_type=form&model=account.asset.asset&action=1034',micro=False)
qrcode.save('2.png')
# qrcode.save('yellow-submarine.png')

# import segno
# qrcode = segno.make('The Beatles -- Albums', error='h')
# qrcode.to_artistic(scale=8)
# qrcode.save('lol.png')


# import short_url
# url = short_url.encode_url('http://localhost:8088/web#id=1&view_type=form&model=account.asset.asset&action=1034')

# print(url)



