import webbrowser
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO

from tkinter.scrolledtext import ScrolledText

def callClimateReports():
    webbrowser.open_new_tab("https://www.ncdc.noaa.gov/sotc/")

def createImageFrame(container, image, noShow=False):
    # Open Image
    imgFile = Image.open(BytesIO(image))
    
    # First calculate image size
    #cWdt = container.winfo_width()
    #cHgt = container.winfo_height()
    cWdt = 1024.0
    cHgt = 768.0
    print(cWdt, cHgt)

    iHgt = float(imgFile.size[1])
    iWdt = float(imgFile.size[0])
    print(iWdt, iHgt)
    if iWdt > cWdt:
        pct = (iWdt/cWdt) - 1.0
        nWdt = int(iWdt - (iWdt * pct))
        nHgt = int(iHgt - (iHgt * pct))
    else:
        nHgt = int(iHgt)
        nWdt = int(iWdt)
    print(nWdt, nHgt)
    newImg = imgFile.resize((nWdt, nHgt))
    img = ImageTk.PhotoImage(newImg)
    
    frame = tk.Label(container)
    frame.configure(image=img)
    frame.image = img

    if noShow is False:
        frame.pack(side="bottom")

    return frame

def createCpcFrame(frame, idx, images):
    f = ttk.Notebook(frame)

    ft = ttk.Frame(f)
    fp = ttk.Frame(f)

    f.add(ft, text='Temperature')
    f.add(fp, text='Precipitation')
    f.grid(row=0, column=1, rowspan=20, columnspan=10)

    p1 = createImageFrame(ft, images[idx])
    p2 = createImageFrame(fp, images[idx+1])



def cpcLrOutlook(container, images):
    multipane = ttk.Notebook(container)

    f1 = ttk.Frame(multipane)
    f2 = ttk.Frame(multipane)
    f3 = ttk.Frame(multipane)
    f4 = ttk.Frame(multipane)
    f5 = ttk.Frame(multipane)
    f6 = ttk.Frame(multipane)
    f7 = ttk.Frame(multipane)
    f8 = ttk.Frame(multipane)
    f9 = ttk.Frame(multipane)
    f10 = ttk.Frame(multipane)
    f11 = ttk.Frame(multipane)
    f12 = ttk.Frame(multipane)
    f13 = ttk.Frame(multipane)

    multipane.add(f1, text='Current')
    multipane.add(f2, text='+1')
    multipane.add(f3, text='+2')
    multipane.add(f4, text='+3')
    multipane.add(f5, text='+4')
    multipane.add(f6, text='+5')
    multipane.add(f7, text='+6')
    multipane.add(f8, text='+7')
    multipane.add(f9, text='+8')
    multipane.add(f10, text='+9')
    multipane.add(f11, text='+10')
    multipane.add(f12, text='+11')
    multipane.add(f13, text='+12')

    multipane.grid(row=0, column=1, rowspan=20, columnspan=10)

    createCpcFrame(f1, 0, images)
    createCpcFrame(f2, 2, images)
    createCpcFrame(f3, 4, images)
    createCpcFrame(f4, 6, images)
    createCpcFrame(f5, 8, images)
    createCpcFrame(f6, 10, images)
    createCpcFrame(f7, 12, images)
    createCpcFrame(f8, 14, images)
    createCpcFrame(f9, 16, images)
    createCpcFrame(f10, 18, images)
    createCpcFrame(f11, 20, images)
    createCpcFrame(f12, 22, images)
    createCpcFrame(f13, 24, images)

    return multipane

def currentConditions(panel, container, images):
    panel.grid_forget()
    multipane = ttk.Notebook(container)

    d7 = ttk.Frame(multipane)

    multipane.add(d7, text='30 Day')
    multipane.grid(row=0, column=1, rowspan=20, columnspan=10)



def cpcOutlook(container, images, droughtImages):
    multipane = ttk.Notebook(container)

    day610 = ttk.Frame(multipane)
    day814 = ttk.Frame(multipane)
    m1 = ttk.Frame(multipane)
    drt = ttk.Frame(multipane)

    multipane.add(day610, text='6-10 Day')
    multipane.add(day814, text='8-14 Day')
    multipane.add(m1, text='1 Month')
    multipane.add(drt, text='Drought')
    multipane.grid(row=0, column=1, rowspan=20, columnspan=10)

    # 6-10 DAY
    createCpcFrame(day610, 0, images)

    # 8-14 DAY
    createCpcFrame(day814, 2, images)

    # 1 Month
    createCpcFrame(m1, 4, images)

    # Drought
    f4 = ttk.Notebook(drt)

    f4mnth = ttk.Frame(f4)
    f4seas = ttk.Frame(f4)

    f4.add(f4mnth, text='Monthly')
    f4.add(f4seas, text='Seasonal')
    f4.grid(row=0, column=1, rowspan=20, columnspan=10)

    f4p1 = createImageFrame(f4mnth, droughtImages[0])
    f4p2 = createImageFrame(f4seas, droughtImages[1])

    return multipane
