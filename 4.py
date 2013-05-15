import urllib2
import re
a='89879'
i=0
url='http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s'
string='and the next nothing is (\d+)'
while True:
    code=urllib2.urlopen(url %a).read()
    a=re.search(string, code).group(1)
    print a
    i=i+1     
    if i==400:
	break

