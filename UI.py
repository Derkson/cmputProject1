from Tkinter import *
from backend import *


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
        loginCall = login(username=self.usernameEntry.get(),password=self.passwordEntry.get())

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
            OfficerMenuGUI(self.master, self.usernameEntry.get())
        else:
            AgentMenuGUI(self.master, self.usernameEntry.get())
        self.master.mainloop()
        self.constructGrid()


class OfficerMenuGUI:
    def __init__(self, master, username):
        self.master = master
        self.username = username
        self.closeButton = Button(self.master, text="Close", command=self.back)
        self.closeButton.grid()

    def back(self):
        self.closeButton.grid_forget()
        self.master.quit()


class AgentMenuGUI:
    def __init__(self, master, username):
        self.master = master
        self.username = username

        self.loginLabel = Label(self.master, text="User:")
        self.userLabel = Label(self.master, text=self.username)

        self.birthButton = Button(self.master,text="Register Birth",command=self.birth)
        self.marriageButton = Button(self.master,text="Register Marriage",command=self.marriage)
        self.registrationButton = Button(self.master,text="Renew Vehicle Resgistration",command=self.registration)
        self.saleButton = Button(self.master,text="Process Bill of Sale",command=self.sale)
        self.paymentButton = Button(self.master,text="Process Payment",command=self.payment)
        self.driverButton = Button(self.master, text="View Driver Abstract", command=self.driver)

        self.constructGrid()

    def constructGrid(self):
        return


if __name__ == "__main__":
    main()
