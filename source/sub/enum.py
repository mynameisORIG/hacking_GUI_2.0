#!/usr/bin/python3

import os,sys
from tkinter import *
from tkinter import ttk

window = Tk()
window.title('Hacking GUI Guide')
window.geometry("500x450")

class toolbar(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        #https://zetcode.com/tkinter/menustoolbars/
        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="File", menu=fileMenu)


        fileMenu1 = Menu(menubar)
        submenu = Menu(fileMenu1)
        fileMenu1.add_command(label="VPN", command=self.onExit)
        Sud0="sudo"
        submenu.add_command(label="use sudo", command=Sud0 )
        menubar.add_cascade(label="Settings", menu=fileMenu1)


    def onExit(self):

        self.quit()
toolbar()

def nmapButt():
    buttpage="source/subsub/nmap.py"

    def IP():
        IP = IPwid.get()
        IPstr=IP
        But1["text"]=IPstr
        #IP = StringVar()
        #def printinput(*args):
        #    print(IP.get())
        #IP.trace("w", printinput)
        #print(IP)

    IPwid = Entry(window, width=15,)
    IPwid.grid(row=0, column=450)
   

    labelText=StringVar()
    labelText.set("IP address:")
    labelDir=Label(window, textvariable=labelText, height=4)

    labelDir.grid(row=0,column=9)

    def cmd():
        nmapscanfolder="filecreation/nmap"
        os.system("chmod +x " + buttpage)
        os.system("nmap -sC -sV -T4 -p- -Pn " + IP + " | tee " + nmapscanfolder)
    But1 = ttk.Button(window, text="nmap", command=cmd)
    #But1.place(relx=0.00, y=00)
    But1.grid(row=0, column=1)
nmapButt()

window.mainloop()