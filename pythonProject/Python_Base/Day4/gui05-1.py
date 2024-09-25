import os
from tkinter import*


def find_file(event=None):
    name =ent.get()
    text.insert(END, "==========================================================================" + '\n')
    text.insert(END, name + '\n')
    text.insert(END, "파일 찾기 시작" + '\n')
    text.insert(END, "==========================================================================" + '\n')


    for root, dirs, files in os.walk('C:/dev/PychamProject\/pythonProject/Python_Base/'):
        for file in files:
            if file == name:
                text.insert(END, "파일을 찾았습니다!!" + '\n')
                text.insert(END,os.path.join(root, file)+ '\n')
                text.insert(END, "==========================================================================" + '\n')


app =Tk()
app.title("텍스트 에디터")
app.geometry("700x400")

ent =Entry(app)
ent.grid(row=0,column=0, padx=10, pady=10)
ent.bind("<Return>", find_file)

btn1 = Button(app,text='추가',command=find_file)
btn1.grid(row=0, column=1, padx=10, pady=10)

btn2 = Button(app,text='식제')
btn2.grid(row=0, column=2, padx=10, pady=10)

text =Text(app)
text.grid(row=1, column=0, columnspan=2) # 2칸차지


app.mainloop()


