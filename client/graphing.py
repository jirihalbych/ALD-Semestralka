import requests
from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("map")
resp = requests.get('http://localhost:9999/generate?height=10&width=19')
data = resp.json()
Y = len(data)*100
X = len(data["0"])*100
geometry = str(X)+"x"+str(Y)
root.geometry(geometry)
root.tk.call('tk', 'scaling', 0.5)

tile1im = Image.open("./tileset/TILE1.jpg")
tile1 = ImageTk.PhotoImage(tile1im)
tile2im = Image.open("./tileset/TILE2.jpg")
tile2 = ImageTk.PhotoImage(tile2im)
tile3im = Image.open("./tileset/TILE3.jpg")
tile3 = ImageTk.PhotoImage(tile3im)
tile4im = Image.open("./tileset/TILE4.jpg")
tile4 = ImageTk.PhotoImage(tile4im)
tile5im = Image.open("./tileset/TILE5.jpg")
tile5 = ImageTk.PhotoImage(tile5im)
tile6im = Image.open("./tileset/TILE6.jpg")
tile6 = ImageTk.PhotoImage(tile6im)
tile7im = Image.open("./tileset/TILE7.jpg")
tile7 = ImageTk.PhotoImage(tile7im)
tile8im = Image.open("./tileset/TILE8.jpg")
tile8 = ImageTk.PhotoImage(tile8im)


row = 0
column = 0

for index in data:
    for tile in data[index]:
        match tile:
            case "TILE1":
                image = Label(root, image=tile1)
                image.grid(row=row, column=column)
            case "TILE2":
                image = Label(root, image=tile2)
                image.grid(row=row, column=column)
            case "TILE3":
                image = Label(root, image=tile3)
                image.grid(row=row, column=column)
            case "TILE4":
                image = Label(root, image=tile4)
                image.grid(row=row, column=column)
            case "TILE5":
                image = Label(root, image=tile5)
                image.grid(row=row, column=column)
            case "TILE6":
                image = Label(root, image=tile6)
                image.grid(row=row, column=column)
            case "TILE7":
                image = Label(root, image=tile7)
                image.grid(row=row, column=column)
            case "TILE8":
                image = Label(root, image=tile8)
                image.grid(row=row, column=column)
            case _:
                continue
        column += 1
        if column == len(data["0"]):
            column = 0
    row += 1
    if row == len(data):
        row = 0

root.mainloop()