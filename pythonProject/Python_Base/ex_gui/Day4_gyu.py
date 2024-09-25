from tkinter import *
from tkinter import messagebox

import Python_Base.Day2.luck
from Python_Base.Day2.luck import make_lotto
from Python_Base.Day2.luck import user_lotto

# def user_get_lotto():
#     message10 = txt.get().split(" ")
#     messagebox.showinfo("로또번호",user_lotto(message10))

app =Tk()
app.geometry('300x100')
app.title('로또번호 생성기')
# def get_lotto():
#     print("클릭됨")
#     msg = txt.get()
#     messagebox.showinfo("로또 번호",make_lotto())


def num_lotto():
    msg = txt.get()
    cnt = int(msg)
    for i in range(cnt):

        num = make_lotto()


    messagebox.showinfo("로또 번호",num)


#     alert 과 같은 역할


lbl =Label(app,text="수량")
lbl.grid(row=0,column=0, padx=10, pady=10)

txt =Entry(app)
txt.grid(row=0,column=1, padx=10, pady=10)

btn = Button(app,text="생성", command= num_lotto)
btn.grid(row=1, column=1, columnspan=2,sticky='ew', padx=10, pady=10)
app.mainloop()

