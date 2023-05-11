# -*- coding: utf-8 -*-
"""
Created on Thu Mar 30 09:08:14 2017

@author: Radek
"""
from pylab import *
from Tkinter import *
from tkMessageBox import *


hlavni = Tk()

HorniMenu=Menu(hlavni)

def Soubor():
    soub=open("hodnoty1.txt","r")
    nazev=soub.readline()
    osax=soub.readline()
    osay=soub.readline()

    x=[]    
    y=[]
    radek=soub.readline()
    while radek!="":
        sez=radek.split(" ")
        x.append(int(sez[0]))
        y.append(int(sez[1]))
        radek=soub.readline()
    soub.close()


    title(nazev)
    xlabel(osax)
    ylabel(osay)    
    plot(x,y)
    show() #zobrazení grafu

def Vypocet():
    okno=Toplevel()
    popisek1=Label(okno,text="Zadej hodnotu m: ")
    popisek1.grid(row=0)
    vstup1=Entry(okno)
    vstup1.grid(row=0,column=1)
    popisek2=Label(okno,text="Zadej hodnotu n: ")
    popisek2.grid(row=1)
    vstup2=Entry(okno)
    vstup2.grid(row=1,column=1)
    popisek3=Label(okno,text="Zadej hodnotu x: ")
    popisek3.grid(row=2)
    vstup3=Entry(okno)
    vstup3.grid(row=2,column=1)
    popisek4=Label(okno,text="Výsledek výrazu: ")
    popisek4.grid(row=3)
    vystup=Label(okno,text="")
    vystup.grid(row=3,column=1)
    def Pocitej():
        try:
            m=int(vstup1.get())
        except:
            showerror("Chyba","Hodnota m musí být celé číslo!")
        try:
            n=int(vstup2.get())
        except:
            showerror("Chyba","Hodnota n musí být celé číslo!")   
        try:
            x=float(vstup3.get())
        except:
            showerror("Chyba","Hodnota x musí být desetinné číslo!")   
        if m<=n:
            soucet=0
            for i in range(m,n+1):            
                hodnota=(-1)**i*sin(2*x)/(1+i*i)
                soucet+=hodnota
            soucet*=3
            vystup["text"]=str(soucet)
        else:
            showerror("Chyba","Hodnota m musí být menší nebo rovna n!")   
            
        
        
    tlac1=Button(okno,text="Výpočet",command=Pocitej)
    tlac1.grid(row=4)
    tlac2=Button(okno,text="Zavři",command=okno.destroy)
    tlac2.grid(row=4,column=1)
    
    

MenuSoubor=Menu(HorniMenu,tearoff=0)
MenuSoubor.add_command(label="Graf ze souboru",command=Soubor)
MenuSoubor.add_command(label="Výpočet ze vzorce",command=Vypocet)
MenuSoubor.add_command(label="Konec",command=hlavni.destroy)

HorniMenu.add_cascade(label="Soubor", menu=MenuSoubor)

hlavni.config(menu=HorniMenu)

mainloop()
