from tkinter import *

'''hàm xử lý button click'''
def donothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()

def win2():
    win2 = Tk()
    win2.title("Second windows")
    win2.geometry('1000x600')
    lb = Label(win2,text="hello")
    lb.place(x=10,y=10)
    

root = Tk()
menubar = Menu(root)

#Tạo menu File
filemenu = Menu(menubar, tearoff=1)
#
filemenu.add_command(label="New", command=win2)
filemenu.add_command(label="Open", command=donothing)
filemenu.add_command(label="Save", command=donothing)
filemenu.add_command(label="Save as...", command=donothing)
filemenu.add_command(label="Close", command=donothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)

menubar.add_cascade(label="File", menu=filemenu)

subsubmenu = Menu(filemenu)
subsubmenu.add_command(label = "One")
subsubmenu.add_command(label = "Two")
filemenu.add_cascade(label = "Submenu", menu=subsubmenu)

editmenu = Menu(menubar, tearoff=5)
editmenu.add_command(label="Undo", command=donothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()
