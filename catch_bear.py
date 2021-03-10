import tkinter as tk
from tkinter import messagebox

import random

def mouseclick(params):
      y = params.y
      x = params.x
      s = str(x) + " " + str(y)
      win.title(s)
      #messagebox.showinfo(title="Поймай медведя", message=s)
      r = 5
      canv.create_oval(x-r,y-r,x+r,y+r,width=1)     
      if abs(x - bearX) < 10 and abs(y - bearY) < 10:
            img = canv.create_image(bearX, bearY, image=bear)            
            messagebox.showinfo("Поймай медведя", "поймал!")
            canv.clear(img)
      else:
            s = ""
            if y < bearY:
                  s += " Южнее"
            else:
                  s += " Севернее"
            if x > bearX:
                  s += " Западнее"
            else:
                  s += " Восточнее"
            messagebox.showinfo("Промах", s)
       
bearX = 150
bearY = 70

win = tk.Tk()
win.geometry()
canv = tk.Canvas(win, width=600, height=400, bg='green')
canv.pack()
bear=tk.PhotoImage(file="bear.png")


win.bind("<1>", mouseclick)
win.mainloop()