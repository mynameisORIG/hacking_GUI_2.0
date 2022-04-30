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


def VPN():
    OP1 = [
    "VPN Options",
    "Hack The Box",
    "Proving Ground",
    "Try Hack Me"
    ]

    def VPNopt(val):
        if val == "Hack The Box":
            # put Hack The Box VPN location here
            os.system("sudo openvpn /home/git/HTB_Notes_writeups/mynameis0rig.ovpn &")
        elif val == "Proving Ground":
            # put Proving Grounds VPN location here
            os.system("sudo openvpn /home/git/PG/pg.ovpn &")
        elif val == "Try Hack Me":
            os.system("openvpn /home/git/OSCP_Lab_Attack/THM/mynameis.ovpn &")

    VPN = StringVar(window)
    VPN.set(OP1[0])

    drop = OptionMenu( window , VPN , *OP1, command=VPNopt)
    #drop.pack()
    drop.place(relx=0.80, y=0, anchor='nw')

#def nmap():
#    os.system("nmap -sC -sV -T4 -p- -Pn " + window)

def enumButt():
    def cmd():
        buttpage="source/sub/enum.py"
        os.system("chmod +x " + buttpage)
        os.system(buttpage)
    But1 = ttk.Button(window, text="Enum", command=cmd)
    But1.place(relx=0.00, y=0, )

def shellButt():
    buttpage="source/sub/shell.py"
    def cmd():
        os.system("chmod +x " + buttpage)
        os.system(buttpage)
    But1 = ttk.Button(window, text="Shell", command=cmd)
    But1.place(relx=0.00, y=50)
