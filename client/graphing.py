import requests
from tkinter import *
from tkinter.ttk import *
from PIL import ImageTk, Image

root = Tk()
root.title("map generator")
root.geometry=("300x300")

input_height = Entry(root)
input_height.grid(row=0, column=0, padx= 5, pady=5)
Label(root, text="input desired height").grid(row=1, column=0)
input_width = Entry(root)
input_width.grid(row=0, column=1, padx= 5, pady=5)
Label(root, text="input desired width").grid(row=1, column=1)


def generate():
    mapa = Toplevel(root)
    mapa.title("map")
    height_value = input_height.get()
    width_value = input_width.get()
    url_string = "http://localhost:9999/generate?height=" + str(height_value) + "&width=" + str(width_value)
    resp = requests.get(url_string)
    data = resp.json()
    Y = height_value*100
    X = width_value*100
    geometry = str(X)+"x"+str(Y)
    mapa.geometry(geometry)
    mapa.tk.call('tk', 'scaling', 0.5)

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
                    image = Label(mapa, image=tile1)
                    image.grid(row=row, column=column)
                case "TILE2":
                    image = Label(mapa, image=tile2)
                    image.grid(row=row, column=column)
                case "TILE3":
                    image = Label(mapa, image=tile3)
                    image.grid(row=row, column=column)
                case "TILE4":
                    image = Label(mapa, image=tile4)
                    image.grid(row=row, column=column)
                case "TILE5":
                    image = Label(mapa, image=tile5)
                    image.grid(row=row, column=column)
                case "TILE6":
                    image = Label(mapa, image=tile6)
                    image.grid(row=row, column=column)
                case "TILE7":
                    image = Label(mapa, image=tile7)
                    image.grid(row=row, column=column)
                case "TILE8":
                    image = Label(mapa, image=tile8)
                    image.grid(row=row, column=column)
                case _:
                    continue
            column += 1
            if column == len(data["0"]):
                column = 0
        row += 1
        if row == len(data):
            row = 0
    mapa.mainloop()    

generate_button = Button(root, text="Generate new map", command=generate)
generate_button.grid(row=2, column=0, columnspan=2, padx= 5, pady=5)

root.mainloop()
