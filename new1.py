from tkinter import *
from tkinter import messagebox
rt = Tk()
rt.title('BOX')
messagebox.showinfo('title', "please listen")
messagebox.showerror("display error","concentrate to the oline class")
rep=messagebox.askyesnocancel("assignment","well you be able to submit by tuesday")
print(rep)
rt.mainloop()
