from backend import *

class BirthGUI:
    """docstring for BirthGUI.
    The GUI used when registering a birth"""

    def __init__(self, master, username):
        self.master = master
        self.username = username

        self.backButton = Button(self.master, text="Back",command=self.master.quit)
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
        if ~persons_exists(fname=MFN.get(),lname=MLN.get()):
            launchNewPerson(title=("Mother",MFN.get(),MLN.get()))
        if ~persons_exists(fname=FFN.get(),lname=FLN.get()):
            launchNewPerson(title=("Father",FFN.get(),FLN.get()))

        register_birth(fname=self.CFN.get(), lname=self.CLN.get(), gender=self.gender.get(),
        bdate=self.BD.get(), bplace=self.BP.get(), f_fname=FFN.get(), f_lname=FLN.get(),
        m_fname=self.MFN.get(), m_lname=self.MLN.get(), uid=self.username)

        pass

    def launchNewPerson(self, title):
        self.deconstructGrid()
        NewPersonGUI(master=self.master,title=title)
        self.master.mainloop()
        self.constructGrid()
        pass

class NewPersonGUI:
    """docstring for NewPersonGUI.
    Used when the parents of a child or one of the partners
    in a marriage don't exist in the Database"""

    def __init__(self, master, title):
        self.master = master
        self.title = title

        self.titleLabel = Label(self.master, text=title[0])
        self.FirstNameLabel = Label(self.master, text="First Name:")
        self.FNLabel = Label(self.master, text=title[1])
        self.LastNameLabel = Label(self.master, text="Last Name:")
        self.LNLabel = Label(self.master, text=title[2])
        self.
        pass
