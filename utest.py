from tkinter import *

root = Tk()

def ted():
    e1num = e1txt.get()
    e2num = e2txt.get()
    e3num = e3txt.get()
    result = e1num * e2num * e3num
    result2 = e1num * e2num
    strresult = str(result)
    strresult2 = str(result2)
    txt1.set(strresult)
    txt2.set(strresult2)

e1txt = IntVar()
e1 = Entry(root, textvariable=e1txt)
e1.grid(row=0,column=0)

e2txt=IntVar()
e2 = Entry(root, textvariable=e2txt)
e2.grid(row=1, column=0)

e3txt = IntVar()
e3 = Entry(root, textvariable=e3txt)
e3.grid(row=2, column=0)

txt1 = StringVar()
l1 = Label(root,textvariable=txt1)
l1.grid(row=3, column=0)

txt2 = StringVar()
l2 = Label(root, textvariable=txt2)
l2.grid(row=4, column=0)

b1 = Button(root,text= "Add Entry", command=ted)
b1.grid(row=5, column=0)

mainloop()
