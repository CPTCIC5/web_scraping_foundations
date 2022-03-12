#parsing html from local device
#bs4 to access data,read/write/append,prettify/a goood view n edit   /CRUD on a HTML document.
from bs4 import BeautifulSoup

with open('index.html','r') as e:
    doc=BeautifulSoup(e,'html.parser')

#print(doc) #prints whole html file
#print(doc.prettify()) #makes spaces,lil bit prettify the whole a to z html file
#print(doc.title)   #<title>Document</title>4
#print(doc.p) #print line with <p> tag
#print(doc.body)  #body> <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quos fugiat doloribus blanditiis praesentium molestias quidem fugit ea possimus eius, sit maxime, exercitationem iure iusto, qui fuga animi reprehenderit officia consectetur.</p> </body>

#to edit a particular tag (that we're accessing) title
'''
x1= doc.title
x1.string= "hello"
print(x1)
#so now title == hello
'''

#to edit a particular tag (that we're accessing) body
'''
x1=doc.body
x1.string='BODY'
print(x1)
'''


'''
x1.doc.find() #used to 
x1=doc.find_all("p")[0]
print(x1)
'''
