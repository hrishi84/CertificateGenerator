from PIL import Image, ImageDraw, ImageFont



image = Image.open('Robowars_Participation.jpg')
draw = ImageDraw.Draw(image)
font = ImageFont.truetype('JosefinSans-SemiBold.ttf', size=75)
# (x, y) = (1500, 1300)
color = 'rgb(0, 0, 0)'
name = "Maharshi Naik"
# position = "First"
event = " Robo Strike "
print(name)
draw.text((1500, 1350), name, fill=color, font=font)
# draw.text((1440, 1580), position, fill=color, font=font)
imageName = name+".png"
image.save(imageName)