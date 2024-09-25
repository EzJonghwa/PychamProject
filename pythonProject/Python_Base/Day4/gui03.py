from tkinter import *
from PIL import Image, ImageTk
# pip install pillow 이미지 관련 라이브러리





def move_left(event):
    print('왼쪽')
    canvas.move('tiger',-10,0)
def move_right(event):
    print('오른쪽')
    canvas.move('tiger', 10, 0)

def move_up(event):
    print('위')
    canvas.move('tiger', 0, -10)
def move_down(event):
    print('아래')
    canvas.move('tiger', 0, 10)

def move_space(event):
    for _ in range(30):
        for _ in range(10):
            canvas.move('tiger',0,-10)
            canvas.update()
            canvas.after(20)
        for _ in range(10):
            canvas.move('tiger', 0, 10)
            canvas.update()
            canvas.after(20)

app =Tk()
canvas = Canvas(app,width=400,height=300)
canvas.pack()            #x1,y1,x2,y2 사각형에 원을 그림 좌상단과 우하단의 좌표
img =Image.open('tiger.png')
img = img.resize((100,100))
item = ImageTk.PhotoImage(img)
canvas.create_image(100,100, image=item, tag='tiger')
# item = canvas.create_oval(100,150,150,200,fill='red')
canvas.bind('<Left>', move_left)
canvas.bind('<Right>', move_right)
canvas.bind('<Up>', move_up)
canvas.bind('<Down>', move_down)
canvas.bind('<space>', move_space)
canvas.focus_set()
canvas.mainloop()