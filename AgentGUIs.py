from Tkinter import *
from backend import *

class BirthGUI:
    """docstring for BirthGUI.
    The GUI used when registering a birth"""

    def __init__(self, master, username):
        self.master = master
        self.username = username

        self.backButton = Button(self.master, text="Back",command=self.quit)
        self.submitButton = Button(self.master, text="Submit",command=self.submitCall)

        self.CFNLabel = Label(self.master, text="Child's First Name:")
        self.CLNLabel = Label(self.master, text="Child's Last Name:")
        self.genderLabel = Label(self.master, text="Child's Gender:")
        self.BDLabel = Label(self.master, text="Child's Birthday:")
        self.BPLabel = Label(self.master, text="Child's Birth Place:")
        self.FFNLabel = Label(self.master, text="Father's First Name:")
        self.FLNLabel = Label(self.master, text="Father's Last Name:")
        self.MFNLabel = Label(self.master, text="Mother's First Name:")
        self.MLNLabel = Label(self.master, text="Mother's Last Name:")

        self.CFN = StringVar()
        self.CFNEntry = Entry(self.master, textvariable=self.CFN)
        self.CLN = StringVar()
        self.CLNEntry = Entry(self.master, textvariable=self.CLN)
        self.gender = StringVar()
        self.genderEntry = Entry(self.master, textvariable=self.gender)
        self.BD = StringVar()
        self.BDEntry = Entry(self.master, textvariable=self.BD)
        self.BP = StringVar()
        self.BPEntry = Entry(self.master, textvariable=self.BP)
        self.FFN = StringVar()
        self.FFNEntry = Entry(self.master, textvariable=self.FFN)
        self.FLN = StringVar()
        self.FLNEntry = Entry(self.master, textvariable=self.FLN)
        self.MFN = StringVar()
        self.MFNEntry = Entry(self.master, textvariable=self.MFN)
        self.MLN = StringVar()
        self.MLNEntry = Entry(self.master, textvariable=self.MLN)

        self.constructGrid()
        pass

    def constructGrid(self):
        self.master.title("Register a Birth")

        self.backButton.grid()
        self.submitButton.grid(column=1,row=0)

        self.CFNLabel.grid(row=1)
        self.CLNLabel.grid(row=2)
        self.genderLabel.grid(row=3)
        self.BDLabel.grid(row=4)
        self.BPLabel.grid(row=5)
        self.FFNLabel.grid(row=6)
        self.FLNLabel.grid(row=7)
        self.MFNLabel.grid(row=8)
        self.MLNLabel.grid(row=9)

        self.CFN.set("")
        self.CFNEntry.grid(column=1,row=1)
        self.CLN.set("")
        self.CLNEntry.grid(column=1,row=2)
        self.gender.set("M or F")
        self.genderEntry.grid(column=1,row=3)
        self.BD.set("YYYY-MM-DD")
        self.BDEntry.grid(column=1,row=4)
        self.BP.set("")
        self.BPEntry.grid(column=1,row=5)
        self.FFN.set("")
        self.FFNEntry.grid(column=1,row=6)
        self.FLN.set("")
        self.FLNEntry.grid(column=1,row=7)
        self.MFN.set("")
        self.MFNEntry.grid(column=1,row=8)
        self.MLN.set("")
        self.MLNEntry.grid(column=1,row=9)
        pass

    def deconstructGrid(self):

        self.backButton.grid_remove()
        self.submitButton.grid_remove()

        self.CFNLabel.grid_remove()
        self.CLNLabel.grid_remove()
        self.genderLabel.grid_remove()
        self.BDLabel.grid_remove()
        self.BPLabel.grid_remove()
        self.FFNLabel.grid_remove()
        self.FLNLabel.grid_remove()
        self.MFNLabel.grid_remove()
        self.MLNLabel.grid_remove()

        self.CFNEntry.grid_remove()
        self.CLNEntry.grid_remove()
        self.genderEntry.grid_remove()
        self.BDEntry.grid_remove()
        self.BPEntry.grid_remove()
        self.FFNEntry.grid_remove()
        self.FLNEntry.grid_remove()
        self.MFNEntry.grid_remove()
        self.MLNEntry.grid_remove()
        pass

    def submitCall(self):
        self.mother = (self.MFN.get(),self.MLN.get())
        self.father = (self.FFN.get(),self.FLN.get())
        if not persons_exists(fname=self.mother[0],lname=self.mother[1]):
            self.launchNewPerson(title=("Mother",self.mother[0],self.mother[1]))
        if not persons_exists(fname=self.father[0],lname=self.father[1]):
            self.launchNewPerson(title=("Father",self.father[0],self.father[1]))

        register_birth(fname=self.CFN.get(), lname=self.CLN.get(), gender=self.gender.get(),
        bdate=self.BD.get(), bplace=self.BP.get(), f_fname=self.FFN.get(), f_lname=self.FLN.get(),
        m_fname=self.MFN.get(), m_lname=self.MLN.get(), uid=self.username)

        pass

    def launchNewPerson(self, title):
        self.deconstructGrid()
        NewPersonGUI(master=self.master,title=title)
        self.master.mainloop()
        self.constructGrid()
        pass

    def quit(self):
        self.deconstructGrid()
        self.master.quit()
        pass

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
        pass

    def quit(self):
        self.deconstructGrid()
        self.master.quit()
        pass

class MarriageGUI:
    """docstring for MarriageGUI.
    Used when creating a marriage"""

    def __init__(self, master, username):
        self.master = master
        self.username = username

        self.backButton = Button(self.master, text="Back",command=self.quit)
        self.submitButton = Button(self.master, text="Submit",command=self.submitCall)

        self.FirstFNLabel = Label(self.master, text="First Partner's First Name:")
        self.FirstLNLabel = Label(self.master, text="First Partner's Last Name:")
        self.SecondFNLabel = Label(self.master, text="Second Partner's First Name:")
        self.SecondLNLabel = Label(self.master, text="Second Partner's Last Name:")

        self.FirstFN = StringVar()
        self.FirstFNEntry = Entry(self.master, textvariable=self.FirstFN)
        self.FirstLN = StringVar()
        self.FirstLNEntry = Entry(self.master, textvariable=self.FirstLN)
        self.SecondFN = StringVar()
        self.SecondFNEntry = Entry(self.master, textvariable=self.SecondFN)
        self.SecondLN = StringVar()
        self.SecondLNEntry = Entry(self.master, textvariable=self.SecondLN)

        self.constructGrid()
        pass

    def constructGrid(self):
        self.master.title("Register a Marriage")

        self.backButton.grid()
        self.submitButton.grid(column=1,row=0)

        self.FirstFNLabel.grid(column=0,row=1)
        self.FirstLNLabel.grid(column=0,row=2)
        self.SecondFNLabel.grid(column=0,row=3)
        self.SecondLNLabel.grid(column=0,row=4)

        self.FirstFN.set("")
        self.FirstFNEntry.grid(column=1,row=1)
        self.FirstLN.set("")
        self.FirstLNEntry.grid(column=1,row=2)
        self.SecondFN.set("")
        self.SecondFNEntry.grid(column=1,row=3)
        self.SecondLN.set("")
        self.SecondLNEntry.grid(column=1,row=4)
        pass

    def deconstructGrid(self):

        self.backButton.grid_remove()
        self.submitButton.grid_remove()

        self.FirstFNLabel.grid_remove()
        self.FirstLNLabel.grid_remove()
        self.SecondFNLabel.grid_remove()
        self.SecondLNLabel.grid_remove()

        self.FirstFNEntry.grid_remove()
        self.FirstLNEntry.grid_remove()
        self.SecondFNEntry.grid_remove()
        self.SecondLNEntry.grid_remove()
        pass

    def submitCall(self):
        self.first = (self.FirstFN.get(),self.FirstLN.get())
        self.second = (self.SecondFN.get(),self.SecondLN.get())
        if not persons_exists(fname=self.first[0],lname=self.first[1]):
            self.launchNewPerson(title=("First Partner",self.first[0],self.first[1]))
        if not persons_exists(fname=self.second[0],lname=self.second[1]):
            self.launchNewPerson(title=("Second Partner",self.second[0],self.second[1]))

        register_marriage(p1_fname=self.FirstFN.get(), p1_lname=self.FirstLN.get(), p2_fname=self.SecondFN.get(),
        p2_lname=self.SecondLN.get(), uid=self.username)
        pass

    def launchNewPerson(self, title):
        self.deconstructGrid()
        NewPersonGUI(master=self.master,title=title)
        self.master.mainloop()
        self.constructGrid()
        pass

    def quit(self):
        self.deconstructGrid()
        self.master.quit()
        pass

class RegistrationGUI:
    """docstring forRegistrationGUI.
    Used to renew a vehicle registration"""

    def __init__(self, master, username):
        self.master = master
        self.username = username

        self.backButton = Button(self.master, text="Back",command=self.quit)
        self.submitButton = Button(self.master, text="Submit",command=self.submitCall)

        self.RegistrationLabel = Label(self.master, text="Registration Number:")
        self.PromptLabel = Label(self.master, text="Reg. Number not in database")

        self.Registration = StringVar()
        self.RegistrationEntry = Entry(self.master, textvariable=self.Registration)

        self.constructGrid()
        pass

    def constructGrid(self):
        self.master.title("Renew Vehicle Registration")

        self.backButton.grid()
        self.submitButton.grid(column=1,row=0)

        self.RegistrationLabel.grid(column=0,row=2)

        self.Registration.set("")
        self.RegistrationEntry.grid(column=1,row=2)
        pass

    def deconstructGrid(self):

        self.backButton.grid_remove()
        self.submitButton.grid_remove()

        self.PromptLabel.grid_remove()
        self.RegistrationLabel.grid_remove()
        self.RegistrationEntry.grid_remove()
        pass

    def submitCall(self):
        # TODO: self.PromptLabel.grid(column=0,columnspan=2,row=1)
        renew_vehicle(self.Registration.get())
        pass

    def quit(self):
        self.deconstructGrid()
        self.master.quit()
        pass
