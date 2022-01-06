# Now let's create a tkinter digital string-art design using a
# for-loop. Type and execute/run the tkinter program example
# below and see what happens.

from tkinter import*

root=Tk()

draw=Canvas(root,height=500,width=500,bg='black')
for i in range(0,400,3):
    draw.create_line(50+i,50+i,450,50,450,50,450,450,50,450,50+i,50+i,fill='cyan')
draw.pack()

root.mainloop()

# Now let's create a tkinter digital string-art design using a tkinter
# 'rectangle' command with a for-loop. Type and execute/run the
# tkinter program example below and see what happens.

from tkinter import*

root=Tk()

draw=Canvas(root,height=500,width=500,bg='black')
for i in range(0,96,5):
    draw.create_rectangle(150+i,100+i,340-i,400-i,outline='cyan')
draw.pack()

root.mainloop()

# Now let's create a tkinter digital string-art design using a tkinter
# 'oval' command with a for-loop. Type and execute/run the tkinter
# program example below and see what happens.

from tkinter import*

root=Tk()

draw=Canvas(root,height=500,width=500,bg='black')
for i in range(0,96,5):
    draw.create_oval(150+i,100+i,340-i,400-i,outline='cyan')
draw.pack()

root.mainloop()

# Now let's create a tkinter digital string-art design using a tkinter
# 'arc' command with a for-loop. Type and execute/run the tkinter
# program example below and see what happens.

from tkinter import*

root=Tk()

draw=Canvas(root,height=500,width=500,bg='black')
for i in range(0,140,5):
    draw.create_arc(120+i ,120+i,400-i,400-i,extent=180,outline='cyan')
draw.pack()

root.mainloop()
