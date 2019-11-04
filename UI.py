from tkinter import *
from backend import *
import sys
import os

from AgentGUIs import *
from OfficerGUIs import *

def main():
    # if statments to check the database argument
    if (not 1 == len(sys.argv[1:])):
        print("Too few or too many arguments")
        return
    if not os.path.exists(sys.argv[1]):
        print("Argument doesn't exist")
        return

    # include: path = sys.argv[1] : in imported sql files for the globals

    #Construct root frame and set up the login
    root = Tk()
    LoginGUI(root)
    root.mainloop()

class LoginGUI:
    """docstring for LoginGUI.
    The GUI used for the login screen"""

    def __init__(self, master):
        self.master = master

        #initialize the ui elements
        self.titleLabel = Label(self.master, text="Registry Database Login:")
        self.usernameLabel = Label(self.master, text="Username:")
        self.passwordLabel = Label(self.master, text="Password:")

        self.closeButton = Button(self.master, text="Close", command=master.quit)
        self.loginButton = Button(self.master, text="Login", command=self.loginClick)

        self.usernameEntry = StringVar()
        self.userEntry = Entry(self.master, textvariable=self.usernameEntry)

        self.passwordEntry = StringVar()
        self.passEntry = Entry(self.master, textvariable=self.passwordEntry)

        self.constructGrid()

    def constructGrid(self):
        #Constructing the ui
        self.master.title("Login")

        self.titleLabel.grid(columnspan=4,rowspan=2)
        self.usernameLabel.grid(column=0,row=3)
        self.passwordLabel.grid(column=0,row=4)

        self.closeButton.grid(column=1,row=5)
        self.loginButton.grid(column=2,row=5)

        self.usernameEntry.set("")
        self.passwordEntry.set("")

        self.userEntry.grid(column=2,columnspan=2,row=3)
        self.passEntry.grid(column=2,columnspan=2,row=4)

    def deconstructGrid(self):
        #Used to temporarely distroy the ui
        self.titleLabel.grid_remove()
        self.usernameLabel.grid_remove()
        self.passwordLabel.grid_remove()
        self.closeButton.grid_remove()
        self.loginButton.grid_remove()
        self.userEntry.grid_remove()
        self.passEntry.grid_remove()

    def loginClick(self):
        #Called when user tries to login
        self.tempUsername = self.usernameEntry.get()

        #See if the user can login
        loginCall = login(username=self.tempUsername,password=self.passwordEntry.get())

        if(loginCall == 2): #no username
            self.usernameEntry.set("Invalid Username")
            self.passwordEntry.set("")
            return

        if(loginCall == 1): # not the right password
            self.passwordEntry.set("Invalid Password")
            return

        # Here the user is logged in: run their appropriate menu

        self.deconstructGrid()
        if(officer(self.usernameEntry.get())):
            OfficerMenuGUI(master=self.master, username=self.tempUsername)
        else:
            AgentMenuGUI(master=self.master, username=self.tempUsername)
        self.master.mainloop()

        # Here the user has logged out: rebuild the gui
        self.constructGrid()


class OfficerMenuGUI:
    """docstring for OfficerMenuGUI.
    The GUI used for the Officers menu"""

    def __init__(self, master, username):
        self.master = master
        self.username = username

        #initialize ui elements
        self.loginLabel = Label(self.master, text="User:")
        self.userLabel = Label(self.master, text=self.username)

        self.backButton = Button(self.master,text="LogOut",command=self.quit)

        self.ticketButton = Button(self.master,text="Issue a Ticket",command=self.ticket)
        self.ownerButton = Button(self.master,text="Find a Car Owner",command=self.owner)

        self.constructGrid()

    def constructGrid(self):
        #construct the ui
        self.master.title("Traffic Officer Menu")

        self.loginLabel.grid()
        self.backButton.grid(column=0,row=1)
        self.userLabel.grid(column=1,row=0)

        self.ticketButton.grid(column=1,row=1)
        self.ownerButton.grid(column=1,row=2)
        pass

    def deconstructGrid(self):
        #temporarely destroy the ui
        self.loginLabel.grid_remove()
        self.userLabel.grid_remove()
        self.backButton.grid_remove()
        self.ticketButton.grid_remove()
        self.ownerButton.grid_remove()
        pass

    def ticket(self):
        #Called to give a ticket: run the right gui
        self.deconstructGrid()
        TicketGUI(master=self.master,username=self.username)
        self.master.mainloop()

        #here they've exited to the this menu: reconstruct
        self.constructGrid()
        pass

    def owner(self):
        #Called to find the owner of a vehicle: run the right gui
        self.deconstructGrid()
        OwnerGUI(master=self.master,username=self.username)
        self.master.mainloop()

        #here they've exited to the this menu: reconstruct
        self.constructGrid()
        pass

    def quit(self):
        #Used to logout from this menu
        self.deconstructGrid()
        self.master.quit()
        pass


class AgentMenuGUI:
    """docstring for AgentMenuGUI.
    The GUI used for the Agents Menu"""

    def __init__(self, master, username):
        self.master = master
        self.username = username

        #initialize the ui elements
        self.loginLabel = Label(self.master, text="User:")
        self.userLabel = Label(self.master, text=self.username)

        self.backButton = Button(self.master,text="LogOut",command=self.quit)

        self.birthButton = Button(self.master,text="Register Birth",command=self.birth)
        self.marriageButton = Button(self.master,text="Register Marriage",command=self.marriage)
        self.registrationButton = Button(self.master,text="Renew Vehicle Resgistration",command=self.registration)
        self.saleButton = Button(self.master,text="Process Bill of Sale",command=self.sale)
        self.paymentButton = Button(self.master,text="Process Payment",command=self.payment)
        self.driverButton = Button(self.master, text="View Driver Abstract", command=self.driver)

        self.constructGrid()

    def constructGrid(self):
        #construct the ui
        self.master.title("Registry Agent Menu")

        self.loginLabel.grid()
        self.backButton.grid(column=0,row=1)
        self.userLabel.grid(column=1,row=0)
        self.birthButton.grid(column=1,row=1)
        self.marriageButton.grid(column=1,row=2)
        self.registrationButton.grid(column=1,row=3)
        self.saleButton.grid(column=1,row=4)
        self.paymentButton.grid(column=1,row=5)
        self.driverButton.grid(column=1,row=6)
        return

    def deconstructGrid(self):
        #temporarely destroy ui
        self.loginLabel.grid_remove()
        self.userLabel.grid_remove()
        self.backButton.grid_remove()
        self.birthButton.grid_remove()
        self.marriageButton.grid_remove()
        self.registrationButton.grid_remove()
        self.saleButton.grid_remove()
        self.paymentButton.grid_remove()
        self.driverButton.grid_remove()
        return

    def birth(self):
        #Called when asked to register a birth
        self.deconstructGrid()
        BirthGUI(master=self.master,username=self.username)
        self.master.mainloop()

        #here they've exited to the this menu: reconstruct
        self.constructGrid()
        pass

    def marriage(self):
        # Called when selected to register a marriage
        self.deconstructGrid()
        MarriageGUI(master=self.master,username=self.username)
        self.master.mainloop()

        #here they've exited to the this menu: reconstruct
        self.constructGrid()
        pass

    def registration(self):
        #Called when the agent selects renewing a registration
        self.deconstructGrid()
        RegistrationGUI(master=self.master,username=self.username)
        self.master.mainloop()

        #here they've exited to the this menu: reconstruct
        self.constructGrid()
        pass

    def sale(self):
        #Called to slect a bill of sale
        self.deconstructGrid()
        SaleGUI(master=self.master,username=self.username)
        self.master.mainloop()

        #here they've exited to the this menu: reconstruct
        self.constructGrid()
        pass

    def payment(self):
        #called to pay off a ticket
        self.deconstructGrid()
        PaymentGUI(master=self.master,username=self.username)
        self.master.mainloop()

        #here they've exited to the this menu: reconstruct
        self.constructGrid()
        pass

    def driver(self):
        #Called to find a driver abstract
        self.deconstructGrid()
        DriverGUI(master=self.master,username=self.username)
        self.master.mainloop()

        #here they've exited to the this menu: reconstruct
        self.constructGrid()
        pass

    def quit(self):
        #Called to log out of the menu
        self.deconstructGrid()
        self.master.quit()
        pass


if __name__ == "__main__":
    main()
