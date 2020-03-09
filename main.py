from time import time, gmtime
import tkinter as tk
from models import Session, Account, Game

'''
To do:
- Stakes adden
'''


class App:
    def __init__(self, master, session):
        self.current_account = 0
        self.session = session
        self.acc_names = ["Account 1", "Account 2", "Account 3", "Account 4"] #Task 1 

        master.title("Hoki Poki 1.0")

        self.frame = tk.Frame(master)  # frame erscheint auf dem master
        self.frame.grid()  # grid erscheint auf frame

        if self.session == None:
            self.btn_start = tk.Button(
                self.frame, text="Start Session", command=lambda: self.start_session("test"))
            self.btn_start.grid(row=0, column=0)


    def start_session(self, sessionname, startbalance=0):
        self.session = Session(sessionname, time(), startbalance)
        self.btn_start.grid_forget()
        for i,element in enumerate(self.acc_names):
            self.session.add_account(element,i)

        for acc in self.session.accounts:
            acc.show(self.frame)

        print("Session startet at {}".format(gmtime(time())))  
        

    def save_session(self, session):
        # stores the session from the argument in a database
        ...

if __name__ == "__main__":
    session = None
    root = tk.Tk()
    #root.geometry("400x200+200+200")
    app = App(root, session)
    # heißt, dass das Fenster permanent geöffnet bleibt, bis es geschlossen wird.
    root.mainloop()

    # if user click "start new session"
    # session = startSession("name")
    # session.add_account("Per Flow")
    # session.add_account("Ralph")
    # print(session.name)
    # print(session.accounts[0].name)
