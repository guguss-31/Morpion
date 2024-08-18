import customtkinter as ct
from CTkMessagebox import CTkMessagebox
from hPyT import *
import time

grille=[1,2,3,4,5,6,7,8,9]

X_ou_O="X"

morpion=ct.CTk()

morpion.resizable(False, False)

maximize_button.disable(morpion)
minimize_button.disable(morpion)


def reinitialiser():
    time.sleep(1)
    global grille
    grille=[1,2,3,4,5,6,7,8,9]
    b1.configure(text=grille[0],fg_color="white",hover_color="white")
    b2.configure(text=grille[1],fg_color="white",hover_color="white")
    b3.configure(text=grille[2],fg_color="white",hover_color="white")
    b4.configure(text=grille[3],fg_color="white",hover_color="white")
    b5.configure(text=grille[4],fg_color="white",hover_color="white")
    b6.configure(text=grille[5],fg_color="white",hover_color="white")
    b7.configure(text=grille[6],fg_color="white",hover_color="white")
    b8.configure(text=grille[7],fg_color="white",hover_color="white")
    b9.configure(text=grille[8],fg_color="white",hover_color="white")

def verifier():
    tour.configure(text=X_ou_O+"\n"+"C'est à "+X_ou_O+" de jouer !")
    if 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9 in grille:
        if grille[0]=="X" and grille[1]=="X" and grille[2]=="X" : 
            b1.configure(fg_color="green",hover_color="green")
            b2.configure(fg_color="green",hover_color="green")
            b3.configure(fg_color="green",hover_color="green")
            CTkMessagebox(title="Winer !",message="Le/la Joueur/joueuse X à gagné !",icon="check", option_1="OK")
            reinitialiser()
        elif grille[0]=="O" and grille[1]=="O" and grille[2]=="O" : 
                b1.configure(fg_color="green",hover_color="green")
                b2.configure(fg_color="green",hover_color="green")
                b3.configure(fg_color="green",hover_color="green")
                CTkMessagebox(title="Winer !",message="Le/la Joueur/joueuse O à gagné !",icon="check", option_1="OK")
                reinitialiser()
        if grille[3] == "X" and grille[4] == "X" and grille[5] == "X" : 
                b4.configure(fg_color="green",hover_color="green")
                b5.configure(fg_color="green",hover_color="green")
                b6.configure(fg_color="green",hover_color="green")
                CTkMessagebox(title="Winer !",message="Le/la Joueur/joueuse X à gagné !",icon="check", option_1="OK")
                reinitialiser()
        elif grille[3] == "O" and grille[4] == "O" and grille[5] == "O" : 
                b4.configure(fg_color="green",hover_color="green")
                b5.configure(fg_color="green",hover_color="green")
                b6.configure(fg_color="green",hover_color="green")
                CTkMessagebox(title="Winer !",message="Le/la Joueur/joueuse O à gagné !",icon="check", option_1="OK")
                reinitialiser()
        
        if grille[6] == "X" and grille[7] == "X" and grille[8] == "X" : 
            b7.configure(fg_color="green",hover_color="green")
            b8.configure(fg_color="green",hover_color="green")
            b9.configure(fg_color="green",hover_color="green")
            CTkMessagebox(title="Winer !",message="Le/la Joueur/joueuse X à gagné !",icon="check", option_1="OK")
            reinitialiser()
        elif grille[6] == "O" and grille[7] == "O" and grille[8] == "O" : 
                b7.configure(fg_color="green",hover_color="green")
                b8.configure(fg_color="green",hover_color="green")
                b9.configure(fg_color="green",hover_color="green")
                CTkMessagebox(title="Winer !",message="Le/la Joueur/joueuse O à gagné !",icon="check", option_1="OK")
                reinitialiser()
        
        if grille[0] == "X" and grille[3] == "X" and grille[6] == "X" : 
            b1.configure(fg_color="green",hover_color="green")
            b4.configure(fg_color="green",hover_color="green")
            b7.configure(fg_color="green",hover_color="green")
            CTkMessagebox(title="Winer !",message="Le/la Joueur/joueuse X à gagné !",icon="check", option_1="OK")
            reinitialiser()
            
        elif grille[0] == "O" and grille[3] == "O" and grille[6] == "O" : 
                b1.configure(fg_color="green",hover_color="green")
                b4.configure(fg_color="green",hover_color="green")
                b7.configure(fg_color="green",hover_color="green")
                CTkMessagebox(title="Winer !",message="Le/la Joueur/joueuse O à gagné !",icon="check", option_1="OK")
                reinitialiser()
                
        if grille[1] == "X" and grille[4] == "X" and grille[7] == "X" : 
            b2.configure(fg_color="green",hover_color="green")
            b5.configure(fg_color="green",hover_color="green")
            b8.configure(fg_color="green",hover_color="green")
            CTkMessagebox(title="Winer !",message="Le/la Joueur/joueuse X à gagné !",icon="check", option_1="OK")
            reinitialiser()
            
        elif grille[1] == "O" and grille[4] == "O" and grille[7] == "O" : 
                b2.configure(fg_color="green",hover_color="green")
                b5.configure(fg_color="green",hover_color="green")
                b8.configure(fg_color="green",hover_color="green")
                CTkMessagebox(title="Winer !",message="Le/la Joueur/joueuse O à gagné !",icon="check", option_1="OK")
                reinitialiser()
                
        if grille[2] == "X" and grille[5] == "X" and grille[8] == "X" : 
            b3.configure(fg_color="green",hover_color="green")
            b6.configure(fg_color="green",hover_color="green")
            b9.configure(fg_color="green",hover_color="green")
            CTkMessagebox(title="Winer !",message="Le/la Joueur/joueuse X à gagné !",icon="check", option_1="OK")
            reinitialiser()
            
        elif grille[2] == "O" and grille[5] == "O" and grille[8] == "O" : 
                b3.configure(fg_color="green",hover_color="green")
                b6.configure(fg_color="green",hover_color="green")
                b9.configure(fg_color="green",hover_color="green")
                CTkMessagebox(title="Winer !",message="Le/la Joueur/joueuse O à gagné !",icon="check", option_1="OK")
                reinitialiser()
                
        if grille[0] == "X" and grille[4] == "X" and grille[8] == "X" : 
            b1.configure(fg_color="green",hover_color="green")
            b5.configure(fg_color="green",hover_color="green")
            b9.configure(fg_color="green",hover_color="green")
            CTkMessagebox(title="Winer !",message="Le/la Joueur/joueuse X à gagné !",icon="check", option_1="OK")
            reinitialiser()
            
        elif grille[0] == "O" and grille[4] == "O" and grille[8] == "O" : 
                b1.configure(fg_color="green",hover_color="green")
                b5.configure(fg_color="green",hover_color="green")
                b9.configure(fg_color="green",hover_color="green")
                CTkMessagebox(title="Winer !",message="Le/la Joueur/joueuse O à gagné !",icon="check", option_1="OK")
                reinitialiser()
                
        if grille[2] == "X" and grille[4] == "X" and grille[6] == "X" : 
            b3.configure(fg_color="green",hover_color="green")
            b5.configure(fg_color="green",hover_color="green")
            b7.configure(fg_color="green",hover_color="green")
            CTkMessagebox(title="Winer !",message="Le/la Joueur/joueuse X à gagné !",icon="check", option_1="OK")
            reinitialiser()
            
        elif grille[2] == "O" and grille[4] == "O" and grille[6] == "O" : 
                b3.configure(fg_color="green",hover_color="green")
                b5.configure(fg_color="green",hover_color="green")
                b7.configure(fg_color="green",hover_color="green")
                CTkMessagebox(title="Winer !",message="Le/la Joueur/joueuse O à gagné !",icon="check", option_1="OK")
                reinitialiser()
    else:
        if grille[0]=="X" and grille[1]=="X" and grille[2]=="X" : 
            b1.configure(fg_color="green",hover_color="green")
            b2.configure(fg_color="green",hover_color="green")
            b3.configure(fg_color="green",hover_color="green")
            CTkMessagebox(title="Winer !",message="Le/la Joueur/joueuse X à gagné !",icon="check", option_1="OK")
            reinitialiser()
        elif grille[0]=="O" and grille[1]=="O" and grille[2]=="O" : 
                b1.configure(fg_color="green",hover_color="green")
                b2.configure(fg_color="green",hover_color="green")
                b3.configure(fg_color="green",hover_color="green")
                CTkMessagebox(title="Winer !",message="Le/la Joueur/joueuse O à gagné !",icon="check", option_1="OK")
                reinitialiser()
        if grille[3] == "X" and grille[4] == "X" and grille[5] == "X" : 
                b4.configure(fg_color="green",hover_color="green")
                b5.configure(fg_color="green",hover_color="green")
                b6.configure(fg_color="green",hover_color="green")
                CTkMessagebox(title="Winer !",message="Le/la Joueur/joueuse X à gagné !",icon="check", option_1="OK")
                reinitialiser()
        elif grille[3] == "O" and grille[4] == "O" and grille[5] == "O" : 
                b4.configure(fg_color="green",hover_color="green")
                b5.configure(fg_color="green",hover_color="green")
                b6.configure(fg_color="green",hover_color="green")
                CTkMessagebox(title="Winer !",message="Le/la Joueur/joueuse O à gagné !",icon="check", option_1="OK")
                reinitialiser()
        
        if grille[6] == "X" and grille[7] == "X" and grille[8] == "X" : 
            b7.configure(fg_color="green",hover_color="green")
            b8.configure(fg_color="green",hover_color="green")
            b9.configure(fg_color="green",hover_color="green")
            CTkMessagebox(title="Winer !",message="Le/la Joueur/joueuse X à gagné !",icon="check", option_1="OK")
            reinitialiser()
        elif grille[6] == "O" and grille[7] == "O" and grille[8] == "O" : 
                b7.configure(fg_color="green",hover_color="green")
                b8.configure(fg_color="green",hover_color="green")
                b9.configure(fg_color="green",hover_color="green")
                CTkMessagebox(title="Winer !",message="Le/la Joueur/joueuse O à gagné !",icon="check", option_1="OK")
                reinitialiser()
        
        if grille[0] == "X" and grille[3] == "X" and grille[6] == "X" : 
            b1.configure(fg_color="green",hover_color="green")
            b4.configure(fg_color="green",hover_color="green")
            b7.configure(fg_color="green",hover_color="green")
            CTkMessagebox(title="Winer !",message="Le/la Joueur/joueuse X à gagné !",icon="check", option_1="OK")
            reinitialiser()
            
        elif grille[0] == "O" and grille[3] == "O" and grille[6] == "O" : 
                b1.configure(fg_color="green",hover_color="green")
                b4.configure(fg_color="green",hover_color="green")
                b7.configure(fg_color="green",hover_color="green")
                CTkMessagebox(title="Winer !",message="Le/la Joueur/joueuse O à gagné !",icon="check", option_1="OK")
                reinitialiser()
                
        if grille[1] == "X" and grille[4] == "X" and grille[7] == "X" : 
            b2.configure(fg_color="green",hover_color="green")
            b5.configure(fg_color="green",hover_color="green")
            b8.configure(fg_color="green",hover_color="green")
            CTkMessagebox(title="Winer !",message="Le/la Joueur/joueuse X à gagné !",icon="check", option_1="OK")
            reinitialiser()
            
        elif grille[1] == "O" and grille[4] == "O" and grille[7] == "O" : 
                b2.configure(fg_color="green",hover_color="green")
                b5.configure(fg_color="green",hover_color="green")
                b8.configure(fg_color="green",hover_color="green")
                CTkMessagebox(title="Winer !",message="Le/la Joueur/joueuse O à gagné !",icon="check", option_1="OK")
                reinitialiser()
                
        if grille[2] == "X" and grille[5] == "X" and grille[8] == "X" : 
            b3.configure(fg_color="green",hover_color="green")
            b6.configure(fg_color="green",hover_color="green")
            b9.configure(fg_color="green",hover_color="green")
            CTkMessagebox(title="Winer !",message="Le/la Joueur/joueuse X à gagné !",icon="check", option_1="OK")
            reinitialiser()
            
        elif grille[2] == "O" and grille[5] == "O" and grille[8] == "O" : 
                b3.configure(fg_color="green",hover_color="green")
                b6.configure(fg_color="green",hover_color="green")
                b9.configure(fg_color="green",hover_color="green")
                CTkMessagebox(title="Winer !",message="Le/la Joueur/joueuse O à gagné !",icon="check", option_1="OK")
                reinitialiser()
                
        if grille[0] == "X" and grille[4] == "X" and grille[8] == "X" : 
            b1.configure(fg_color="green",hover_color="green")
            b5.configure(fg_color="green",hover_color="green")
            b9.configure(fg_color="green",hover_color="green")
            CTkMessagebox(title="Winer !",message="Le/la Joueur/joueuse X à gagné !",icon="check", option_1="OK")
            reinitialiser()
            
        elif grille[0] == "O" and grille[4] == "O" and grille[8] == "O" : 
                b1.configure(fg_color="green",hover_color="green")
                b5.configure(fg_color="green",hover_color="green")
                b9.configure(fg_color="green",hover_color="green")
                CTkMessagebox(title="Winer !",message="Le/la Joueur/joueuse O à gagné !",icon="check", option_1="OK")
                reinitialiser()
                
        if grille[2] == "X" and grille[4] == "X" and grille[6] == "X" : 
            b3.configure(fg_color="green",hover_color="green")
            b5.configure(fg_color="green",hover_color="green")
            b7.configure(fg_color="green",hover_color="green")
            CTkMessagebox(title="Winer !",message="Le/la Joueur/joueuse X à gagné !",icon="check", option_1="OK")
            reinitialiser()
            
        elif grille[2] == "O" and grille[4] == "O" and grille[6] == "O" : 
                b3.configure(fg_color="green",hover_color="green")
                b5.configure(fg_color="green",hover_color="green")
                b7.configure(fg_color="green",hover_color="green")
                CTkMessagebox(title="Winer !",message="Le/la Joueur/joueuse O à gagné !",icon="check", option_1="OK")
                reinitialiser()
        CTkMessagebox(title="Winer !",message="Pas de gagnant-e , match nul !",icon="check", option_1="OK")
        reinitialiser()

def c1():
    global X_ou_O
    if grille[0]==1:
        b1.configure(text=X_ou_O,fg_color="#000000",hover_color="#000000")
        grille[0]=X_ou_O
        if X_ou_O=="X":
            X_ou_O="O"
        else:
            X_ou_O="X"
    verifier()

def c2():
    global X_ou_O
    if grille[1]==2:
        b2.configure(text=X_ou_O,fg_color="#000000",hover_color="#000000")
        grille[1]=X_ou_O
        if X_ou_O=="X":
            X_ou_O="O"
        else:
            X_ou_O="X"
    verifier()

def c3():
    global X_ou_O
    if grille[2]==3:
        b3.configure(text=X_ou_O,fg_color="#000000",hover_color="#000000")
        grille[2]=X_ou_O
        if X_ou_O=="X":
            X_ou_O="O"
        else:
            X_ou_O="X"
    verifier()

def c4():
    global X_ou_O
    if grille[3]==4:
        b4.configure(text=X_ou_O,fg_color="#000000",hover_color="#000000")
        grille[3]=X_ou_O
        if X_ou_O=="X":
            X_ou_O="O"
        else:
            X_ou_O="X"
    verifier()

def c5():
    global X_ou_O
    if grille[4]==5:
        b5.configure(text=X_ou_O,fg_color="#000000",hover_color="#000000")
        grille[4]=X_ou_O
        if X_ou_O=="X":
            X_ou_O="O"
        else:
            X_ou_O="X"
    verifier()

def c6():
    global X_ou_O
    if grille[5]==6:
        b6.configure(text=X_ou_O,fg_color="#000000",hover_color="#000000")
        grille[5]=X_ou_O
        if X_ou_O=="X":
            X_ou_O="O"
        else:
            X_ou_O="X"
    verifier()

def c7():
    global X_ou_O
    if grille[6]==7:
        b7.configure(text=X_ou_O,fg_color="#000000",hover_color="#000000")
        grille[6]=X_ou_O
        if X_ou_O=="X":
            X_ou_O="O"
        else:
            X_ou_O="X"
    verifier()

def c8():
    global X_ou_O
    if grille[7]==8:
        b8.configure(text=X_ou_O,fg_color="#000000",hover_color="#000000")
        grille[7]=X_ou_O
        if X_ou_O=="X":
            X_ou_O="O"
        else:
            X_ou_O="X"
    verifier()

def c9():
    global X_ou_O
    if grille[8]==9:
        b9.configure(text=X_ou_O,fg_color="#000000",hover_color="#000000")
        grille[8]=X_ou_O
        if X_ou_O=="X":
            X_ou_O="O"
        else:
            X_ou_O="X"
    verifier()

frame1=ct.CTkFrame(morpion)
frame1.grid(pady=10,padx=10,column=0,row=1)

frame11=ct.CTkFrame(frame1,fg_color="transparent")
frame11.grid(pady=21,padx=21,column=0,row=0)

frame2=ct.CTkFrame(morpion)
frame2.grid(pady=10,padx=10,column=0,row=0)

frame22=ct.CTkFrame(frame2,fg_color="transparent")
frame22.grid(pady=21,padx=21,column=0,row=0)

b1=ct.CTkButton(frame11,text=grille[0],width=100,height=100,fg_color="white",hover_color="white")
b1.grid(row=0,column=0)
b1.bind("<Button-1>",lambda event:c1())

b2=ct.CTkButton(frame11,text=grille[1],width=100,height=100,fg_color="white",hover_color="white")
b2.grid(row=0,column=1)
b2.bind("<Button-1>",lambda event:c2())

b3=ct.CTkButton(frame11,text=grille[2],width=100,height=100,fg_color="white",hover_color="white")
b3.grid(row=0,column=2)
b3.bind("<Button-1>",lambda event:c3())

b4=ct.CTkButton(frame11,text=grille[3],width=100,height=100,fg_color="white",hover_color="white")
b4.grid(row=1,column=0)
b4.bind("<Button-1>",lambda event:c4())

b5=ct.CTkButton(frame11,text=grille[4],width=100,height=100,fg_color="white",hover_color="white")
b5.grid(row=1,column=1)
b5.bind("<Button-1>",lambda event:c5())

b6=ct.CTkButton(frame11,text=grille[5],width=100,height=100,fg_color="white",hover_color="white")
b6.grid(row=1,column=2)
b6.bind("<Button-1>",lambda event:c6())

b7=ct.CTkButton(frame11,text=grille[6],width=100,height=100,fg_color="white",hover_color="white")
b7.grid(row=2,column=0)
b7.bind("<Button-1>",lambda event:c7())

b8=ct.CTkButton(frame11,text=grille[7],width=100,height=100,fg_color="white",hover_color="white")
b8.grid(row=2,column=1)
b8.bind("<Button-1>",lambda event:c8())

b9=ct.CTkButton(frame11,text=grille[8],width=100,height=100,fg_color="white",hover_color="white")
b9.grid(row=2,column=2)
b9.bind("<Button-1>",lambda event:c9())

tour=ct.CTkLabel(frame22,text=X_ou_O+"\n"+"C'est à "+X_ou_O+" de jouer !",fg_color="red",width=300,height=100,corner_radius=21)
tour.grid(row=0,column=0)

morpion.mainloop()

