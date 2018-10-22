import tkinter as tk
from tkinter import ttk
from script import Database
from appliance import Appliance


database = Database()
appliance = Appliance()
class Root(tk.Tk):
    def __init__(self, *args, **kwargs):
        super(Root,self).__init__()
        self.title("ENERGY AUDIT")
        self.createWidget()

    
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
    def createWidget(self):
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

        self.sizing = ttk.Button(self, text="SIZING",)
        self.sizing.grid(row=7, column=4, rowspan=2, columnspan=2, padx=5)

    
if __name__ == '__main__':
    root = Root()
    root.mainloop()
