import urllib
import xml.dom.minidom
f = urllib.urlopen("http://www.treasury.gov/resource-center/data-chart-center/interest-rates/Datasets/yield.xml")
s = f.read()
f2 = open("yield.xml",'w')
f2.write(s)
f2.close()
x = xml.dom.minidom.parse("yield.xml")

y = x.getElementsByTagName("BC_1MONTH")

books = x.getElementsByTagName("LIST_G_NEW_DATE")

for book in books:
  print book.getElementsByTagName("BID_CURVE_DATE")[0].firstChild
  print book.getElementsByTagName("BC_1MONTH")[0].firstChild
