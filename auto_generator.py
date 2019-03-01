import pandas as pd
import smtplib 
import string

from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 

from PIL import Image, ImageDraw, ImageFont
from pandas import ExcelWriter
from pandas import ExcelFile
p_wE_d ="#######"
fromaddr = "certificate@&&&&&&&&&&&&"

df = pd.read_excel('soccer_part.xlsx', sheet_name='Sheet2')


for i in df.index:
	image = Image.open('RoboSoccer_Participation.jpg')
	draw = ImageDraw.Draw(image)
	font = ImageFont.truetype('JosefinSans-SemiBold.ttf', size=75)
# (x, y) = (1500, 1300)
	color = 'rgb(0, 0, 0)'
	name = df['Name'][i] 
	name.upper()
	# position = df['position'][i]
	print(i+1,name)
	# print(i)
	draw.text((1500, 1450), name, fill=color, font=font)
	# draw.text((1440, 1580), position, fill=color, font=font)
	imageName = "monster_part/"+name+".pdf"
	image.save(imageName)
	
	toaddr = df['Email'][i]
	msg = MIMEMultipart() 
	msg['From'] = fromaddr 

	# storing the receivers email address 
	msg['To'] = toaddr 

	# storing the subject 
	msg['Subject'] = "Certificate for Participation in Robo Soccer in Technovanza 2018"

	# string to store the body of the mail 
	body = '''Thank you for participating in Robo Soccer Competition in Technovanza 2018
			  
	Thanks and Regards
	Team Technovanza
			'''

	# attach the body with the msg instance 
	msg.attach(MIMEText(body, 'plain')) 

	# open the file to be sent 
	filename = name +".pdf"
	attachment = open(imageName, "rb")
	p = MIMEBase('application', 'octet-stream') 

	# To change the payload into encoded form 
	p.set_payload((attachment).read()) 

	# encode into base64 
	encoders.encode_base64(p) 

	p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 

	# attach the instance 'p' to instance 'msg' 
	msg.attach(p) 

	# creates SMTP session 
	s = smtplib.SMTP('smtp.gmail.com', 587) 

	# start TLS for security 
	s.starttls() 

	# Authentication 
	s.login(fromaddr, p_wE_d) 

	# Converts the Multipart msg into a string 
	text = msg.as_string() 

	# sending the mail 
	s.sendmail(fromaddr, toaddr, text) 

	# terminating the session 
	


s.quit() 
 