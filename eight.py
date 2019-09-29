from xml.dom import minidom

# parse an xml file by name
doc = minidom.parse('sample.xml')

print(doc.nodeName)
print(doc.firstChild.tagName)

elems = []
elems1 = []
elems2 = []
elems3 = []
for i in range(0, 3):
    elm = doc.getElementsByTagName('title')[i]
    s = [node.data for node in elm.childNodes]
    elems.append(s)
    elm1 = doc.getElementsByTagName('author')[i]
    s1 = [node.data for node in elm1.childNodes]
    elems1.append(s1)
    elm2 = doc.getElementsByTagName('year')[i]
    s2 = [node.data for node in elm2.childNodes]
    elems2.append(s2)
    elm3 = doc.getElementsByTagName('price')[i]
    s3 = [node.data for node in elm3.childNodes]
    elems3.append(s3)

ttl = doc.getElementsByTagName("title")
print("---------- There are %d Titles ------------" % ttl.length)
print(elems)

auth = doc.getElementsByTagName("author")
print("------------ There are %d Authors------------" % auth.length)
print(elems1)

yr = doc.getElementsByTagName("year")
print("------------- There are %d Years-------------" % yr.length)
print(elems2)

price = doc.getElementsByTagName("price")
print("-------------There are %d Prices------------" % price.length)
print(elems3)
