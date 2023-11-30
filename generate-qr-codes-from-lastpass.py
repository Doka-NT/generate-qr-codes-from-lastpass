import qrcode
import json
from qrcode.image.pure import PyPNGImage
from pprint import pprint

json_file = open("./var/accounts.json", "r")
json_data = json.load(json_file)

for account in json_data['accounts']:
    issuer = account['issuerName']
    user_name = account['userName']
    secret = account['secret']

    qr_string = f"otpauth://totp/{issuer}:{user_name}?secret={secret}&issuer={issuer}"

    im = qrcode.make(qr_string)
    image_name = f"{issuer}___{user_name}.png"
    im.save(f'./var/{image_name}')
    print(f"{image_name} - OK")
