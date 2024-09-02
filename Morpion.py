import customtkinter as ct
from CTkMessagebox import CTkMessagebox
from hPyT import *
import time
from PIL import Image
possible=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
ggrid=[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]
Bouton = []

fichier=open("datas/Var.txt","r")

contenu=fichier.read()
exec(contenu)
fichier.close()

morpion=ct.CTk()
morpion.title("MMorpion (Tic-Tac-Toe)")

ct.set_appearance_mode("dark")
ct.set_default_color_theme("green")

morpion.resizable(False, False)
maximize_minimize_button.hide(morpion)

def no_history():
    frame4.grid_forget()
    frame1.grid(pady=10,padx=10,row=2)
    frame2.grid(pady=10,padx=10,row=1)
    history=ct.CTkImage(light_image=Image.open("datas/history.png"),dark_image=Image.open("datas/history.png"),size=(21,21))
    hhistorique.configure(image=history,command=historyy)

def fenetre(i):
    bhouton=[]
    morpion_history=ct.CTk()

    frame1=ct.CTkFrame(morpion_history,fg_color="transparent")
    frame1.grid(pady=10,padx=10,row=0)

    for b in range(9):
        bouton="b",b+1
        bouton=ct.CTkButton(frame1,text=b+1,width=100,height=100,fg_color="white", hover_color="white",border_color="#000000",border_width=2,corner_radius=21,
                            command= lambda b=b:c9(Bouton[b],b,b+1))
        bouton.grid(row=ggrid[b][0],column=ggrid[b][1])
        bhouton.append(bouton)

    def color_buttons(i, c):
        if c < len(numero[i-1]):
            bhouton[numero[i-1][c]].configure(fg_color="black", hover_color="black",text=grille[i-1][numero[i-1][c]])
            bhouton[numero[i-1][c]].after(1000, lambda: color_buttons(i, c+1))
        else:
            for g in range(len(numero[i-1])):
                if couleur[i-1][numero[i-1][g]]=="green":
                    bhouton[numero[i-1][g]].configure(fg_color=couleur[i-1][numero[i-1][g]],hover_color=couleur[i-1][numero[i-1][g]])

    color_buttons(i, 0)

    morpion_history.mainloop()

def trashh():
    global grille, cancel, couleur, numero, X_ou_O
    grille = [[1,2,3,4,5,6,7,8,9]]
    cancel = []
    couleur = [['white', 'white', 'white', 'white', 'white', 'white', 'white', 'white', 'white']]
    numero = [[]]
    X_ou_O = "X"

def historyy():
    time.sleep(0.5)
    trash=ct.CTkImage(light_image=Image.open("datas/trash.png"),dark_image=Image.open("datas/trash.png"),size=(21,21))
    ttrash=ct.CTkButton(frame3,text="",fg_color="green",image=trash,width=21,command=trashh)
    ttrash.grid(row=1,column=0,columnspan=2)
    history=ct.CTkImage(light_image=Image.open("datas/x.png"),dark_image=Image.open("datas/x.png"),size=(21,21))
    hhistorique.configure(image=history,command=no_history)
    frame1.grid_forget()
    frame2.grid_forget()
    frame4.grid(pady=10,padx=10,row=1)
    WinerX=ct.CTkImage(light_image=Image.open("datas/WinerX.png"),dark_image=Image.open("datas/WinerX.png"),size=(280,28))
    WinerO=ct.CTkImage(light_image=Image.open("datas/WinerO.png"),dark_image=Image.open("datas/WinerO.png"),size=(280,28))
    NoWiner=ct.CTkImage(light_image=Image.open("datas/NoWiner.png"),dark_image=Image.open("datas/NoWiner.png"),size=(280,28))
    for i in range(len(grille)-1):
        x=i+2
        if grille[i][-1]=="X":
            (i)=ct.CTkButton(frame4,text="",image=WinerX,width=280,command=lambda i=i: fenetre(i+1))
        elif grille[i][-1]=="O":
            (i)=ct.CTkButton(frame4,text="",image=WinerO,width=280,command=lambda i=i: fenetre(i+1))
        elif grille[i][-1]=="?":
            (i)=ct.CTkButton(frame4,text="",image=NoWiner,width=280,command=lambda i=i: fenetre(i+1))
        (i).grid(ipady=0,ipadx=0,column=1,row=(x))
        (i)=ct.CTkLabel(frame4,text=x-1,width=30)
        (i).grid(column=0,row=(x))

def ccouleur():
    for i in range(9):
        Bouton[i].configure(fg_color=couleur[-1][i],hover_color=couleur[-1][i])
    time.sleep(0.5)

def undoo():
    global cancel
    global ccancel
    print(cancel)
    print(grille)
    if 0 in cancel or 1 in cancel or 2 in cancel or 3 in cancel or 4 in cancel or 5 in cancel or 6 in cancel or 7 in cancel or 8 in cancel:
        ccancel=cancel[-1]+1
        grille[-1][cancel[-1]]=ccancel
        couleur[-1][cancel[-1]]="white"
        cancel.pop(-1)
        print(cancel)
        print(grille)
        ccouleur()

def reinitialiser(winer):
    if winer=="X" or winer=="O":
        CTkMessagebox(title="Winer !",message="Le/la Joueur/joueuse "+winer+" à gagné !",icon="check", option_1="OK")
    else:
        CTkMessagebox(title="Winer !",message="Pas de gagnant-e , match nul !",icon="check", option_1="OK")
    time.sleep(1)
    global grille
    grille[-1].append(winer)
    grille.append([1,2,3,4,5,6,7,8,9])
    numero.append([])
    couleur.append(["white","white","white","white","white","white","white","white","white",])
    for i in range(9):
        Bouton[i].configure(text=grille[-1][i],fg_color=couleur[-1][i],hover_color=couleur[-1][i])

def verifier():
    tour.configure(text=X_ou_O+"\n"+"C'est à "+X_ou_O+" de jouer !")

    for i in range(8):
        if grille[-1][possible[i][0]]=="X" and grille[-1][possible[i][1]]=="X" and grille[-1][possible[i][2]]=="X":
            couleur[-1][possible[i][0]]="green"
            Bouton[possible[i][0]].configure(fenetre,fg_color=couleur[-1][possible[i][0]],hover_color=couleur[-1][possible[i][0]])
            couleur[-1][possible[i][1]]="green"
            Bouton[possible[i][1]].configure(fenetre,fg_color=couleur[-1][possible[i][1]],hover_color=couleur[-1][possible[i][1]])
            couleur[-1][possible[i][2]]="green"
            Bouton[possible[i][2]].configure(fenetre,fg_color=couleur[-1][possible[i][2]],hover_color=couleur[-1][possible[i][2]])
            reinitialiser("X")
    for i in range(8):
        if grille[-1][possible[i][0]]=="O" and grille[-1][possible[i][1]]=="O" and grille[-1][possible[i][2]]=="O":
            couleur[-1][possible[i][0]]="green"
            Bouton[possible[i][0]].configure(fenetre,fg_color=couleur[-1][possible[i][0]],hover_color=couleur[-1][possible[i][0]])
            couleur[-1][possible[i][1]]="green"
            Bouton[possible[i][1]].configure(fenetre,fg_color=couleur[-1][possible[i][1]],hover_color=couleur[-1][possible[i][1]])
            couleur[-1][possible[i][2]]="green"
            Bouton[possible[i][2]].configure(fenetre,fg_color=couleur[-1][possible[i][2]],hover_color=couleur[-1][possible[i][2]])
            reinitialiser("O")

    if 1 not in grille[-1] and 2 not in grille[-1] and 3 not in grille[-1] and 4 not in grille[-1] and 5 not in grille[-1] and 6 not in grille[-1] and 7 not in grille[-1] and 8 not in grille[-1] and 9 not in grille[-1] and "X" in grille[-1] and "O" in grille[-1] :
        reinitialiser("?")

def c9(bouton,tableau,chiffre):
    global X_ou_O
    global cancel
    global couleur
    global numero
    if grille[-1][tableau]==chiffre:
        couleur[-1][tableau]="black"
        bouton.configure(text=X_ou_O,fg_color=couleur[-1][tableau],hover_color=couleur[-1][tableau])
        if len(numero)!=0:
            numero[-1].append(tableau)
        grille[-1][tableau]=X_ou_O
        cancel.append(tableau)
        if X_ou_O=="X":
            X_ou_O="O"
        else:
            X_ou_O="X"
    verifier()

frame1=ct.CTkFrame(morpion,fg_color="transparent")
frame1.grid(pady=10,padx=10,row=2)

frame2=ct.CTkFrame(morpion,fg_color="transparent")
frame2.grid(pady=10,padx=10,row=1)

frame3=ct.CTkFrame(morpion,fg_color="transparent")
frame3.grid(pady=10,padx=10,row=0)

frame4=ct.CTkFrame(morpion,fg_color="transparent")

undo=ct.CTkImage(light_image=Image.open("datas/undo.png"),dark_image=Image.open("datas/undo.png"),size=(21,21))

uundo=ct.CTkButton(frame3,text="",fg_color="green",image=undo,command=undoo,width=21)
uundo.grid(column=0,row=0)

history=ct.CTkImage(light_image=Image.open("datas/history.png"),dark_image=Image.open("datas/history.png"),size=(21,21))

hhistorique=ct.CTkButton(frame3,text="",fg_color="green",image=history,width=21,height=21,command=historyy)
hhistorique.grid(column=1,row=0)

for b in range(9):
    bouton="b",b+1
    bouton=ct.CTkButton(frame1,text=grille[-1][b],width=100,height=100,fg_color=couleur[-1][b],hover_color=couleur[-1][b],border_color="#000000",border_width=2,corner_radius=21,
                        command= lambda b=b:c9(Bouton[b],b,b+1))
    bouton.grid(row=ggrid[b][0],column=ggrid[b][1])
    Bouton.append(bouton)

tour=ct.CTkLabel(frame2,text=X_ou_O+"\n"+"C'est à "+X_ou_O+" de jouer !",fg_color="red",width=300,height=100,corner_radius=21)
tour.grid(row=0,column=0)

def on_closing():
    print("La fenêtre a été fermée")
    with open("datas/Var.txt", "w") as fichier:
        fichier.write("grille = "+str(grille)+"\n")
        fichier.write("cancel = " + str(cancel) + "\n")
        fichier.write("couleur = " + str(couleur) + "\n")
        fichier.write("numero = " + str(numero) + "\n")
        fichier.write("X_ou_O = " + '"' + str(X_ou_O) + '"')
        fichier.close()
    morpion.destroy()

morpion.protocol("WM_DELETE_WINDOW", on_closing)

morpion.mainloop()

