from aip import AipFace
import base64

""" 你的 APPID AK SK """
APP_ID = '15459757'
API_KEY = 'TeflwgR9RxI8haND8HI1atao'
SECRET_KEY = 'GaXWynsGRBGGeCPfAAwkSTnutDK3I7ti'

client = AipFace(APP_ID, API_KEY, SECRET_KEY)

print(client)

""" 读取图片 """

f = open('image/jjw.jpg', 'rb')

image = base64.b64encode(f.read())

image64 = str(image, 'utf-8')

image_type = "BASE64"

result = client.detect(image64, image_type, {"face_field": "beauty"})

print(result["result"]['face_list'][0]["beauty"])
