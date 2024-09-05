import tkinter as tk
import tkinter.ttk as ttk
import math
from PIL import Image, ImageTk
from functools import partial

# Windows initialisation
root = tk.Tk()
root.title('Tic Tac Toe game')
root.geometry('700x700')
root.configure(background='white')

# Button style initialization
style = ttk.Style()
button_font = ("Helvetica", 26, "bold")
style.configure('W.TButton', background='grey')

# Free Icon from https://www.flaticon.com/fr/auteurs/seochan
# Need to resize the image with PIL
img = (Image.open("sign/x.png"))
resized_image = img.resize((200, 200))
xImg = ImageTk.PhotoImage(resized_image)

img = (Image.open("sign/o.png"))
resized_image = img.resize((200, 200))
oImg = ImageTk.PhotoImage(resized_image)

#oImg = tk.PhotoImage(file="sign/o2.png")

COUNT = 1

def play(n, r, c):
    print(f"Play argument : n={n}, r={r}, c={c})")
    global xImg, oImg, COUNT
    cname = f"cnane{n}"
    query = f'{cname} = tk.Canvas(root, width=200, height=200, highlightthickness=1, highlightbackground="black")'
    exec(query)

    # Add padding on frame to center frames
    if c == 0:
        px = 50
    else:
        px = 0

    if r == 0:
        py = 50
    else:
        py = 0

    query = f'{cname}.grid(row={r}, column={c}, padx = ({px}, 0), pady = ({py}, 0))'
    exec(query)
    if COUNT%2 == 1:
        query = f'{cname}.create_image(100, 100, anchor="center", image=xImg)'
    else:
        query = f'{cname}.create_image(100, 100, anchor="center", image=oImg)'
    exec(query)
    COUNT += 1
    print(COUNT)


for x in range(9):
    row_n = math.trunc(x / 3)
    col_n = x % 3

    # Create a frame to contain the buttons and center it
    fname = 'frame' + str(x)
    query = f'{fname} = tk.Frame(root, width=200, height=200, bg="lightgrey")'
    exec(query)
    query = f'{fname}.grid_propagate(False)'  # Prevent the frame from resizing based on its contents
    exec(query)

    # Add padding on frame to center frames
    if col_n == 0:
        px = 50
    else:
        px = 0

    if row_n == 0:
        py = 50
    else:
        py = 0

    query = f'{fname}.grid(row={row_n}, column={col_n}, padx = ({px}, 0), pady = ({py}, 0))'
    exec(query)

    # Configure the grid layout of the frame to allow the button to expand
    query = f'{fname}.columnconfigure({col_n}, weight=1)'
    exec(query)
    query = f'{fname}.rowconfigure({row_n}, weight=1)'
    exec(query)

    # Create the Button
    bname = 'btn' + str(x)
    query = f'{bname} = ttk.Button({fname}, style="W.TButton", command=partial(play, {x}, {row_n}, {col_n}))'
    exec(query)
    query = f'{bname}.grid(row={str(row_n)}, column={str(col_n)}, sticky="nsew")'
    exec(query)


root.mainloop()
