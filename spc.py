import tkinter as tk
import cpc as cpc
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.scrolledtext import ScrolledText


def showSpcOutlook(container, imageList, text_prods):
    multipane = ttk.Notebook(container)

    d1 = ttk.Frame(multipane)
    d2 = ttk.Frame(multipane)
    d3 = ttk.Frame(multipane)
    d4 = ttk.Frame(multipane)
    d5 = ttk.Frame(multipane)
    d6 = ttk.Frame(multipane)
    d7 = ttk.Frame(multipane)
    d8 = ttk.Frame(multipane)

    multipane.add(d1, text='Day 1')
    multipane.add(d2, text='Day 2')
    multipane.add(d3, text='Day 3')
    multipane.add(d4, text='Day 4')
    multipane.add(d5, text='Day 5')
    multipane.add(d6, text='Day 6')
    multipane.add(d7, text='Day 7')
    multipane.add(d8, text='Day 8')
    multipane.grid(row=0, column=1, rowspan=20, columnspan=10)

    # DAY ONE ---------------
    d1f = ttk.Notebook(d1)

    d1c = ttk.Frame(d1f)
    d1t = ttk.Frame(d1f)
    d1w = ttk.Frame(d1f)
    d1h = ttk.Frame(d1f)

    d1f.add(d1c, text='Categorical')
    d1f.add(d1t, text='Tornado')
    d1f.add(d1w, text='Wind')
    d1f.add(d1h, text='Hail')
    d1f.grid(row=0, column=1, rowspan=20, columnspan=10)

    panel1 = cpc.createImageFrame(d1c, imageList[0])
    panel2 = cpc.createImageFrame(d1t, imageList[1])
    panel3 = cpc.createImageFrame(d1w, imageList[2])
    panel4 = cpc.createImageFrame(d1h, imageList[3])

    # DAY TWO ---------------
    d2f = ttk.Notebook(d2)

    d2c = ttk.Frame(d2f)
    d2p = ttk.Frame(d2f)

    d2f.add(d2c, text='Categorical')
    d2f.add(d2p, text='Probabilistic')

    d2f.grid(row=0, column=1, rowspan=20, columnspan=10)

    panel5 = cpc.createImageFrame(d2c, imageList[4])
    panel6 = cpc.createImageFrame(d2p, imageList[5])

    # DAY THREE ---------------
    d3f = ttk.Notebook(d3)

    d3c = ttk.Frame(d3f)
    d3p = ttk.Frame(d3f)

    d3f.add(d3c, text='Categorical')
    d3f.add(d3p, text='Probabilistic')

    d3f.grid(row=0, column=1, rowspan=20, columnspan=10)

    panel5 = cpc.createImageFrame(d3c, imageList[6])
    panel6 = cpc.createImageFrame(d3p, imageList[7])

    # DAY 4-8

    panel7 = cpc.createImageFrame(d4, imageList[8])
    panel8 = cpc.createImageFrame(d5, imageList[9])
    panel9 = cpc.createImageFrame(d6, imageList[10])
    panel10 = cpc.createImageFrame(d7, imageList[11])
    panel11 = cpc.createImageFrame(d8, imageList[12])

    spcTextWindow(text_prods)

    return multipane


def spcTextWindow(product_list):
    window = tk.Toplevel()
    window.wm_title("SPC DISCUSSION TEXT")

    canvas = ttk.Notebook(window)

    d1 = ttk.Frame(canvas)
    d2 = ttk.Frame(canvas)
    d3 = ttk.Frame(canvas)
    d48 = ttk.Frame(canvas)

    canvas.add(d1, text='Day 1')
    canvas.add(d2, text='Day 2')
    canvas.add(d3, text='Day 3')
    canvas.add(d48, text='Day 4-8')

    canvas.grid(row=0, column=0, rowspan=20, columnspan=10, padx=5, pady=5)

    drawTextScroll(d1, product_list[0])
    drawTextScroll(d2, product_list[1])
    drawTextScroll(d3, product_list[2])
    drawTextScroll(d48, product_list[3])

    b = ttk.Button(window, text="Close", command=window.destroy)
    b.grid(row=1, column=0)


def showForecast(container, images):
    multipane = ttk.Notebook(container)

    d1 = ttk.Frame(multipane)
    d2 = ttk.Frame(multipane)
    d3 = ttk.Frame(multipane)

    multipane.add(d1, text='Day 4')
    multipane.add(d2, text='Day 5')
    multipane.add(d3, text='Day 6')
    multipane.grid(row=0, column=1, rowspan=20, columnspan=10)

    panel1 = cpc.createImageFrame(d1, images[3])
    panel2 = cpc.createImageFrame(d2, images[4])
    panel3 = cpc.createImageFrame(d3, images[5])
    
    return multipane


def drawTextScroll(parent, text):
        l = ScrolledText(parent)
        l.insert(tk.INSERT, text)
        l.grid(row=0, column=0)
