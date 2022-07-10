from cProfile import label
import tkinter as tk

def addition():
    txt1 = int(box1.get())
    txt2 = int(box2.get())
    txt3 = (txt1+txt2)
    box3.insert(0, txt3)
    
def sub():
    txt1 = int(box1.get())
    txt2 = int(box2.get())
    txt3 = (txt1-txt2)
    box3.insert(0, txt3)

def mult():
    txt1 = int(box1.get())
    txt2 = int(box2.get())
    txt3 = (txt1*txt2)
    box3.insert(0, txt3)

def div():
    txt1 = int(box1.get())
    txt2 = int(box2.get())
    txt3 = (txt1/txt2)
    box3.insert(0, txt3)

def clear():
    box1.delete(0, tk.END)
    box2.delete(0, tk.END)
    box3.delete(0, tk.END) 

app = tk.Tk()
app.title("Calculator")
app.geometry("880x300")
app.iconbitmap("jonty_dp_G1h_icon.ico")
button1 = tk.Button(app , font=("Arial",15),bg ="Orange",text ="+",command=addition)
button1.place(x=102 , y= 150 , width = 70)

button2 = tk.Button(app , font=("Arial",15),bg ="Orange",text ="-",command=sub)
button2.place(x=202 , y= 150 , width = 70)

button3 = tk.Button(app , font=("Arial",15),bg ="Orange",text ="x",command=mult)
button3.place(x=302 , y= 150 , width = 70)

button4 = tk.Button(app , font=("Arial",15),bg ="Orange",text ="÷",command=div)
button4.place(x=402 , y= 150 , width = 70)

button5 = tk.Button(app , font=("Arial",15),bg ="#D3D3D3",text ="CE",command=clear)
button5.place(x=502 , y= 150 , width = 70)

label1 =tk.Label(app, text = "Enter First Number:",font = ("Arial", 15))
label1.place(x=0, y=0)

label2 =tk.Label(app, text = "Enter second Number:",font = ("Arial", 15))
label2.place(x=0, y=100)

label3 =tk.Label(app, text = "Output:",font = ("Arial", 15))
label3.place(x=0, y=220)

box1 = tk.Entry(app, font = ("Arial", 25), bg="#D3D3D3")
box1.place(x=210, y=10)

box2 = tk.Entry(app, font = ("Arial", 25), bg="#D3D3D3")
box2.place(x=210, y=100)

box3 = tk.Entry(app, font = ("Arial", 25), bg="#D3D3D3")
box3.place(x=210, y=210)

image = tk.PhotoImage(file="calcc.png" , height= 500,width=500)
label = tk.Label(image = image)
label.place(x=580, y=0)
app.mainloop()