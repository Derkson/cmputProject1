from Tkinter import *
from backend import *

class NewPersonGUI:
    """docstring for NewPersonGUI.
    Used when the parents of a child or one of the partners
    in a marriage don't exist in the Database"""

    def __init__(self, master, title):
        self.master = master
        self.title = title

        self.backButton = Button(self.master, text="Back",command=self.quit)
        self.submitButton = Button(self.master, text="Submit",command=self.submitCall)

        self.titleLabel = Label(self.master, text=title[0])
        self.FirstNameLabel = Label(self.master, text="First Name:")
        self.FNLabel = Label(self.master, text=title[1])
        self.LastNameLabel = Label(self.master, text="Last Name:")
        self.LNLabel = Label(self.master, text=title[2])
        self.BDLabel = Label(self.master, text="Birth Date:")
        self.BPLabel = Label(self.master, text="Birth Place:")
        self.addressLabel = Label(self.master, text="Address:")
        self.phoneLabel = Label(self.master, text="Phone: Number")

        self.BD = StringVar()
        self.BP = StringVar()
        self.address = StringVar()
        self.phone = StringVar()
        self.BDEntry = Entry(self.master, textvariable=self.BD)
        self.BPEntry = Entry(self.master, textvariable=self.BP)
        self.addressEntry = Entry(self.master, textvariable=self.address)
        self.phoneEntry = Entry(self.master, textvariable=self.phone)

        self.constructGrid()
        pass

    def constructGrid(self):
        self.master.title("New Person")

        self.backButton.grid()
        self.submitButton.grid(column=1,row=0)

        self.titleLabel.grid(column=0,columnspan=2,row=1)
        self.FirstNameLabel.grid(column=0,row=2)
        self.FNLabel.grid(column=1,row=2)
        self.LastNameLabel.grid(column=0,row=3)
        self.LNLabel.grid(column=1,row=3)
        self.BDLabel.grid(column=0,row=4)
        self.BPLabel.grid(column=0,row=5)
        self.addressLabel.grid(column=0,row=6)
        self.phoneLabel.grid(column=0,row=7)

        self.BD.set("YYYY-MM-DD")
        self.BP.set("")
        self.address.set("")
        self.phone.set("")

        self.BDEntry.grid(column=1,row=4)
        self.BPEntry.grid(column=1,row=5)
        self.addressEntry.grid(column=1,row=6)
        self.phoneEntry.grid(column=1,row=7)
        pass

    def deconstructGrid(self):

        self.backButton.grid_remove()
        self.submitButton.grid_remove()

        self.titleLabel.grid_remove()
        self.FirstNameLabel.grid_remove()
        self.FNLabel.grid_remove()
        self.LastNameLabel.grid_remove()
        self.LNLabel.grid_remove()
        self.BDLabel.grid_remove()
        self.BPLabel.grid_remove()
        self.addressLabel.grid_remove()
        self.phoneLabel.grid_remove()

        self.BDEntry.grid_remove()
        self.BPEntry.grid_remove()
        self.addressEntry.grid_remove()
        self.phoneEntry.grid_remove()
        pass

    def submitCall(self):
        create_person(fname=self.title[1], lname=self.title[2], bdate=self.BD.get(),
        bplace=self.BP.get(), address=self.address.get(), phone=self.phone.get())
        self.quit()
        pass

    def quit(self):
        self.deconstructGrid()
        self.master.quit()
        pass

class DriverAbstractGUI:
    """docstring forDriverAbstractGUI."""

    def __init__(self, master, username, driver):
        self.master = master
        self.username = username
        self.driver = driver

        self.backButton = Button(self.master, text="Back",command=self.quit)

        self.constructGrid()
        pass

    def constructGrid(self):
        self.master.title("New Person")

        self.backButton.grid()
        pass

    def deconstructGrid(self):
        self.backButton.grid_remove()
        pass

    def quit(self):
        self.deconstructGrid()
        self.master.quit()
        pass
