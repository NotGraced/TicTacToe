from tkinter import*
from tkinter import messagebox#pazinojumi, ieteikumi
mansLogs=Tk()#loga objekts
mansLogs.title("TicTacToe")

SpeletajsX=True#kuram speletajam karta speley, liks krustinus
count=0#aizpildito rutin skaits

def disablebuttons():
    btn1.config(state=DISABLED)
    btn2.config(state=DISABLED)
    btn3.config(state=DISABLED)
    btn4.config(state=DISABLED)
    btn5.config(state=DISABLED)
    btn6.config(state=DISABLED)
    btn7.config(state=DISABLED)
    btn8.config(state=DISABLED)
    btn9.config(state=DISABLED)

def reset():
    btn1.config(state=NORMAL)
    btn2.config(state=NORMAL)
    btn3.config(state=NORMAL)
    btn4.config(state=NORMAL)
    btn5.config(state=NORMAL)
    btn6.config(state=NORMAL)
    btn7.config(state=NORMAL)
    btn8.config(state=NORMAL)
    btn9.config(state=NORMAL)
    btn1["text"]=""
    btn2["text"]=""
    btn3["text"]=""
    btn4["text"]=""
    btn5["text"]=""
    btn6["text"]=""
    btn7["text"]=""
    btn8["text"]=""
    btn9["text"]=""


def btnClick(button):#padod visu pogu
    global SpeletajsX,count#kadi mainigiw tiks izmantoti visa programma
    if button["text"]==""and SpeletajsX==True:#spele X peletajs
        button["text"]="X"#maina uz X
        SpeletajsX=False
        count+=1#palielina rutinu skaits
        CheckWinner()
    elif button["text"]==""and SpeletajsX==False:#mainas speletajs
        button["text"]="O"
        SpeletajsX=True
        count+=1
        CheckWinner()
    else:
        messagebox.showerror("Krustinaplitis","Seit kads jau ir piespiedis")

def CheckWinner():
    global CheckWinner
    winner=False
    if (btn1["text"]=="X" and btn2["text"]=="X" and btn3["text"]=="X" or
    btn4["text"]=="X" and btn5["text"]=="X" and btn6["text"]=="X" or
    btn7["text"]=="X" and btn8["text"]=="X" and btn9["text"]=="X" or
    btn1["text"]=="X" and btn4["text"]=="X" and btn7["text"]=="X" or
    btn2["text"]=="X" and btn5["text"]=="X" and btn8["text"]=="X" or
    btn3["text"]=="X" and btn6["text"]=="X" and btn9["text"]=="X" or
    btn1["text"]=="X" and btn5["text"]=="X" and btn9["text"]=="X" or
    btn3["text"]=="X" and btn5["text"]=="X" and btn7["text"]=="X"):
        winner=True
        disablebuttons()
        messagebox.showinfo("TicTacToe", "SpeletajsX ir uzvaretajs")
    elif (btn1["text"]=="O" and btn2["text"]=="O" and btn3["text"]=="O" or
    btn4["text"]=="O" and btn5["text"]=="O" and btn6["text"]=="O" or
    btn7["text"]=="O" and btn8["text"]=="O" and btn9["text"]=="O" or
    btn1["text"]=="O" and btn4["text"]=="O" and btn7["text"]=="O" or
    btn2["text"]=="O" and btn5["text"]=="O" and btn8["text"]=="O" or
    btn3["text"]=="O" and btn6["text"]=="O" and btn9["text"]=="O" or
    btn1["text"]=="O" and btn5["text"]=="O" and btn9["text"]=="O" or
    btn3["text"]=="O" and btn5["text"]=="O" and btn7["text"]=="O"):
        winner=True
        disablebuttons()
        messagebox.showinfo("TicTacToe", "SpeletajsO ir uzvaretajs")
    elif count==9 and winner==False:
        disablebuttons()
        messagebox.showinfo("TicTacToe", "Neizskirts")
    return

btn1=Button(mansLogs,text="",width=6,height=3,font=("Helvica',24"),command=lambda:btnClick(btn1))
btn2=Button(mansLogs,text="",width=6,height=3,font=("Helvica',24"),command=lambda:btnClick(btn2))
btn3=Button(mansLogs,text="",width=6,height=3,font=("Helvica',24"),command=lambda:btnClick(btn3))
btn4=Button(mansLogs,text="",width=6,height=3,font=("Helvica',24"),command=lambda:btnClick(btn4))
btn5=Button(mansLogs,text="",width=6,height=3,font=("Helvica',24"),command=lambda:btnClick(btn5))
btn6=Button(mansLogs,text="",width=6,height=3,font=("Helvica',24"),command=lambda:btnClick(btn6))
btn7=Button(mansLogs,text="",width=6,height=3,font=("Helvica',24"),command=lambda:btnClick(btn7))
btn8=Button(mansLogs,text="",width=6,height=3,font=("Helvica',24"),command=lambda:btnClick(btn8))
btn9=Button(mansLogs,text="",width=6,height=3,font=("Helvica',24"),command=lambda:btnClick(btn9))

btn1.grid(row=1,column=1)
btn2.grid(row=1,column=2)
btn3.grid(row=1,column=3)
btn4.grid(row=2,column=1)
btn5.grid(row=2,column=2)
btn6.grid(row=2,column=3)
btn7.grid(row=3,column=1)
btn8.grid(row=3,column=2)
btn9.grid(row=3,column=3)

galvenaizvelne=Menu(mansLogs)#izveido galveno izvelni
mansLogs.config(menu=galvenaizvelne)#pievieno galvenajam logam

opcijas=Menu(galvenaizvelne,tearoff=False)#maza izvelne
galvenaizvelne.add_cascade(label="Opcijas",menu=opcijas)#lejupkritosais saraksts           

opcijas.add_command(label="jauna spele",command=reset)
opcijas.add_command(label="Iziet",command=mansLogs.quit)











































mansLogs.mainloop()