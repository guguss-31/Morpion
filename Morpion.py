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
            
    if 1 not in grille and 2 not in grille and 3 not in grille and 4 not in grille and 5 not in grille and 6 not in grille and 7 not in grille and 8 not in grille and 9 not in grille and "X" in grille and "O" in grille :
        CTkMessagebox(title="Winer !",message="Pas de gagnant-e , match nul !",icon="check", option_1="OK")
        reinitialiser()

def c9(bouton,tableau,chiffre):
    global X_ou_O
    if grille[tableau]==chiffre:
        bouton.configure(text=X_ou_O,fg_color="#000000",hover_color="#000000")
        grille[tableau]=X_ou_O
        if X_ou_O=="X":
            X_ou_O="O"
        else:
            X_ou_O="X"
    verifier()

frame1=ct.CTkFrame(morpion,fg_color="transparent")
frame1.grid(pady=10,padx=10,column=0,row=1)

frame2=ct.CTkFrame(morpion,fg_color="transparent")
frame2.grid(pady=10,padx=10,column=0,row=0)

b1=ct.CTkButton(frame1,text=grille[0],width=100,height=100,fg_color="white",hover_color="white",border_color="#000000",border_width=2,corner_radius=21)
b1.grid(row=0,column=0)
b1.bind("<Button-1>",lambda event:c9(b1,0,1))

b2=ct.CTkButton(frame1,text=grille[1],width=100,height=100,fg_color="white",hover_color="white",border_color="#000000",border_width=2,corner_radius=21)
b2.grid(row=0,column=1)
b2.bind("<Button-1>",lambda event:c9(b2,1,2))

b3=ct.CTkButton(frame1,text=grille[2],width=100,height=100,fg_color="white",hover_color="white",border_color="#000000",border_width=2,corner_radius=21)
b3.grid(row=0,column=2)
b3.bind("<Button-1>",lambda event:c9(b3,2,3))

b4=ct.CTkButton(frame1,text=grille[3],width=100,height=100,fg_color="white",hover_color="white",border_color="#000000",border_width=2,corner_radius=21)
b4.grid(row=1,column=0)
b4.bind("<Button-1>",lambda event:c9(b4,3,4))

b5=ct.CTkButton(frame1,text=grille[4],width=100,height=100,fg_color="white",hover_color="white",border_color="#000000",border_width=2,corner_radius=21)
b5.grid(row=1,column=1)
b5.bind("<Button-1>",lambda event:c9(b5,4,5))

b6=ct.CTkButton(frame1,text=grille[5],width=100,height=100,fg_color="white",hover_color="white",border_color="#000000",border_width=2,corner_radius=21)
b6.grid(row=1,column=2)
b6.bind("<Button-1>",lambda event:c9(b6,5,6))

b7=ct.CTkButton(frame1,text=grille[6],width=100,height=100,fg_color="white",hover_color="white",border_color="#000000",border_width=2,corner_radius=21)
b7.grid(row=2,column=0)
b7.bind("<Button-1>",lambda event:c9(b7,6,7))

b8=ct.CTkButton(frame1,text=grille[7],width=100,height=100,fg_color="white",hover_color="white",border_color="#000000",border_width=2,corner_radius=21)
b8.grid(row=2,column=1)
b8.bind("<Button-1>",lambda event:c9(b8,7,8))

b9=ct.CTkButton(frame1,text=grille[8],width=100,height=100,fg_color="white",hover_color="white",border_color="#000000",border_width=2,corner_radius=21)
b9.grid(row=2,column=2)
b9.bind("<Button-1>",lambda event:c9(b9,8,9))

tour=ct.CTkLabel(frame2,text=X_ou_O+"\n"+"C'est à "+X_ou_O+" de jouer !",fg_color="red",width=300,height=100,corner_radius=21)
tour.grid(row=0,column=0)

morpion.mainloop()

