from email import message
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter
# from tkinter import tkFileDialog
import tkinter.filedialog
# or
from tkinter import filedialog
from traceback import print_tb
from typing import List
import xml.etree.ElementTree as ET
# from signal import pthread_kill, SIGTSTP
import threading
import configparser
import os.path
import os
from lang import change_lang as change

import time

import sqlite3
import csv
from numpy import *
from datetime import datetime

from tendo import singleton
me = singleton.SingleInstance()





class language_pack():
    def get_language():
        global config_obj
        global default
        global language
        filename = "language.xml"
        tree = ET.parse(filename)
        root = tree.getroot()
        loc = 'language.ini'
        config_obj = configparser.ConfigParser()
        config_obj.read(loc) 
        default = 'English'
        language = root[0][1].text

    def read__langpack(objname):
        global lista
        lista = []
        x = 0
        size = 100
        error = 0
        localdir = config_obj[objname]
        for x in range(size):
            try:
                z = str(x)
                lista.append(localdir[z])
            except Exception:
                error =+1
        if error > 0:
            lista = []
            x = 0
            localdir = config_obj[default]
            for x in range(size):
                z = str(x)
                lista.append(localdir[z])
        else:
            # print("pass")
            pass
    
    def check_language(name):
        if name == 'English':
            language_pack.read__langpack(name)
            return 0
        elif name == 'Serbian':
            try:
                language_pack.read__langpack(name)
            except KeyError:
                language_pack.read__langpack('English')
            return 0
        elif name == 'Spanish':
            try:
                language_pack.read__langpack(name)
            except KeyError:
                language_pack.read__langpack('English')
            return 0
        else:
            language_pack.read__langpack('English')
            return 0

    def replace_lang(jazik):
        change(jazik)

class front_end():
    def main_window():
        global root
        global menubar
        root = Tk()
        root.title('Roletnica')
        
        my_canvas = Canvas(root, width=855, height=600)
        my_canvas.pack(expand= True)

        root.geometry('855x600')
        root.minsize(855,600)
        root.maxsize(855,600)
        # photo = PhotoImage(file = "blind.ico")
        # root.iconphoto(False, photo)

        # bg = PhotoImage(file = "bg-blue-green-lime.png")
        # my_label = Label(root, image=bg)
        # my_label.place(x=-600, y=0) 
        front_end.head_bar()
        mainloop()  

    def window_1():
        bbgcolor = ("#009D94")              # boja polja
        bfgcolor = ("white")                # slova
        bgcolorentrfield = ("#A2D9CE")      # entry field
        bgcolorletter = ("black")           # slova 
        fstylelabel = ('Verdana', 20)       # font labela
        fstyleentry = ('Verdana', 25)       # font entry

        Sirina_text = StringVar()

        Sirina_label = Label(root, text=lista[10], font=fstylelabel, width=7,padx=20,pady=5 ,bg=bbgcolor, fg = bfgcolor ,borderwidth=0)
        Sirina_label.place(x=30, y=30)

        Sirina_entry = Entry(root, textvariable=Sirina_text, font=fstyleentry,width=7, bg=bgcolorentrfield, fg = bgcolorletter,borderwidth=0)
        Sirina_entry.place(x=205, y=30)

        Visina_text = StringVar()

        Visina_label = Label(root, text=lista[11], font=fstylelabel, width=7,padx=20,pady=5 ,bg=bbgcolor, fg = bfgcolor ,borderwidth=0)
        Visina_label.place(x=30, y=90)

        Visina_entry = Entry(root, textvariable=Visina_text, font=fstyleentry,width=7, bg=bgcolorentrfield, fg = bgcolorletter,borderwidth=0)
        Visina_entry.place(x=205, y=90)

        ####################################
        #           Kolicina
        ####################################
        Kolicina_text = StringVar()

        Kolicina_label = Label(root, text=lista[12], font=fstylelabel, width=7,padx=20,pady=5 ,bg=bbgcolor, fg = bfgcolor ,borderwidth=0)
        Kolicina_label.place(x=30, y=150)

        Kolicina_entry = Entry(root, textvariable=Kolicina_text, font=fstyleentry,width=7, bg=bgcolorentrfield, fg = bgcolorletter,borderwidth=0)
        Kolicina_entry.place(x=205, y=150)

        ####################################
        #           Tabela
        ####################################
        Tabela_text = StringVar()

        Tabela_label = Label(root, text=lista[13], font=fstylelabel, width=7,padx=20,pady=5 ,bg=bbgcolor, fg = bfgcolor ,borderwidth=0)
        Tabela_label.place(x=500, y=30)

        Tabela_entry = Entry(root, textvariable=Tabela_text, font=fstyleentry,width=7, bg=bgcolorentrfield, fg = bgcolorletter,borderwidth=0)
        Tabela_entry.place(x=675, y=30)

        dim_list = Listbox(root, height=8, font=('bold', 15), width=18, border=0, bg = "#D6F8FE", justify= CENTER) # border=0, bg = 'white' 
        dim_list.place(x=99, y=350)
        # Scrollbar object
        scrollbar = Scrollbar(root, bg = 'black')
        scrollbar.place(x=335, y=350)
        # Set scroll to listbox
        dim_list.bind('<<ListboxSelect>>')
        ###############################################
        #           Right
        ####################################
        table_list = Listbox(root,height=8,font=('bold', 15), width=18, border=0,bg = "#D6F8FE", fg = bgcolorletter) # border=0, bg = 'white'
        table_list.place(x=545, y=175)
        # Scrollbar object
        scrollbar = Scrollbar(root,bg = 'black')
        scrollbar.place(x=770, y=175)
        # Set scroll to listbox
        table_list.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=table_list.yview)
        # Bind select 
        table_list.bind('<<ListboxSelect>>')
        ################################################
        # # # # # # Dugmici za roletnu # # # # # # # # #
        ################################################
        #           Left
        ####################################
        # dodaj
        add_btn_l = Button(root, text=lista[14], font=('bold', 10),width=6, height=2,padx=4,pady=5, bg = "#98EF5E",borderwidth=0)
        add_btn_l.place(x=30, y=220)
        # obrisi
        remove_btn_l = Button(root, text=lista[15], font=('bold', 10),width=6, height=2,padx=4,pady=5, bg = "#CD6155",borderwidth=0)
        remove_btn_l.place(x=165, y=220)
        # izmeni
        update_btn_l = Button(root,text=lista[16], font=('bold', 10),width=6, height=2,padx=4,pady=5, bg = "#5DADE2",borderwidth=0)
        update_btn_l.place(x=295, y=220)
        ####################################
        #           CLear
        ####################################

        clear_btn = Button(root,text=lista[17], font=('bold', 10),width=6, height=2,padx=4,pady=5, bg = "yellow",borderwidth=0)
        clear_btn.place(x=400, y=150)

        ####################################
        #           Right
        ####################################
        # dodaj
        add_btn_r = Button(root, text=lista[14], font=('bold', 10),width=6, height=2,padx=4,pady=5, bg = "#98EF5E",borderwidth=0)
        add_btn_r.place(x=545, y=100)
        # obrisi
        remove_btn_r = Button(root, text=lista[15], font=('bold', 10),width=6, height=2,padx=4,pady=5, bg = "#CD6155",borderwidth=0)
        remove_btn_r.place(x=637, y=100)
        # izmeni
        update_btn_r = Button(root,text=lista[16], font=('bold', 10),width=6, height=2,padx=4,pady=5, bg = "#5DADE2",borderwidth=0)
        update_btn_r.place(x=727, y=100)

    def head_bar():
        global menubar
        menubar=Menu(root)
        root.config(menu=menubar)
        filemenu=Menu(menubar,tearoff=0)
        filemenu.add_command(label=lista[0],command=front_end.window_1) 
        filemenu.add_command(label=lista[1]) #,command=t2

        filemenu.add_separator()
        filemenu.add_command(label=lista[2], command=root.quit)
        menubar.add_cascade(label=lista[3], menu=filemenu)

        helpmenu=Menu(menubar,tearoff=0)
        helpmenu.add_command(label=lista[4])
        helpmenu.add_command(label=lista[5],command=front_end.info)
        menubar.add_cascade(label=lista[6],menu=helpmenu)

        languagemenu=Menu(menubar,tearoff=0)
        # languagemenu.add_command(label=lista[31], command=lambda: language_pack.to_eng("parameter")
        languagemenu.add_command(label=lista[31], command=lambda: front_end.lanu_edit("English"))
        languagemenu.add_command(label=lista[32], command=lambda: front_end.lanu_edit("Serbian"))
        menubar.add_cascade(label=lista[30],menu=languagemenu)
    def info():
        result = messagebox.showinfo(
        title="My program",
        message=lista[50]+"\n",
        detail=lista[51]+"\n\n"+lista[52]+"\n\n"+lista[53]+"\n\n"+lista[54]+" Nenad Mirković"
        )

    def lanu_edit(jazik):
        language_pack.replace_lang(jazik)
        menubar.destroy()
        language_pack.get_language()
        language_pack.check_language(language)
        # time.sleep(5)
        front_end.head_bar()

if __name__ == "__main__":
    language_pack.get_language()
    language_pack.check_language(language)
    front_end.main_window()