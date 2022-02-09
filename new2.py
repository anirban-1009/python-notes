from tkinter import *
from tkinter import messagebox
rt=Tk()
rt.title("BOX")
messagebox.showinfo("title","please listen")
messagebox.showerror("display error", "concentrate to the online clss")
rep=messagebox.askyesnocancel("assignment","will you be able to submit by tuesday")
print(rep)
rep1=messagebox.askyesno("result","will you clear the exam")
print(rep1)
rt.mainloop()
