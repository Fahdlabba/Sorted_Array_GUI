from tkinter import *
from pytube import YouTube

def Downloader():
    try:
        url =YouTube(str(link.get()))
        video = url.streams.first()
        video.download()
        Label(window, text = 'DOWNLOADED', font = 'arial 15').place(x= 0 , y = 200)
    except:
        Label(window, text='Url Not Found', font='arial 15',bg="white").place(x=145, y=215)


helper="Copy ur video link and paste it bellow and then \n click Telecharger "
window=Tk();
window.geometry('450x400')
window.resizable(width=False,height=False)
window.config(bg="#cc1701")

#Title
title=Label(window,text="Youtube Video ",font=("Times New Roman",30),fg="Black",bg='#cc1701')
title.place(x=100,y=30)
#help
help=Label(window,text=helper,font=("Times New Roamn",15),bg="#cc1701")
help.place(x=5,y=150)
#entry:input
link=Entry(window,font=("arial",12))
link.place(x=25,y=250,width=400,height=30)
#btn
btn1=Button(window,text="Telecharger ",font=("Bahnschrift Light Condensed",18),command=Downloader)
btn1.place(x=50,y=320,width=150,height=35)
btn2=Button(window,text="Annuler",font=("Bahnschrift Light Condensed",18),command=window.destroy)
btn2.place(x=250,y=320,width=150,height=35)





mainloop()