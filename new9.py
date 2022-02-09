from urllib.parse import urlparse,urlunparse,urljoin
from urllib import request
parsed_text=urlparse("https://docs.python.org/3/library/tkinter.messagebox.html")
print(parsed_text)
myurl=urlunparse(parsed_text)
print(myurl)
f=request.urlopen("https://docs.python.org/3/library/tkinter.messagebox.html")
print(f.read())
k=urljoin("https://docs/python.org/3/library/tkinter.messagebox.html","tkinter.scroledtext.html")
print(k)
