from PIL import ImageFont, ImageDraw, Image  
import random
import re
import glob
import os
  

'''
ast="image processing"
draw.text((500, 25), ast, font=font, fill=(0,0,0,255))
ast = "bad use prohibeted"
draw.text((500, 55), ast, font=font, fill=(0,0,0,255))
image.save("Me_with_text.png")
'''
txtfiles = []
for file in glob.glob("text_dir/*.txt"):
	txtfiles.append(file)

def process_text(assignment_name):
	image = Image.open("standard.jpg")  
	draw = ImageDraw.Draw(image)  

	# use a truetype font 

	fontlist=["handw.ttf","handw.ttf","Fontsah.ttf"]
	#font = ImageFont.truetype("emizfont.ttf", 45) 

	fontname=random.choice(fontlist) 
	print(fontname)
	font = ImageFont.truetype(fontname, 40)
	read_text = open(str(assignment_name), "r")
	data=read_text.read()
	number_of_lines=len(data.splitlines())
	read_text.close()
	initialcount=0
	read_text = open(str(assignment_name), "r")
	xcor=200
	ycor=165
	initial=0
	#character_count=0

	while initialcount<number_of_lines:
		rawdata=read_text.readline()
		initialcount+=1
		rawdata.strip()
		for idx,word in enumerate(re.split(r"\s", rawdata)):
			if idx>=0:
				while initial<len(word):
					ast=word[initial]
					#here starts text placements
					fontname=random.choice(fontlist)
					font = ImageFont.truetype(fontname, 40)
					draw.text((xcor, ycor), ast, font=font, fill=(0,0,0,255))
					if ast=="i"or ast=="l"or ast=="I" or ast=="L":
						xcor+=12
					else:
						xcor+=16
					initial+=1
				xcor+=25
				initial=0
		ycor+=49.5
		xcor=200
	head, tail = os.path.split(str(assignment_name))
	image.save("images/"+str(tail.split(".txt")[0])+".png")
number_of_files=len(txtfiles)
for number in range(0,number_of_files):
	os.chdir("./")
	process_text(txtfiles[number])
#notes: line pixel count is 50 px for vertical spacing
#		line pixel count is 25 px for horizontal specing
#		line pixel count for space character is 50 px
#		starting coordinates after margin to first line are 200,155
#		title name on top has starting coordinates 500 px ,25 px
