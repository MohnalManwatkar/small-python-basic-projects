#importing required libraries
import qrcode
import image

qr = qrcode.QRCode(
    version = 15,  #15 means version the qr code, high the number bigger the code image and complicated picture
    box_size = 10,  #size of the box where qr code will be displayed
    border = 5  #it is a white part of image -- border in all 4 side white in colour

)

data = "https://drive.google.com/file/d/1zGkus2C_y_OLFyGbwDaQQh4ydlTehrub/view?usp=share_link"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = 'black', back_colour = 'white')
img.save("resume.png")