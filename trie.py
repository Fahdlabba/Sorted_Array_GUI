from tkinter import *

def trie():
    text=str(array.get())
    list1 = []
    list1[:0] = text
    try:
        for i in range(len(list1)):
            for j in range(i+1):
                if int(list1[i])< int(list1[j]):
                    aux=list1[i]
                    list1[i]=list1[j]
                    list1[j]=aux
        result.delete(0, END)
        result.insert(0, list1)
    except:
        array.insert(0,"Error")
        result.insert(0,'Error')

window=Tk();
window.geometry('450x350')
window.resizable(width=False,height=False)
window.config(bg="#5F38D8")

#Title
title=Label(window,text="Trier un Tableau ",font=("Times New Roman",30),fg="#B8C816",bg='#5F38D8')
title.place(x=110,y=30)
#entry:input
mess=Label(window,text="List :",font=("Times New Roman",20),fg="#B8C816",bg='#5F38D8')
mess.place(x=4,y=120)
array=Entry(window,font=("arial",12),bg="#8F969D")
array.place(x=100,y=120,width=320,height=30)
#---------
mess2=Label(window,text="Result:",font=("Times New Roman",20),fg="#B8C816",bg='#5F38D8')
mess2.place(x=5,y=200)
result=Entry(window,font=("arial",12),bg="#8F969D")
result.place(x=100,y=200,width=320,height=30)
#btn
btn1=Button(window,text="Trier",font=("Bahnschrift Light Condensed",18),bg="#787D82",command=trie)
btn1.place(x=120,y=280,width=120,height=35)
btn2=Button(window,text="Annuler",font=("Bahnschrift Light Condensed",18),bg="#787D82",command=window.destroy)
btn2.place(x=270,y=280,width=120,height=35)




mainloop()