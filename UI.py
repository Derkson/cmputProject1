from Tkinter import *
from backend import *

from AgentGUIs import *
from OfficerGUIs import *

def main():
    root = Tk()
    LoginGUI(root)
    root.mainloop()

class LoginGUI:
    def __init__(self, master):
        self.master = master

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
        self.master.title("Login")

        self.titleLabel.grid(columnspan=4,sticky=W+E+S+N,rowspan=2)
        self.usernameLabel.grid(column=0,row=3)
        self.passwordLabel.grid(column=0,row=4)

        self.closeButton.grid(column=1,row=5)
        self.loginButton.grid(column=2,row=5)

        self.usernameEntry.set("")
        self.passwordEntry.set("")

        self.userEntry.grid(column=2,columnspan=2,row=3)
        self.passEntry.grid(column=2,columnspan=2,row=4)

    def deconstructGrid(self):
        self.titleLabel.grid_remove()
        self.usernameLabel.grid_remove()
        self.passwordLabel.grid_remove()
        self.closeButton.grid_remove()
        self.loginButton.grid_remove()
        self.userEntry.grid_remove()
        self.passEntry.grid_remove()

    def loginClick(self):
        self.tempUsername = self.usernameEntry.get()
        loginCall = login(username=self.tempUsername,password=self.passwordEntry.get())

        if(loginCall == 2):
            self.usernameEntry.set("Invalid Username")
            self.passwordEntry.set("")
            return

        if(loginCall == 1):
            self.passwordEntry.set("Invalid Password")
            return

        # Here the user is logged in

        self.deconstructGrid()
        if(officer(self.usernameEntry.get())):
            OfficerMenuGUI(master=self.master, username=self.tempUsername)
        else:
            AgentMenuGUI(master=self.master, username=self.tempUsername)
        self.master.mainloop()
        self.constructGrid()


class OfficerMenuGUI:
    def __init__(self, master, username):
        self.master = master
        self.username = username

        self.loginLabel = Label(self.master, text="User:")
        self.userLabel = Label(self.master, text=self.username)

        self.backButton = Button(self.master,text="LogOut",command=self.quit)

        self.ticketButton = Button(self.master,text="Issue a Ticket",command=self.ticket)
        self.ownerButton = Button(self.master,text="Find a Car Owner",command=self.owner)

        self.constructGrid()

    def constructGrid(self):
        self.master.title("Traffic Officer Menu")

        self.loginLabel.grid()
        self.backButton.grid(column=0,row=1)
        self.userLabel.grid(column=1,row=0)

        self.ticketButton.grid(column=1,row=1)
        self.ownerButton.grid(column=1,row=2)
        pass

    def deconstructGrid(self):
        self.loginLabel.grid_remove()
        self.userLabel.grid_remove()
        self.backButton.grid_remove()
        self.ticketButton.grid_remove()
        self.ownerButton.grid_remove()
        pass

    def ticket(self):
        pass

    def owner(self):
        pass

    def quit(self):
        self.deconstructGrid()
        self.master.quit()
        pass


class AgentMenuGUI:
    def __init__(self, master, username):
        self.master = master
        self.username = username

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
        self.deconstructGrid()
        BirthGUI(master=self.master,username=self.username)
        self.master.mainloop()
        self.constructGrid()
        pass

    def marriage(self):
        self.deconstructGrid()
        MarriageGUI(master=self.master,username=self.username)
        self.master.mainloop()
        self.constructGrid()
        pass

    def registration(self):
        self.deconstructGrid()
        RegistrationGUI(master=self.master,username=self.username)
        self.master.mainloop()
        self.constructGrid()
        pass

    def sale(self):
        pass

    def payment(self):
        pass

    def driver(self):
        pass

    def quit(self):
        self.deconstructGrid()
        self.master.quit()
        pass


if __name__ == "__main__":
    main()
