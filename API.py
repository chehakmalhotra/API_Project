import requests
import json
import pprint



print("No key is needed")
Url="https://www.thecolorapi.com/id?"
type=input("Enter type")
if type=="hex":
    hex=input("Enter hex number")
    quer_par={"hex":hex,"format":format}
elif type=='rgb':
    rgb=input("Enter rgb number")
    quer_par={"rgb":rgb,"format":format}
elif type=='hsl':
    hsl=input("Enter hsl number")
    quer_par={"hsl":hsl,"format":format}
elif type=='cmyk':
    cmyk=input("Enter cmyk number")
    quer_par={"cmyk":cmyk,"format":format}
format="json"


resp=requests.get(Url,quer_par)


Data=resp.json()

Image=[]
Images=(Data["image"])
for url in Images:
    Image.append(Images[url])
Hex_rgb_hsv_name=[]
INFO=[Data['hex'],Data['rgb'],Data['hsl'],Data['hsv'],Data['name']]
for i in INFO:
    Hex_rgb_hsv_name.append(i)

filter={}
filter["HEX Value"]=Hex_rgb_hsv_name[0]
filter["RGB Value"]=Hex_rgb_hsv_name[1]
filter["HSL Value"]=Hex_rgb_hsv_name[2]
filter["HSV Value"]=Hex_rgb_hsv_name[3]
filter["Color Name"]=Hex_rgb_hsv_name[4]
filter["Image without Name: "]=Image[0]
filter["Image with Name: "]=Image[1]

print(pprint.pp(filter))

