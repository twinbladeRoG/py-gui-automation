import tkinter as tk
import re as reg
import requests
import threading
import send_sms
# %%
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.grid(sticky=tk.N+tk.S+tk.E+tk.W)
        self.createWidgets()

    def createWidgets(self):
      pass

# %%
root = tk.Tk()
root.geometry('800x500')
root["bg"] = "red"
app = Application(master=root)
app.master.title("GUI Automation")
app.mainloop()
