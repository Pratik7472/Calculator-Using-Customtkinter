from customtkinter import *
#ED802E
app =CTk()
app.title("MY")
app.geometry("700×700")
app.minsize(height=280,width=245)
app.resizable(False,False)

def answer():
    x=ans.get(0.0,'end-1c')
    k=eval(x)
    ans.delete(0.0,'end-1c')
    ans.insert('end',k)


ans=CTkTextbox(app,height=80,width=240,font=("",20,"bold"))
ans.place(x=0,y=0)

bu1=CTkButton(app,text="AC",text_color="#C17033",fg_color="#243441",font=("",25,"bold"),width=55,command=lambda:ans.delete(0.0,'end'))
bu1.place(x=0,y=81)

bu1=CTkButton(app,text="<",text_color="#C17033",fg_color="#243441",font=("",25,"bold"),width=58,command=lambda:ans.delete("end-2c", "end-1c"))
bu1.place(x=58,y=81)

bu1=CTkButton(app,text="%",text_color="#C17033",fg_color="#243441",font=("",25,"bold"),width=58,command=lambda:ans.insert('end','%'))
bu1.place(x=119,y=81)

bu1=CTkButton(app,text="/",text_color="#C17033",fg_color="#243441",font=("",25,"bold"),width=58,command=lambda:ans.insert('end','/'))
bu1.place(x=180,y=81)

bu1=CTkButton(app,text="7",text_color="white",fg_color="#243441",font=("",25,"bold"),width=55,command=lambda:ans.insert('end',7))
bu1.place(x=0,y=121)

bu1=CTkButton(app,text="8",text_color="white",fg_color="#243441",font=("",25,"bold"),width=58,command=lambda:ans.insert('end',8))
bu1.place(x=58,y=121)

bu1=CTkButton(app,text="9",text_color="white",fg_color="#243441",font=("",25,"bold"),width=58,command=lambda:ans.insert('end',9))
bu1.place(x=119,y=121)

bu1=CTkButton(app,text="×",text_color="#C17033",fg_color="#243441",font=("",25,"bold"),width=58,command=lambda:ans.insert('end','*'))
bu1.place(x=180,y=121)

bu1=CTkButton(app,text="4",text_color="white",fg_color="#243441",font=("",25,"bold"),width=55,command=lambda:ans.insert('end',4))
bu1.place(x=0,y=161)

bu1=CTkButton(app,text="5",text_color="white",fg_color="#243441",font=("",25,"bold"),width=58,command=lambda:ans.insert('end',5))
bu1.place(x=58,y=161)

bu1=CTkButton(app,text="6",text_color="white",fg_color="#243441",font=("",25,"bold"),width=58,command=lambda:ans.insert('end',6))
bu1.place(x=119,y=161)

bu1=CTkButton(app,text="-",text_color="#C17033",fg_color="#243441",font=("",25,"bold"),width=58,command=lambda:ans.insert('end','-'))
bu1.place(x=180,y=161)

bu1=CTkButton(app,text="1",text_color="white",fg_color="#243441",font=("",25,"bold"),width=55,command=lambda:ans.insert('end',1))
bu1.place(x=0,y=201)

bu1=CTkButton(app,text="2",text_color="white",fg_color="#243441",font=("",25,"bold"),width=58,command=lambda:ans.insert('end',2))
bu1.place(x=58,y=201)

bu1=CTkButton(app,text="3",text_color="white",fg_color="#243441",font=("",25,"bold"),width=58,command=lambda:ans.insert('end',3))
bu1.place(x=119,y=201)

bu1=CTkButton(app,text="+",text_color="#C17033",fg_color="#243441",font=("",25,"bold"),width=58,command=lambda:ans.insert('end','+'))
bu1.place(x=180,y=201)

bu1=CTkButton(app,text="0",text_color="white",fg_color="#243441",font=("",25,"bold"),width=55,command=lambda:ans.insert('end',0))
bu1.place(x=0,y=241)

bu1=CTkButton(app,text=".",text_color="white",fg_color="#243441",font=("",25,"bold"),width=58,command=lambda:ans.insert('end',"."))
bu1.place(x=58,y=241)

bu1=CTkButton(app,text="=",text_color="white",fg_color="#ED802E",font=("",25,"bold"),width=119,command=answer)
bu1.place(x=119,y=241)

app.mainloop()
