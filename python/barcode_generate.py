import barcode
from barcode.writer import ImageWriter

number = 'http://localhost:8088/web?debug=1#id=1&view_type=form&model=account.asset.asset&menu_id=818&action=1034' 


EAN = barcode.get_barcode_class('ean13')
ean = EAN(number, writer=ImageWriter())
fullname = ean.save('barcode')