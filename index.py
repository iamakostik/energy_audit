import tkinter as tk
from tkinter import ttk
from script import Database
from appliance import Appliance
from main import Root
import tkinter.messagebox
import os
import datetime
import  random

database = Database()
appliance = Appliance()

date= datetime.datetime.now().date()
LARGE_FONT=(" verdana", 12)
class Energyaudit(tk.Tk):

    def __init__(self, *args, **kwargs):
        super(Energyaudit, self, *args, **kwargs).__init__()
        tk.Tk.iconbitmap(self, default="energyaudit.ico")
        tk.Tk.title(self,string="ENERGY AUDIT")
        container = tk.Frame(self)
        container.grid(row=0, column=0)
        container.grid_rowconfigure(0,weight=1)
        container.grid_columnconfigure( 0, weight=1)

        self.frames = {}

        for F in (StartPage, LoginPage, RegisterPage, Main, Sizing, Solarmodule, Battery, Chargecontroller, Inverter, Cost):
            frame = F(container,self)
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky='nsew')

        self.show_frame(StartPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Energy Audit App", font = LARGE_FONT)
        label.grid(row= 0, column = 0)
        button1 = ttk.Button(self, text="Login",command=lambda : controller.show_frame(LoginPage))
        button1.grid(row=1,column=1)
        button1 = ttk.Button(self, text="Register",
                             command=lambda: controller.show_frame(RegisterPage))
        button1.grid(row=2, column=1)

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="  Login", font=LARGE_FONT)
        label.grid(row=2, column=2)
        button1 = ttk.Button(self, text="Home",
                             command=lambda: controller.show_frame(StartPage))
        button1.grid(row=1, column=1)
        button2 = ttk.Button(self, text="Login",
                             command=lambda: controller.show_frame(Main))
        button2.grid(row=2, column=1)



class RegisterPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=" Register Here", font=LARGE_FONT)
        label.grid(row=2, column=2)
        button1 = ttk.Button(self, text="Login",
                             command=lambda: controller.show_frame(LoginPage))
        button1.grid(row=1, column=1)


class Sizing(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=" Sizing Page", font=LARGE_FONT)
        label.grid(row=1, column=2)
        gobackbtn = ttk.Button(self, text="Go Back",
                             command=lambda: controller.show_frame(Main))
        gobackbtn.grid(row=1, column=1)
        button2 = ttk.Button(self, text="Generate Report",
                             command=self.generate_report)
        button2.grid(row=7, column=7, sticky ='es')
        
        solarmodulebtn = ttk.Button(
            self, text=" Solar Module", command=lambda: controller.show_frame(Solarmodule))
        solarmodulebtn.grid(
            row=2, column=2)
        batterybtn = ttk.Button(
            self, text=" Battery Module", command=lambda: controller.show_frame(Battery))
        batterybtn.grid(row=3, column=2)
        chargecontrollerbtn = ttk.Button(
            self, text=" Charge Controller Module", command=lambda: controller.show_frame(Chargecontroller))
        chargecontrollerbtn.grid(row=4, column=2)
        inverterbtn = ttk.Button(
            self, text=" Inverter Module", command=lambda: controller.show_frame(Inverter))
        inverterbtn.grid(row=5, column=2)
        costbtn = ttk.Button(
            self, text=" Cost Module", command=lambda: controller.show_frame(Cost))
        costbtn.grid(row=6, column=2)
    
    def generate_report(self):
        directory = "C:/Users/innoc/Desktop/projects/energyaudit/Report/" + str(date) + "/"

        if not os.path.exists(directory):
            os.makedirs(directory)
        else:
            company = "\t\t\t\t\t Energy Audit Report"
            #data_from = "\t\t\t\t " + self.view_entry
            final = company
            file_name = str(directory) +str(date) +str(random.randrange(5000,10000)) + ".rtf"
            f = open(file_name, 'w')
            f.write(final)

            os.startfile(file_name,"print")
            f.close()


class Solarmodule(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=" Solar Module Page", font=LARGE_FONT)
        label.grid(row=1, column=2)
        gobackbtn = ttk.Button(self, text="Go Back",
                               command=lambda: controller.show_frame(Sizing))
        gobackbtn.grid(row=1, column=1)


class Battery(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=" Battery Module Page", font=LARGE_FONT)
        label.grid(row=1, column=2)
        gobackbtn = ttk.Button(self, text="Go Back",
                               command=lambda: controller.show_frame(Sizing))
        gobackbtn.grid(row=1, column=1)


class Chargecontroller(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=" Charge Controller Module Page", font=LARGE_FONT)
        label.grid(row=1, column=2)
        gobackbtn = ttk.Button(self, text="Go Back",
                               command=lambda: controller.show_frame(Sizing))
        gobackbtn.grid(row=1, column=1)


class Inverter(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=" Inverter Module Page", font=LARGE_FONT)
        label.grid(row=1, column=2)
        gobackbtn = ttk.Button(self, text="Go Back",
                               command=lambda: controller.show_frame(Sizing))
        gobackbtn.grid(row=1, column=1)


class Cost(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text=" Cost Module Page", font=LARGE_FONT)
        label.grid(row=1, column=2)
        gobackbtn = ttk.Button(self, text="Go Back",
                               command=lambda: controller.show_frame(Sizing))
        gobackbtn.grid(row=1, column=1)

    
class Main(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.createWidget(parent, controller)

    def get_selected_row(self,event):
        global selected_tuple
        index = self.list1.curselection()[0]
        selected_tuple = self.list1.get(index)

        self.entappliance.delete(0, tk.END)
        self.entappliance.insert(tk.END, selected_tuple[1])

        self.entquantity.delete(0, tk.END)
        self.entquantity.insert(tk.END, selected_tuple[2])

        self.entpower_rating.delete(0, tk.END)
        self.entpower_rating.insert(tk.END, selected_tuple[3])

        self.entduty_cycle.delete(0, tk.END)
        self.entduty_cycle.insert(tk.END, selected_tuple[4])

        self.entdaily_energy.delete(0, tk.END)
        self.entdaily_energy.insert(tk.END, selected_tuple[5])

        self.entload_profile.delete(0, tk.END)
        self.entload_profile.insert(tk.END, selected_tuple[6])

    def view_command(self):
        self.list1.delete(0, tk.END)
        for row in database.view():
            self.list1.insert(tk.END, row)

    def search_command(self):
        self.list1.delete(0, tk.END)
        for row in database.search(self.appliance_text.get()):
            self.list1.insert(tk.END, row)

    def insert_command(self):
        self.e1num = self.q.get()
        self.e2num = self.pr.get()
        self.e3num = self.dc.get()
        self.result = self.e1num * self.e2num * self.e3num
        self.result2 = self.e1num * self.e2num
        # strresult = str(result)
        # strresult2 = str(result2)
        self.de.set(self.result)
        self.lp.set(self.result2)
        if self.appliance_text.get() == '' or self.e1num == '' or self.e2num == '' or self.e3num == '':
            tkinter.messagebox.showinfo("Error", "you can't insert because a value is missing" )
        else:
            database.insert(self.appliance_text.get(), self.q.get(),
                        self.pr.get(), self.dc.get(), self.result, self.result2)
            self.list1.delete(0, tk.END)
            self.list1.insert(tk.END, (self.appliance_text.get(), self.q.get(),
                                self.pr.get(), self.dc.get(), self.result, self.result2))

    def delete_comamnd(self):
        database.delete(selected_tuple[0])

    def update_command(self):
        database.update(selected_tuple[0], self.appliance_text.get(
        ), self.q.get(), self.pr.get(), self.dc.get(), self.de.get(), self.lp.get())

    def total_ed_command(self):
        self.list1.delete(0, tk.END)
        for row in database.total_ed():
            self.list1.insert(tk.END, row)

    def total_tlp_command(self):
        self.list1.delete(0, tk.END)
        for row in database.total_tlp():
            self.list1.insert(tk.END, row)


    #tkinter label starts here
    def createWidget(self, parent, controller):
        self.id = ttk.Label(self, text="ID")
        self.id.grid(row=0, column=0, sticky='e')

        self.appliance = ttk.Label(self, text="Appliance")
        self.appliance.grid(row=1, column=0, sticky='e')

        self.quantity = ttk.Label(self, text="quantity")
        self.quantity.grid(row=2, column=0, sticky='e')

        self.power_rating = ttk.Label(self, text="Power Rating (watts)")
        self.power_rating.grid(row=3, column=0, sticky='e')

        self.duty_cycle = ttk.Label(self, text="Duty Cycle (hours)")
        self.duty_cycle.grid(row=4, column=0, sticky='e')

        self.daily_energy = ttk.Label(self, text="Daily Energy (wh)")
        self.daily_energy.grid(row=5, column=0, sticky='e')

        self.load_profile = ttk.Label(self, text="Load Profile (watts)")
        self.load_profile.grid(row=6, column=0, sticky='e')
            #tkinter Label widget ends here

        #tkinter Entry widget starts here
        self.entid = tk.Entry(self, text="ID")
        self.entid.grid(row=0, column=1)

        self.appliance_text = tk.StringVar()
        self.entappliance = ttk.Combobox(self, textvariable=self.appliance_text,width=17)
        self.entappliance['values'] = appliance.appliance_list
        self.entappliance.grid(row=1, column=1)
        
        self.q = tk.IntVar()
        self.entquantity = tk.Entry(self, textvariable=self.q)
        self.entquantity.grid(row=2, column=1)

        self.pr = tk.DoubleVar()
        self.entpower_rating = ttk.Entry(self, text=self.pr)
        self.entpower_rating.grid(row=3, column=1)

        self.dc = tk.DoubleVar()
        self.entduty_cycle = ttk.Entry(self, text=self.dc)
        self.entduty_cycle.grid(row=4, column=1)

        self.de = tk.DoubleVar()
        self.entdaily_energy = ttk.Entry(self, textvariable=self.de)
        self.entdaily_energy.grid(row=5, column=1)

        self.lp = tk.DoubleVar()
        self.entload_profile = ttk.Entry(self, textvariable=self.lp)
        self.entload_profile.grid(row=6, column=1)
        #tkinter Entry widget ends here

        self.add_entry = tk.Button(self, text="Add Entry",
                                height=2, width=20, command=self.insert_command)
        self.add_entry.grid(row=7, column=0, rowspan=2, columnspan=2)

        self.list1 = tk.Listbox(self, height=20, width=50)
        self.list1.grid(row=0, column=2, rowspan=10)
        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)
        self.s1 = tk.Scrollbar(self)
        self.s1.grid(row=0, column=3, rowspan=10)
        self.list1.configure(yscrollcommand=self.s1.set)
        self.s1.configure(command=self.list1.yview)

        #tkinter button widgets for control
        self.view_entry = ttk.Button(self, text="View All", command=self.view_command)
        self.view_entry.grid(row=0, column=4, rowspan=2, columnspan=2)

        self.search = ttk.Button(self, text="Search", command=self.search_command)
        self.search.grid(row=1, column=4, rowspan=2, columnspan=2)

        self.update = ttk.Button(self, text="Update Selected", command=self.update_command)
        self.update.grid(row=2, column=4, rowspan=2, columnspan=2)

        self.delete = ttk.Button(self, text="Delete Selected", command=self.delete_comamnd)
        self.delete.grid(row=3, column=4, rowspan=2, columnspan=2)

        self.total_tlp = ttk.Button(self, text="Total TLP", command=self.total_tlp_command)
        self.total_tlp.grid(row=4, column=4, rowspan=2, columnspan=2)

        self.total_ed = ttk.Button(self, text="Total ED",command=self.total_ed_command)
        self.total_ed.grid(row=5, column=4, rowspan=2, columnspan=2)

        self.sizing = ttk.Button(self, text="SIZING", command = lambda : controller.show_frame(Sizing))
        self.sizing.grid(row=7, column=4, rowspan=2, columnspan=2, padx=5)
if __name__ == '__main__':
    app = Energyaudit()
    app.mainloop()
