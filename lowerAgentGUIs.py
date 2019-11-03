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
        if not persons_exists(fname=self.title[1], lname=self.title[2]):
            self.phone.set("ERROR: Person not made")
            return
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
        self.info = driver_abstract(self.driver[0],self.driver[1])
        self.length = self.info[0][0]
        if self.length == 0:
            self.tickets = ()
        else:
            self.tickets = self.info[4]
        self.offset = 0

        self.backButton = Button(self.master, text="Back",command=self.quit)
        self.TicketsButton = Button(self.master, text="View Tickets",command=self.viewTickets)
        self.decButton = Button(self.master, text="<<<",command=self.decCall)
        self.incButton = Button(self.master, text=">>>",command=self.incCall)

        self.TicketNumLabel = Label(self.master, text=("Number of Tickets: " + str(self.info[0][0])))
        self.NoticesNumLabel = Label(self.master, text=("Number of Demerit Notices: " + str(self.info[1][0])))
        self.DemeritTotalLabel = Label(self.master, text=("Total Demerit Points: " + str(self.info[1][1])))
        self.DemeritPastLabel = Label(self.master, text=("Points from the Past 2 Years: " + str(self.info[3][1])))

        self.labelLabels = (Label(self.master,text="Ticket Num:"),
        Label(self.master,text="Date:"),
        Label(self.master,text="Violation Reason:"),
        Label(self.master,text="Ticket Fine:"),
        Label(self.master,text="Vehicle Make:"),
        Label(self.master,text="Vehicle Model:"))

        for i in range(self.length):
            for j in range(6):
                self.ticketLabels[(6*i)+j] = Label(self.master, text=self.tickets[i][j])
            pass

        self.constructGrid()
        pass

    def constructGrid(self):
        self.master.title("Driver: " + self.driver[0] + " " + self.driver[1])

        self.backButton.grid()
        self.TicketsButton.grid(column=1,row=0)

        self.TicketNumLabel.grid(column=0,columnspan=2,row=1)
        self.NoticesNumLabel.grid(column=0,columnspan=2,row=2)
        self.DemeritTotalLabel.grid(column=0,columnspan=2,row=3)
        self.DemeritPastLabel.grid(column=0,columnspan=2,row=4)
        pass

    def deconstructGrid(self):
        self.backButton.grid_remove()
        self.TicketsButton.grid_remove()

        self.TicketNumLabel.grid_remove()
        self.NoticesNumLabel.grid_remove()
        self.DemeritTotalLabel.grid_remove()
        self.DemeritPastLabel.grid_remove()
        self.incButton.grid_remove()
        self.decButton.grid_remove()
        self.removeTickets()
        pass

    def viewTickets(self):
        self.TicketsButton.grid_remove()
        if self.length > 5:
            self.incButton.grid(column=4,row=0)
            pass
        refreshTickets()
        pass

    def removeTickets(self):
        for i in self.ticketLabels:
            i.grid_remove()
        for i in range(6):
            self.labelLabels[i].grid_remove()
        pass

    def refreshTickets(self):
        self.removeTickets()

        for i in range(min(5,self.length-self.offset)):
            for j in range(6):
                self.labelLabels[j].grid(column=2,row=(1+(6*i)+j))
                self.ticketLabels[(6*i)+j+self.offset].grid(column=3,row=(1+(6*i)+j))
        pass

    def incCall(self):
        self.offset += 5
        if 5 >= self.length - self.offset:
            self.incButton.grid_remove()
        self.decButton.grid(column=3,row=0)
        refreshTickets()
        pass

    def decCall(self):
        self.offset -= 5
        if 5 > self.offset:
            self.decButton.grid_remove()
        self.incButton.grid(column=4,row=0)
        refreshTickets()
        pass

    def quit(self):
        self.deconstructGrid()
        self.master.quit()
        pass
