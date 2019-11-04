from tkinter import *
from backend import *
from officer import *

class TicketGUI:
    """docstring for TicketGUI.
    Used for issuing a ticket."""

    def __init__(self, master, username):
        self.master = master
        self.username = username

        #initialize the ui elements
        self.backButton = Button(self.master, text="Back",command=self.quit)
        self.vehicleButton = Button(self.master, text="See Vehicle Info",command=self.vehicleCall)
        self.ticketButton = Button(self.master, text="Enter Ticket?",command=self.ticketCall)
        self.submitButton = Button(self.master, text="Submit",command=self.submitCall)

        self.RegistrationLabel = Label(self.master, text="RegNo:")
        self.Registration = StringVar()
        self.RegistrationEntry = Entry(self.master, textvariable=self.Registration)

        self.Regno = StringVar()
        self.RegnoLabel = Label(self.master)
        self.FN = StringVar()
        self.FirstNameLabel = Label(self.master, text="First Name:")
        self.FNLabel = Label(self.master)
        self.LN = StringVar()
        self.LastNameLabel = Label(self.master, text="Last Name:")
        self.LNLabel = Label(self.master)
        self.Make = StringVar()
        self.VehicleMakeLabel = Label(self.master, text="Vehicle Make:")
        self.MakeLabel = Label(self.master)
        self.Model = StringVar()
        self.VehicleModelLabel = Label(self.master, text="Vehicle Model:")
        self.ModelLabel = Label(self.master)
        self.Year = StringVar()
        self.VehicleYearLabel = Label(self.master, text="Vehicle Year:")
        self.YearLabel = Label(self.master)
        self.Color = StringVar()
        self.VehicleColorLabel = Label(self.master, text="Vehicle Color:")
        self.ColorLabel = Label(self.master)

        self.Date = StringVar()
        self.Date.set("YYYY-MM-DD")
        self.DateLabel = Label(self.master, text="Ticket Date:")
        self.DateEntry = Entry(self.master, textvariable=self.Date)
        self.Text = StringVar()
        self.Text.set("")
        self.TextLabel = Label(self.master, text="Ticket Reason:")
        self.TextEntry = Entry(self.master, textvariable=self.Text)
        self.Amount = StringVar()
        self.Amount.set("")
        self.AmountLabel = Label(self.master, text="Ticket Amount:")
        self.AmountEntry = Entry(self.master, textvariable=self.Amount)


        self.constructGrid()
        pass

    def constructGrid(self):
        # construct the initial ui elements
        self.master.title("Insert Vehicle Registration Number")

        self.backButton.grid()
        self.vehicleButton.grid(column=1,row=0)

        self.RegistrationLabel.grid(column=0,row=1)
        self.Registration.set("")
        self.RegistrationEntry.grid(column=1,row=1)
        pass

    def deconstructGrid(self):
        #temporarely destroys all of the ui elements
        self.backButton.grid_remove()
        self.vehicleButton.grid_remove()
        self.ticketButton.grid_remove()
        self.submitButton.grid_remove()

        self.RegistrationLabel.grid_remove()
        self.RegistrationEntry.grid_remove()

        self.RegnoLabel.grid_remove()
        self.FirstNameLabel.grid_remove()
        self.FNLabel.grid_remove()
        self.LastNameLabel.grid_remove()
        self.LNLabel.grid_remove()
        self.VehicleMakeLabel.grid_remove()
        self.MakeLabel.grid_remove()
        self.VehicleModelLabel.grid_remove()
        self.ModelLabel.grid_remove()
        self.VehicleYearLabel.grid_remove()
        self.YearLabel.grid_remove()
        self.VehicleColorLabel.grid_remove()
        self.ColorLabel.grid_remove()

        self.DateLabel.grid_remove()
        self.DateEntry.grid_remove()
        self.TextLabel.grid_remove()
        self.TextEntry.grid_remove()
        self.AmountLabel.grid_remove()
        self.AmountEntry.grid_remove()
        pass

    def vehicleCall(self):
        # used to see if the vehicle is in the database and find the data
        try:
            if not regno_exists(int(self.Registration.get())):
                self.Registration.set("RegNo not in Database")
                return
        except ValueError:
            self.Registration.set("Not a number")
            return

        #Here the regno is valid: get the info and construct the new ui elements
        self.Regno = self.Registration.get()
        self.info = get_regno_info(int(self.Regno))
        self.FN = str(self.info[0])
        self.LN = str(self.info[1])
        self.Make = str(self.info[2])
        self.Model = str(self.info[3])
        self.Color = str(self.info[4])
        self.Year = str(self.info[5])

        self.RegnoLabel.config(text=self.Regno)
        self.FNLabel.config(text=self.FN)
        self.LNLabel.config(text=self.LN)
        self.MakeLabel.config(text=self.Make)
        self.ModelLabel.config(text=self.Model)
        self.YearLabel.config(text=self.Year)
        self.ColorLabel.config(text=self.Color)

        self.RegistrationEntry.grid_remove()
        self.RegnoLabel.grid(column=1,row=1)

        self.vehicleButton.grid_remove()
        self.ticketButton.grid(column=1,row=0)

        self.FirstNameLabel.grid(column=0,row=2)
        self.FNLabel.grid(column=1,row=2)
        self.LastNameLabel.grid(column=0,row=3)
        self.LNLabel.grid(column=1,row=3)
        self.VehicleMakeLabel.grid(column=0,row=4)
        self.MakeLabel.grid(column=1,row=4)
        self.VehicleModelLabel.grid(column=0,row=5)
        self.ModelLabel.grid(column=1,row=5)
        self.VehicleYearLabel.grid(column=0,row=6)
        self.YearLabel.grid(column=1,row=6)
        self.VehicleColorLabel.grid(column=0,row=7)
        self.ColorLabel.grid(column=1,row=7)
        pass

    def ticketCall(self):
        # here the user want to give them a ticket: open up the ticket ui elements
        self.ticketButton.grid_remove()
        self.submitButton.grid(column=1,row=0)

        self.DateLabel.grid(column=2,row=1)
        self.DateEntry.grid(column=3,row=1)
        self.TextLabel.grid(column=2,row=3)
        self.TextEntry.grid(column=3,row=3)
        self.AmountLabel.grid(column=2,row=2)
        self.AmountEntry.grid(column=3,row=2)
        pass

    def submitCall(self):
        # Here the user is submiting a ticket
        try:
            issue_ticket(regno=int(self.Regno), violation=self.Text.get(), fine=int(self.Amount.get()), vdate=self.Date.get())
        except ValueError:
            self.Amount.set("Not a number")
            return
        self.submitButton.grid_remove()
        self.Amount.set("Complete")
        pass

    def quit(self):
        self.deconstructGrid()
        self.master.quit()
        pass

class OwnerGUI:
    """docstring for OwnerGui.
    Used for finding a vehicles owner"""

    def __init__(self, master, username):
        self.master = master
        self.username = username

        # initialize the ui elements
        self.backButton = Button(self.master, text="Back",command=self.quit)
        self.submitButton = Button(self.master, text="Submit",command=self.submitCall)

        self.InstructLabel = Label(self.master, text="Insert One or More:")

        self.Plate = StringVar()
        self.PlateLabel = Label(self.master, text="Vehicle Plate:")
        self.PlateEntry = Entry(self.master, textvariable=self.Plate)
        self.Make = StringVar()
        self.MakeLabel = Label(self.master, text="Vehicle Make:")
        self.MakeEntry = Entry(self.master, textvariable=self.Make)
        self.Model = StringVar()
        self.ModelLabel = Label(self.master, text="Vehicle Model:")
        self.ModelEntry = Entry(self.master, textvariable=self.Model)
        self.Year = StringVar()
        self.YearLabel = Label(self.master, text="Vehicle Year:")
        self.YearEntry = Entry(self.master, textvariable=self.Year)
        self.Color = StringVar()
        self.ColorLabel = Label(self.master, text="Vehicle Color:")
        self.ColorEntry = Entry(self.master, textvariable=self.Color)

        self.constructGrid()
        pass

    def constructGrid(self):
        self.master.title("Find Vehicle Owner")

        self.backButton.grid(column=0,row=0)
        self.submitButton.grid(column=1,row=0)

        self.InstructLabel.grid(column=0,row=1,columnspan=2)

        self.PlateLabel.grid(column=0,row=2)
        self.PlateEntry.grid(column=1,row=2)
        self.MakeLabel.grid(column=0,row=3)
        self.MakeEntry.grid(column=1,row=3)
        self.ModelLabel.grid(column=0,row=4)
        self.ModelEntry.grid(column=1,row=4)
        self.YearLabel.grid(column=0,row=5)
        self.YearEntry.grid(column=1,row=5)
        self.ColorLabel.grid(column=0,row=6)
        self.ColorEntry.grid(column=1,row=6)
        pass

    def deconstructGrid(self):
        self.backButton.grid_remove()
        self.submitButton.grid_remove()

        self.InstructLabel.grid_remove()

        self.PlateLabel.grid_remove()
        self.PlateEntry.grid_remove()
        self.MakeLabel.grid_remove()
        self.MakeEntry.grid_remove()
        self.ModelLabel.grid_remove()
        self.ModelEntry.grid_remove()
        self.YearLabel.grid_remove()
        self.YearEntry.grid_remove()
        self.ColorLabel.grid_remove()
        self.ColorEntry.grid_remove()
        pass

    def submitCall(self):
        # TODO: complete the list
        self.list = find_car_owner(make=self.Make.get(), model=self.Model.get(), year=self.Year.get(),
        color=self.Color.get(), plate=self.Plate.get())
        pass

    def quit(self):
        self.deconstructGrid()
        self.master.quit()
        pass
