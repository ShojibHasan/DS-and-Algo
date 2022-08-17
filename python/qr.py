import pyshorteners
from MyQR import myqr as mq
s = pyshorteners.Shortener()
# a = s.chilpit.short('http://localhost:8088/web#id=1&view_type=form&model=account.asset.asset&action=1034')
a = 'http://localhost:8088/web#id=1&view_type=form&model=account.asset.asset&action=1034'
qr = mq.run(a, save_name = 'tco_qr.png')



# import segno
# import io
# qr = segno.make('Paul McCartney')
# buff = io.BytesIO()
# qr.save(buff, kind='svg')
