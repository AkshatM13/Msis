#GEt data in unstructed way
"""import requests

web = requests.get("https://www.youtube.com/watch?v=fJKdIf11GcI")
#print(web)
web.content"""

#parsing using BS4

"""import requests

from bs4 import BeautifulSoup

web = requests.get("https://www.tutorialsfreak.com/")

web.status_code

web.content

soup = BeautifulSoup(web.content,"html.parser")"""

#import requests
#from bs4 import BeautifulSoup
##url = "https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
#r=requests.get(url)
#print(r.status_code)
#print(r)
#print(r.text)
#soup= BeautifulSoup(r.text ,"lxml")
#print(soup.div)  #tag div
#print(soup.div.ul)  #tag ul

# attribute
"""tag=soup.header
#print(tag.attrs)
atb=(tag.attrs)
print(atb["class"])"""

#navigable strings
#tag=soup.div.p.string
#print(tag)

import requests
from bs4 import BeautifulSoup

url ="https://webscraper.io/test-sites/e-commerce/allinone/computers/tablets"
r=requests.get(url)
#print(r)

soup=BeautifulSoup(r.text,"lxml")

price =( soup.find("h4" , {"class":"price float-end card-title pull-right"}))
print(price.string)

#desc=(soup.find("p",{"class":"review-count float-end"}))  
#print(desc.string)
 #or

desc=(soup.find("p",class_ = "review-count float-end"))
print(desc.string)







