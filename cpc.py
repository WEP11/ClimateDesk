import webbrowser
import tkinter as tk
import spc as spc
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
    container.update_idletasks()

    #cWdt = container.winfo_width()
    #cHgt = container.winfo_height()
    cWdt = 1024.0
    cHgt = 768.0
    #print(cWdt, cHgt)

    iHgt = float(imgFile.size[1])
    iWdt = float(imgFile.size[0])
    #print(iWdt, iHgt)
    if iWdt > cWdt:
        pct = (iWdt - cWdt)/iWdt
        #pct = (cWdt/iWdt) - 1.0
        nWdt = int(cWdt)
        nHgt = int(iHgt - (iHgt * pct))
    else:
        nHgt = int(iHgt)
        nWdt = int(iWdt)
    #print(nWdt, nHgt)
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

def hprccObs(container, images):
    multipane = ttk.Notebook(container)

    d7 = ttk.Frame(multipane)
    d14 = ttk.Frame(multipane)
    d30 = ttk.Frame(multipane)
    d60 = ttk.Frame(multipane)
    d90 = ttk.Frame(multipane)
    d120 = ttk.Frame(multipane)
    m6 = ttk.Frame(multipane)
    m12 = ttk.Frame(multipane)
    m24 = ttk.Frame(multipane)
    m36 = ttk.Frame(multipane)
    grow = ttk.Frame(multipane)
    sumr = ttk.Frame(multipane)
    watr = ttk.Frame(multipane)
    year = ttk.Frame(multipane)
    mnth = ttk.Frame(multipane)
    l1 = ttk.Frame(multipane)
    l3 = ttk.Frame(multipane)
    l12 = ttk.Frame(multipane)
    drought = ttk.Frame(multipane)

    multipane.add(d7, text="7 Day")
    multipane.add(d14, text="14 Day")
    multipane.add(d30, text="30 Day")
    multipane.add(d60, text="60 Day")
    multipane.add(d90, text="90 Day")
    multipane.add(d120, text="120 Day")
    multipane.add(m6, text="6 Month")
    multipane.add(m12, text="12 Month")
    multipane.add(m24, text="24 Month")
    multipane.add(m36, text="36 Month")
    multipane.add(grow, text="Apr 1")
    multipane.add(sumr, text="Jul 1")
    multipane.add(watr, text="Oct 1")
    multipane.add(year, text="Annual")
    multipane.add(mnth, text="Month")
    multipane.add(l1, text="Last Month")
    multipane.add(l3, text="Last 3 Months")
    multipane.add(l12, text="Last 12 Months")
    multipane.add(drought, text="Drought")

    multipane.grid(row=0, column=1, rowspan=20, columnspan=10)

    # [d7, d14, d30, d60, d90, d120, m6, m12, m24, m36, grow, sumr, year, water, drought]
    createHprccFrame(d7, images[0])
    createHprccFrame(d14, images[1])
    createHprccFrame(d30, images[2])
    createHprccFrame(d60, images[3])
    createHprccFrame(d90, images[4])
    createHprccFrame(d120, images[5])
    '''
    createHprccFrame(m6, images[6])
    createHprccFrame(m12, images[7])
    createHprccFrame(m24, images[8])
    createHprccFrame(m36, images[9])
    createHprccFrame(grow, images[10])
    createHprccFrame(sumr, images[11])
    createHprccFrame(watr, images[13])
    createHprccFrame(year, images[12])
    createHprccFrame(mnth, images[0])
    createHprccFrame(d7, images[0])
    createHprccFrame(d7, images[0])
    createHprccFrame(d7, images[0])
    '''
    droughtPane = createImageFrame(drought, images[14][0])

    return multipane

def createHprccFrame(container, images):
    f = ttk.Notebook(container)

    p = ttk.Frame(f)
    p_d = ttk.Frame(f)
    p_n = ttk.Frame(f)
    t = ttk.Frame(f)
    t_d = ttk.Frame(f)
    tx = ttk.Frame(f)
    tn = ttk.Frame(f)

    f.add(p, text='Precipitation')
    f.add(p_d, text='Dept from Normal Precip')
    f.add(p_n, text='Pct of Normal Precip')
    f.add(t, text='Temperature')
    f.add(t_d, text='Dept from Normal Temp')
    f.add(tx, text='Max Temperature')
    f.add(tn, text='Min Temperature')
    f.grid(row=0, column=1, rowspan=20, columnspan=10)

    p1 = createImageFrame(p, images[0])
    p2 = createImageFrame(p_d, images[1])
    p3 = createImageFrame(p_n, images[2])
    p4 = createImageFrame(t, images[3])
    p5 = createImageFrame(t_d, images[4])
    p6 = createImageFrame(tx, images[5])
    p7 = createImageFrame(tn, images[6])

def showDiscussions(products):
    window = tk.Toplevel()
    window.wm_title("CPC DISCUSSION TEXT")

    canvas = ttk.Notebook(window)

    d1 = ttk.Frame(canvas)
    d2 = ttk.Frame(canvas)
    d3 = ttk.Frame(canvas)

    canvas.add(d1, text='Short Term')
    canvas.add(d2, text='30 Day')
    canvas.add(d3, text='Long Range')

    canvas.grid(row=0, column=0, rowspan=20, columnspan=10, padx=5, pady=5)

    spc.drawTextScroll(d1, products[5])
    spc.drawTextScroll(d2, products[6])
    spc.drawTextScroll(d3, products[7])

    b = ttk.Button(window, text="Close", command=window.destroy)
    b.grid(row=1, column=0)


def telecon(container, images):
    f = ttk.Notebook(container)

    ao = ttk.Frame(f)
    nao = ttk.Frame(f)
    pna = ttk.Frame(f)
    aao = ttk.Frame(f)

    f.add(ao, text="AO")
    f.add(nao, text="NAO")
    f.add(pna, text="PNA")
    f.add(aao, text="AAO")
    f.grid(row=0, column=1, rowspan=20, columnspan=10)

    p1 = createImageFrame(ao, images[0], noShow=True)
    p1.pack(side="left")
    p2 = createImageFrame(ao, images[1], noShow=True)
    p2.pack(side="left")

    p3 = createImageFrame(nao, images[2], noShow=True)
    p3.pack(side="left")
    p4 = createImageFrame(nao, images[3], noShow=True)
    p4.pack(side="left")

    p5 = createImageFrame(pna, images[4], noShow=True)
    p5.pack(side="left")
    p6 = createImageFrame(pna, images[5], noShow=True)
    p6.pack(side="left")

    p7 = createImageFrame(aao, images[6], noShow=True)
    p7.pack(side="left")
    p8 = createImageFrame(aao, images[7], noShow=True)
    p8.pack(side="left")

    return f
