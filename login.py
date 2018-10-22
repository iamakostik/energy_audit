from tkinter import *
#from tkinter.ttk import *
root = Tk()
root.configure(bg="#00ff70")
root.geometry("600x400")

label = Label(
    root,bd=8,relief="groove",
    width=25,height=2, 
    text="Energy Audit ",
    font="Times 15")
label.grid(row=0,column=0,columnspan=10)

label2 =Label(
    root, bd=1, 
    relief="solid", 
    text="Login to use the Energy Audit App", 
    font="Times 15",
    anchor=NW,)
label2.grid(row=1,column=0)

frame = Frame(root)
frame2 = Frame(root)
userNameLabel = Label(frame2, text="User Name")
userNameLabel.grid(row='0',column='0',sticky=E)
passWordLabel = Label(frame2, text="Password")
passWordLabel.grid(row='1', column='0',sticky=E)

userNameEntry = Entry(frame2, text="User Name")
userNameEntry.grid(row='0', column='1')
passWordEntry = Entry(frame2, text="Password")
passWordEntry.grid(row='1', column='1')

loginButton = Button(frame2,text="Login")
loginButton.grid(columnspan=2)

#frame.grid(row=0,column=0)
frame2.grid(row=2,column=0)
root.mainloop()
