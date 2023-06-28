import qrcode
def generate_qrcode(text):
   qr= qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,

)
   # Adding data to the instance 'qr'
   qr.add_data(text)
   # Encoding data using make() function

   qr.make(fit=True)
   img = qr.make_image(fill_color = 'black',
                    back_color = 'white')
   img.save('MyQRCode2.png')
   
url=input('enter the url: ')
generate_qrcode(url)
   