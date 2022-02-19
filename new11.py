from urllib.parse import urlparse, urlunparse,urljoin
parsed_text=urlparse("https://docs.python.org/3/library/tkinter.messagebox.html")
print(parsed_text)
myurl=urlunparse(parsed_text)
print(myurl)


from urllib import request
#f=request.urlopen("https://www.hitam.org/bse.html")
k=urljoin("https://docs.python.org/3/library/tkinter.messagebox.html", "tkinterscrolledtext.html")
print(k)
#print(f.code)