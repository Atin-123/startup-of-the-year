from tkinter import *
import webbrowser as wb
import os

# wb.open('https://www.facebook.com/') 
#...............................open fb.............................................#
def open_fb():
	wb.open('https://www.facebook.com/') 
#...................................................................................#
#.............................open instra...........................................#
def open_instra():
	wb.open('https://www.instagram.com/?hl=en')
#...................................................................................#
#.............................open chrome...........................................#
def open_chrome():
	os.startfile('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe')
#...................................................................................#
#.............................open Logomaker........................................#
def open_logomaker():
	wb.open('https://logomaker.thehoth.com/')
#...................................................................................#
root=Tk()
root.iconbitmap("logo.ico")
root.title("Shortcuts")
root.geometry("300x700")
root.minsize(300,700)
root.maxsize(300,700)
Label(root,text="",padx=20,pady=20).pack()
Button(root,text="Open Facebook",borderwidth=5,relief="groove",padx=20,pady=20,command=open_fb).pack(padx=10,pady=10)
Label(root,text="",padx=10,pady=10).pack()
Button(root,text="Open Instra",borderwidth=5,relief="groove",padx=20,pady=20,command=open_instra).pack(padx=10,pady=10)
Label(root,text="",padx=10,pady=10).pack()
Button(root,text="Open Chrome",borderwidth=5,relief="groove",padx=20,pady=20,command=open_chrome).pack(padx=10,pady=10)
Label(root,text="",padx=10,pady=10).pack()
Button(root,text="Logo Maker",borderwidth=5,relief="groove",padx=20,pady=20,command=open_logomaker).pack(padx=10,pady=10)
Label(root,text="",padx=10,pady=10).pack()
Button(root,text="currently not in use",borderwidth=5,relief="groove",padx=20,pady=20,command=None).pack(padx=10,pady=10)
root.mainloop()



#.........................if forgot password........................................#
#...................................................................................#

#...................................................................................#