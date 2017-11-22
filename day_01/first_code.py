#coding =utf-8
import urllib.request
import re

#define a function
def getHtml(url): #note there is a ':' after the function name....
    page = urllib.request.urlopen(url)
    html = page.read()
    return  html

def getImg(html):
	reg = 'src="(.+?\.png)"'
	img = re.compile(reg)
	html = html.decode('utf-8')
	imglist = re.findall(img,html)
	x=0
	#define 
	for i in range(6): #note there is a ':' after the for statement.
		imgurl = imglist[i]
		#download file from url
		urllib.request.urlretrieve(imgurl,'%s.jpg'% x) 
		x+=1

global Max_Num
Max_Num = 10
for i in range(Max_Num):
	try:
		html = getHtml("view-source:http://www.shangxueba.com/jingyan/2438398.html")
		getImg(html)
		break
	except:
		if i <Max_Num -1:
			continue
		else:
			print("open url error!")

#note:
#python is a typical script-based tool,and much diffrent with normal PL(programing languages like C C++ C# JAVA or others)
#the block statement is more like BASH/MATLAB because its variant parameters is auto type specified,and it's block statement
#is all follwed by a ':'.
print("Hello World")