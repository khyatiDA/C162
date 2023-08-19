from tkinter import *
from PIL import Image  , ImageTk
from tkinter import messagebox
from tkinter import filedialog
import os
import webbrowser


window=Tk()

window.title("HTML IDE")
window.minsize(600,600)
window.maxsize(600,600)

window.configure(background ="SandyBrown")

run = ImageTk.PhotoImage(Image.open("run.png"))
open = ImageTk.PhotoImage(Image.open("open_file.png"))
save = ImageTk.PhotoImage(Image.open("save_file.png"))


label = Label(window , text = "File Name")
label.place(relx= 0.38 , rely = 0.05 , anchor = CENTER)

input = Entry(window)
input.place(relx = 0.6 , rely=0.05 , anchor = CENTER)

textArea = Text(window , height = 35 , width = 80)
textArea.place(relx=0.5 , rely = 0.5  , anchor = CENTER)

name = ""
def openFile():
    global name
    textArea.delete(1.0 , END)
    input.delete(0 , END)
    html_file = filedialog.askopenfilename(title = "OPEN HTML FILE" , filetypes = (("Html Files" , "*.html"),))
    print(html_file)
    name = os.path.basename(html_file)
    formated_name = name.split('.')[0]
    input.insert(END , formated_name)
    window.title(formated_name)
    html_file =  open(name , 'r')
    paragraph = html_file.read()
    textArea.insert(END,paragraph)

    html_file.close()

def saveFile():
    input_name = input.get()  
    file = open(input_name+".html" , "w")

    data = textArea.get("1.0" , END)
    print(data)
    file.write(data)


    input.delete(0 , END)
    textArea.delete(1.0 , END)
    messagebox.showinfo("Update" , "Success")

def run_html():
    webbrowser.open(name)


openBtn = Button(window , image = open , command= openFile)
openBtn.place(relx = 0.05 , rely= 0.03 , anchor = CENTER)

saveBtn = Button(window , image = save , command = saveFile)
saveBtn.place(relx = 0.14, rely= 0.05 , anchor = CENTER)


runBtn = Button(window , image = run , command = run_html)
runBtn.place(relx = 0.2, rely= 0.05 , anchor = CENTER)







window.mainloop()