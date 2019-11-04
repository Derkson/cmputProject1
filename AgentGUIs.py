from tkinter import *
from backend import *
from validation import *
from agent import *
from create import *
from lowerAgentGUIs import *

class BirthGUI:
    """docstring for BirthGUI.
    The GUI used when registering a birth"""

    def __init__(self, master, username):
        self.master = master
        self.username = username

        #initialize the ui elements
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
        #Construct the ui
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
        #temporarely destroy the ui
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
        #called to submit the birth
        self.mother = (self.MFN.get(),self.MLN.get())
        self.father = (self.FFN.get(),self.FLN.get())

        #check and see if the parents need to be created
        if not persons_exists(fname=self.mother[0],lname=self.mother[1]):
            self.launchNewPerson(title=("Mother",self.mother[0],self.mother[1]))
        if not persons_exists(fname=self.father[0],lname=self.father[1]):
            self.launchNewPerson(title=("Father",self.father[0],self.father[1]))

        #run the registration function and check if the date is wrong
        if (0 == register_birth(fname=self.CFN.get(), lname=self.CLN.get(), gender=self.gender.get(),
        bdate=self.BD.get(), bplace=self.BP.get(), f_fname=self.FFN.get(), f_lname=self.FLN.get(),
        m_fname=self.MFN.get(), m_lname=self.MLN.get(), uid=self.username)):
            self.BD.set("Date in the future")
            return

        #success
        self.quit()
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
        #temporarely destroy the ui
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
        #Called to submit the marriage
        self.first = (self.FirstFN.get(),self.FirstLN.get())
        self.second = (self.SecondFN.get(),self.SecondLN.get())

        # check and see if the partners need to be created
        if not persons_exists(fname=self.first[0],lname=self.first[1]):
            self.launchNewPerson(title=("First Partner",self.first[0],self.first[1]))
            if not persons_exists(self.first[0],self.first[1]):
                self.FirstFN.set("Aborted Marriage")
                return
        if not persons_exists(fname=self.second[0],lname=self.second[1]):
            self.launchNewPerson(title=("Second Partner",self.second[0],self.second[1]))
            if not persons_exists(self.second[0],self.second[1]):
                self.FirstFN.set("Aborted Marriage")
                return

        #Register the marriage
        register_marriage(p1_fname=self.FirstFN.get(), p1_lname=self.FirstLN.get(), p2_fname=self.SecondFN.get(),
        p2_lname=self.SecondLN.get(), uid=self.username)
        self.quit()
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

        #initialize the ui elements
        self.backButton = Button(self.master, text="Back",command=self.quit)
        self.submitButton = Button(self.master, text="Submit",command=self.submitCall)

        self.RegistrationLabel = Label(self.master, text="RegNo:")

        self.Registration = StringVar()
        self.RegistrationEntry = Entry(self.master, textvariable=self.Registration)

        self.constructGrid()
        pass

    def constructGrid(self):
        #Construct the ui
        self.master.title("Renew Vehicle Registration")

        self.backButton.grid()
        self.submitButton.grid(column=1,row=0)

        self.RegistrationLabel.grid(column=0,row=2)

        self.Registration.set("")
        self.RegistrationEntry.grid(column=1,row=2)
        pass

    def deconstructGrid(self):
        #temporarely destroy the ui
        self.backButton.grid_remove()
        self.submitButton.grid_remove()

        self.RegistrationLabel.grid_remove()
        self.RegistrationEntry.grid_remove()
        pass

    def submitCall(self):
        #Called to submit the regno
        try:
            if not regno_exists(int(self.Registration.get())):
                self.Registration.set("Invalid RegNo")
                return
        except ValueError: # failed to convert to int
            self.Registration.set("Not a number")
            return

        #success
        renew_vehicle(self.Registration.get())
        self.Registration.set("Success")
        pass

    def quit(self):
        self.deconstructGrid()
        self.master.quit()
        pass

class SaleGUI:
    """docstring for SaleGUI.
    Used for processing a vehicle sale"""

    def __init__(self, master, username):
        self.master = master
        self.username = username

        #initialize the ui elements
        self.backButton = Button(self.master, text="Back",command=self.quit)
        self.submitButton = Button(self.master, text="Submit",command=self.submitCall)

        self.VINLabel = Label(self.master, text="Vehicle VIN:")
        self.SFNameLabel = Label(self.master, text="Seller Fist Name:")
        self.SLNameLabel = Label(self.master, text="Seller Last Name:")
        self.BFNameLabel = Label(self.master, text="Buyer Fist Name:")
        self.BLNameLabel = Label(self.master, text="Buyer Last Name:")
        self.PlateLabel = Label(self.master, text="New Plate Number:")

        self.VIN = StringVar()
        self.SFN = StringVar()
        self.SLN = StringVar()
        self.BFN = StringVar()
        self.BLN = StringVar()
        self.Plate = StringVar()
        self.VINEntry = Entry(self.master, textvariable=self.VIN)
        self.SFNEntry = Entry(self.master, textvariable=self.SFN)
        self.SLNEntry = Entry(self.master, textvariable=self.SLN)
        self.BFNEntry = Entry(self.master, textvariable=self.BFN)
        self.BLNEntry = Entry(self.master, textvariable=self.BLN)
        self.PlateEntry = Entry(self.master, textvariable=self.Plate)

        self.constructGrid()
        pass

    def constructGrid(self):
        self.master.title("Bill of Sale")

        self.backButton.grid()
        self.submitButton.grid(column=1,row=0)

        self.VINLabel.grid(column=0,row=1)
        self.SFNameLabel.grid(column=0,row=2)
        self.SLNameLabel.grid(column=0,row=3)
        self.BFNameLabel.grid(column=0,row=4)
        self.BLNameLabel.grid(column=0,row=5)
        self.PlateLabel.grid(column=0,row=6)

        self.VIN.set("")
        self.SFN.set("")
        self.SLN.set("")
        self.BFN.set("")
        self.BLN.set("")
        self.Plate.set("")
        self.VINEntry.grid(column=1,row=1)
        self.SFNEntry.grid(column=1,row=2)
        self.SLNEntry.grid(column=1,row=3)
        self.BFNEntry.grid(column=1,row=4)
        self.BLNEntry.grid(column=1,row=5)
        self.PlateEntry.grid(column=1,row=6)
        pass

    def deconstructGrid(self):

        self.backButton.grid_remove()
        self.submitButton.grid_remove()

        self.VINLabel.grid_remove()
        self.SFNameLabel.grid_remove()
        self.SLNameLabel.grid_remove()
        self.BFNameLabel.grid_remove()
        self.BLNameLabel.grid_remove()
        self.PlateLabel.grid_remove()

        self.VINEntry.grid_remove()
        self.SFNEntry.grid_remove()
        self.SLNEntry.grid_remove()
        self.BFNEntry.grid_remove()
        self.BLNEntry.grid_remove()
        self.PlateEntry.grid_remove()
        pass

    def submitCall(self):
        if not vin_exists(vin=self.VIN.get()): #Vehicle doesn't exist
            self.VIN.set("VIN not in database")
            return

        if not persons_exists(fname=self.SFN.get(),lname=self.SLN.get()):
            self.SFN.set("Seller not in database")
            self.SLN.set("")
            return

        if not persons_exists(fname=self.BFN.get(),lname=self.BLN.get()):
            self.BFN.set("Buyer not in database")
            self.BLN.set("")
            return

        if not is_current_owner(fname=self.SFN.get(),lname=self.SLN.get(),vin=self.VIN.get()):
            self.SFN.set("Seller not the owner")
            self.SLN.set("")
            return

        #success
        bill_of_sale(vin=self.VIN.get(), o_fname=self.SFN.get(), o_lname=self.SLN.get(),
        new_fname=self.BFN.get(), new_lname=self.BLN.get(), newplate=self.Plate.get())
        self.quit()
        pass

    def quit(self):
        self.deconstructGrid()
        self.master.quit()
        pass

class PaymentGUI:
    """docstring for PaymentGUI.
    Used to pay for a ticket"""

    def __init__(self, master, username):
        self.master = master
        self.username = username

        #initialize the ui elements
        self.backButton = Button(self.master, text="Back",command=self.quit)
        self.submitButton = Button(self.master, text="Submit",command=self.submitCall)

        self.TicketLabel = Label(self.master, text="Ticket Number:")
        self.AmountLabel = Label(self.master, text="Amount Paid:")

        self.Ticket = StringVar()
        self.Amount = StringVar()
        self.TicketEntry = Entry(self.master, textvariable=self.Ticket)
        self.AmountEntry = Entry(self.master, textvariable=self.Amount)

        self.constructGrid()
        pass

    def constructGrid(self):
        self.master.title("Ticket Payment")

        self.backButton.grid()
        self.submitButton.grid(column=1,row=0)

        self.TicketLabel.grid(column=0,row=1)
        self.AmountLabel.grid(column=0,row=2)

        self.Ticket.set("")
        self.Amount.set("")
        self.TicketEntry.grid(column=1,row=1)
        self.AmountEntry.grid(column=1,row=2)
        pass

    def deconstructGrid(self):

        self.backButton.grid_remove()
        self.submitButton.grid_remove()

        self.TicketLabel.grid_remove()
        self.AmountLabel.grid_remove()

        self.TicketEntry.grid_remove()
        self.AmountEntry.grid_remove()
        pass

    def submitCall(self):
        try: # to process the payment
            self.return = process_payment(tno=int(self.Ticket.get()),amount=int(self.Amount.get()))
            if self.return == 1: # When the amount is over the current
                self.Amount.set("Paying too much")
                return
            if self.return == 0: #When the amount is negative
                self.Amount.set("No negatives")
                return

        except ValueError: # failed to convert to int
            self.Ticket.set("Not a number")
            self.Amount.set("")
            return

        #success
        self.quit()
        pass

    def quit(self):
        self.deconstructGrid()
        self.master.quit()
        pass

class DriverGUI:
    """docstring for DriverGUI
    Called for getting a drivers abstract"""

    def __init__(self, master, username):
        self.master = master
        self.username = username

        #Construct the ui elements
        self.backButton = Button(self.master, text="Back",command=self.quit)
        self.submitButton = Button(self.master, text="Submit",command=self.submitCall)

        self.FirstNameLabel = Label(self.master, text="First Name:")
        self.LastNameLabel = Label(self.master, text="Last Name:")

        self.FN = StringVar()
        self.FNEntry = Entry(self.master, textvariable=self.FN)
        self.LN = StringVar()
        self.LNEntry = Entry(self.master, textvariable=self.LN)

        self.constructGrid()
        pass

    def constructGrid(self):
        self.master.title("Get Driver Abstract")

        self.backButton.grid()
        self.submitButton.grid(column=1,row=0)

        self.FirstNameLabel.grid(column=0,row=1)
        self.LastNameLabel.grid(column=0,row=2)

        self.FN.set("")
        self.FNEntry.grid(column=1,row=1)
        self.LN.set("")
        self.LNEntry.grid(column=1,row=2)
        pass

    def deconstructGrid(self):

        self.backButton.grid_remove()
        self.submitButton.grid_remove()

        self.FirstNameLabel.grid_remove()
        self.LastNameLabel.grid_remove()

        self.FNEntry.grid_remove()
        self.LNEntry.grid_remove()
        pass

    def submitCall(self):
        if not persons_exists(fname=self.FN.get(),lname=self.LN.get()):
            self.FN.set("Driver not in database")
            self.LN.set("")
            return

        # Driver in database: run the abstract
        self.deconstructGrid()
        DriverAbstractGUI(master=self.master,username=self.username,driver=(self.FN.get(),self.LN.get()))
        self.master.mainloop()

        # Here the user has come back
        self.master.quit()
        pass

    def quit(self):
        self.deconstructGrid()
        self.master.quit()
        pass
