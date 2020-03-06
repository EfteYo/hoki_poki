from time import time, gmtime
import tkinter as tk
from models import Session, Account, Game

'''
To do:
-Accounts in-app generieren
-Stakes adden
'''

class App:
    def __init__(self, master, session):
        self.session = session
        self.acc_names = ["Account 1", "Account 2"] #Task 1 

        master.title("Hoki Poki 1.0")

        self.frame = tk.Frame(master)  # frame erscheint auf dem master
        self.frame.grid()  # grid erscheint auf frame

        if self.session == None:
            self.btn_start = tk.Button(
                self.frame, text="Start Session", command=lambda: self.start_session("test"))
            self.btn_start.grid(row=0, column=0)
        else:
            self.init_gui()

    def init_gui(self):
        self.acc_tabs = []
        i = 0
        for account in self.session.accounts:
            tab = tk.Button(self.frame, text=account.name, command=lambda: self.start_game())
            tab.grid(row=i, column=0)
            self.acc_tabs.append(tab)
            i += 1

        tab = tk.Button(self.frame, text="New Account")
        tab.grid(row=i, column=0)
        self.acc_tabs.append(tab)

    def start_session(self, sessionname, startbalance=0):
        self.session = Session(sessionname, time(), startbalance)
        self.btn_start.grid_forget()
        for element in self.acc_names:
            self.session.add_account(element)
        self.init_gui()
        print("Session startet at {}".format(gmtime(time())))

    def start_game(self):
        self.btn_new_game = tk.Button(
            self.frame, text = "Start Game" # add command
        )
        self.btn_new_game.grid(row=0, column=1)
        self.session.accounts[0].add_game(time(),42) #add stakes



    def save_session(self, session):
        # stores the session from the argument in a database
        ...

    def print_accounts(self, session):
        ...

def test():
    ...

if __name__ == "__main__":
    session = None
    root = tk.Tk()
    root.geometry("400x200+200+200")
    app = App(root, session)
    # heißt, dass das Fenster permanent geöffnet bleibt, bis es geschlossen wird.
    root.mainloop()

    # if user click "start new session"
    # session = startSession("name")
    # session.add_account("Per Flow")
    # session.add_account("Ralph")
    # print(session.name)
    # print(session.accounts[0].name)
