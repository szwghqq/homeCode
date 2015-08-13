#coding:utf8
import re
import urllib.request
def getHTML(url):
    page = urllib.request.urlopen(url).read()
    html = page.read()
    return html
 
#http://a.36krcnd.com/photo/2014/9dcdc9eaed74a5879236f2fc7def0072.png!slider
def getImg(html,imgType):
    reg = r'src="(.*?\.+'+imgType+'!slider)" '
    imgre = re.compile(reg)
    imgList = re.findall(imgre, html)
    x=0
    for imgurl in imgList:
        print(imgurl)
        urllib.urlretrieve(imgurl, '%s.%s' % (x, imgType))
        x =x+1
 
 
html= getHTML("http://www.36kr.com/topic/brands")
 
getImg(html,'jpg')
