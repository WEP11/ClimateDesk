import tkinter as tk
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

    panel1 = tk.Label(d1c)
    panel1.configure(image=imageList[0])
    panel1.image = imageList[0]
    panel1.pack(side="bottom")

    panel2 = tk.Label(d1t)
    panel2.configure(image=imageList[1])
    panel2.image = imageList[1]
    panel2.pack(side="bottom")

    panel3 = tk.Label(d1w)
    panel3.configure(image=imageList[2])
    panel3.image = imageList[2]
    panel3.pack(side="bottom")

    panel4 = tk.Label(d1h)
    panel4.configure(image=imageList[3])
    panel4.image = imageList[3]
    panel4.pack(side="bottom")

    # DAY TWO ---------------
    d2f = ttk.Notebook(d2)

    d2c = ttk.Frame(d2f)
    d2p = ttk.Frame(d2f)

    d2f.add(d2c, text='Categorical')
    d2f.add(d2p, text='Probabilistic')

    d2f.grid(row=0, column=1, rowspan=20, columnspan=10)

    panel5 = tk.Label(d2c)
    panel5.configure(image=imageList[4])
    panel5.image = imageList[4]
    panel5.pack(side="bottom")

    panel6 = tk.Label(d2p)
    panel6.configure(image=imageList[5])
    panel6.image = imageList[5]
    panel6.pack(side="bottom")

    # DAY THREE ---------------
    d3f = ttk.Notebook(d3)

    d3c = ttk.Frame(d3f)
    d3p = ttk.Frame(d3f)

    d3f.add(d3c, text='Categorical')
    d3f.add(d3p, text='Probabilistic')

    d3f.grid(row=0, column=1, rowspan=20, columnspan=10)

    panel5 = tk.Label(d3c)
    panel5.configure(image=imageList[6])
    panel5.image = imageList[6]
    panel5.pack(side="bottom")

    panel6 = tk.Label(d3p)
    panel6.configure(image=imageList[7])
    panel6.image = imageList[7]
    panel6.pack(side="bottom")

    # DAY 4-8

    panel7 = tk.Label(d4)
    panel7.configure(image=imageList[8])
    panel7.image = imageList[8]
    panel7.pack(side="bottom")

    panel8 = tk.Label(d5)
    panel8.configure(image=imageList[9])
    panel8.image = imageList[9]
    panel8.pack(side="bottom")

    panel9 = tk.Label(d6)
    panel9.configure(image=imageList[10])
    panel9.image = imageList[10]
    panel9.pack(side="bottom")

    panel10 = tk.Label(d7)
    panel10.configure(image=imageList[11])
    panel10.image = imageList[11]
    panel10.pack(side="bottom")

    panel11 = tk.Label(d8)
    panel11.configure(image=imageList[12])
    panel11.image = imageList[12]
    panel11.pack(side="bottom")

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

    panel1 = tk.Label(d1)
    panel1.configure(image=images[3])
    panel1.image = images[3]
    panel1.pack(side="bottom")

    panel2 = tk.Label(d2)
    panel2.configure(image=images[4])
    panel2.image = images[4]
    panel2.pack(side="bottom")

    panel3 = tk.Label(d3)
    panel3.configure(image=images[5])
    panel3.image = images[5]
    panel3.pack(side="bottom")

    return multipane


def drawTextScroll(parent, text):
        l = ScrolledText(parent)
        l.insert(tk.INSERT, text)
        l.grid(row=0, column=0)
