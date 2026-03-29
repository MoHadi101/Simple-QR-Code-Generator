# #python.exe -m pip install --upgrade pip um richtige package zu installieren von pip 
# import qrcode

# data = input("Enter the Text or URL: ").strip()
# filename= input("Enter the Filename: ").strip()


# qr = qrcode.QRCode(box_size=10, border=4)

# qr.add_data(data)

# image = qr.make_image(fill_color='blak', back_color='white')

# image.save(filename)

# print(f"The QR Code is in{filename}")
import qrcode

data = input("Enter the Text or URL: ").strip()
filename = input("Enter the Filename: ").strip()

# Make sure to add .png extension if not provided
if not filename.endswith('.png'):
    filename = filename + '.png'

qr = qrcode.QRCode(box_size=10, border=4)
qr.add_data(data)
qr.make(fit=True)  # Add this line to generate the QR code

# Fix typo: 'blak' -> 'black'
image = qr.make_image(fill_color='black', back_color='white')

image.save(filename)

print(f"The QR Code is saved as {filename}")  