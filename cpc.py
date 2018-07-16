import webbrowser
import tkinter as tk
import spc as spc
from tkinter import ttk
from PIL import Image, ImageTk
from io import BytesIO

from tkinter.scrolledtext import ScrolledText


def callClimateReports():
    """Opens NCEI climate reports in the default browser"""
    webbrowser.open_new_tab("https://www.ncdc.noaa.gov/sotc/")


def createImageFrame(container, image, noShow=False):
    """Creates an image within a parent container"""
    # Open Image
    imgFile = Image.open(BytesIO(image))

    # First calculate image size
    container.update_idletasks()

    # cWdt = container.winfo_width()
    # cHgt = container.winfo_height()
    cWdt = 1024.0
    cHgt = 768.0
    # print(cWdt, cHgt)

    iHgt = float(imgFile.size[1])
    iWdt = float(imgFile.size[0])
    # print(iWdt, iHgt

    # Scale the image if the height or width exceeds the window resolution
    if iWdt > cWdt:
        pct = (iWdt - cWdt)/iWdt
        nWdt = int(cWdt)
        nHgt = int(iHgt - (iHgt * pct))
    elif iHgt > cHgt:
        pct = (iHgt - cHgt)/iHgt
        nHgt = int(cHgt)
        nWdt = int(iWdt - (iWdt * pct))
    else:
        nHgt = int(iHgt)
        nWdt = int(iWdt)

    if nHgt > cHgt:
        pct = (nHgt - cHgt)/nHgt
        nHgt = int(cHgt)
        nWdt = int(nWdt - (nWdt * pct))
    else:
        nHgt = int(nHgt)
        nWdt = int(nWdt)
    # print(nWdt, nHgt)
    newImg = imgFile.resize((nWdt, nHgt))
    img = ImageTk.PhotoImage(newImg)

    frame = tk.Label(container)
    frame.configure(image=img)
    frame.image = img

    if noShow is False:
        frame.pack(side="bottom")

    return frame


def createCpcFrame(frame, idx, images):
    """Creates a tabbed CPC outlook container within a parent container"""
    f = ttk.Notebook(frame)

    ft = ttk.Frame(f)
    fp = ttk.Frame(f)

    f.add(ft, text='Temperature')
    f.add(fp, text='Precipitation')
    f.grid(row=0, column=1, rowspan=20, columnspan=10)

    p1 = createImageFrame(ft, images[idx])
    p2 = createImageFrame(fp, images[idx+1])


def cpcLrOutlook(container, images):
    """
    Creates a tabbed CPC long range outlook container
    within a parent container
    """
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


def cpcOutlook(container, images, droughtImages):
    """Creates a CPC and drought outlook container within a parent container"""
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
    """
    Creates a tabbed HPRCC climate map container within a parent container.
    """
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
    """
    Creates a tabbed HPRCC product frame for a parent HPRCC timescale frame
    """
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
    """
    Creates a window with a scrolling text view of the CPC discussions.
    """
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
    """
    Creates a tabbed container with the CPC teleconnection outlooks
    """
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


def enso(container, images):
    """
    Creates a tabbed container with the CPC ENSO information
    """
    f = ttk.Notebook(container)

    sst = ttk.Frame(f)
    olr = ttk.Frame(f)
    wind = ttk.Frame(f)
    sea = ttk.Frame(f)
    outlook = ttk.Frame(f)

    f.add(sst, text="SST")
    f.add(olr, text="OLR")
    f.add(wind, text="Wind")
    f.add(sea, text="Ocean")
    f.add(outlook, text="Nino 3.4 Outlook")
    f.grid(row=0, column=1, rowspan=20, columnspan=10)

    createSstTabs(sst, images)
    createWindTabs(wind, images)
    createSeaTabs(sea, images)
    createEnsoOutlookTabs(outlook, images)

    p1 = createImageFrame(olr, images[4], noShow=True)
    p1.pack(side="left")
    p2 = createImageFrame(olr, images[5], noShow=True)
    p2.pack(side="left")

    return f


def createSstTabs(container, images):
    f = ttk.Notebook(container)

    nino = ttk.Frame(f)
    obs = ttk.Frame(f)

    f.add(nino, text="Nino Regions")
    f.add(obs, text="Observations")
    f.grid(row=0, column=1, rowspan=20, columnspan=10)

    p1 = createImageFrame(obs, images[0], noShow=True)
    p1.pack(side="left")
    p2 = createImageFrame(obs, images[1], noShow=True)
    p2.pack(side="left")

    p3 = createImageFrame(nino, images[2], noShow=True)
    p3.pack(side="left")
    p4 = createImageFrame(nino, images[3], noShow=True)
    p4.pack(side="left")


def createWindTabs(container, images):
    f = ttk.Notebook(container)

    mapA = ttk.Frame(f)
    timLonA = ttk.Frame(f)

    f.add(mapA, text="Map Anomalies")
    f.add(timLonA, text="Time-Longitude Anom")
    f.grid(row=0, column=1, rowspan=20, columnspan=10)

    p1 = createImageFrame(mapA, images[6], noShow=True)
    p1.pack(side="top")
    p2 = createImageFrame(mapA, images[7], noShow=True)
    p2.pack(side="top")

    p3 = createImageFrame(timLonA, images[8])


def createSeaTabs(container, images):
    f = ttk.Notebook(container)

    temps = ttk.Frame(f)
    iso = ttk.Frame(f)
    m55 = ttk.Frame(f)
    m105 = ttk.Frame(f)
    m155 = ttk.Frame(f)
    seaLvl = ttk.Frame(f)

    f.add(temps, text="Temperature")
    f.add(iso, text="20C Isotherm")
    f.add(m55, text="55m")
    f.add(m105, text="105m")
    f.add(m155, text="155m")
    f.add(seaLvl, text="Sea Level")
    f.grid(row=0, column=1, rowspan=20, columnspan=10)

    p1 = createImageFrame(temps, images[9], noShow=True)
    p1.pack(side="left")
    p2 = createImageFrame(temps, images[16], noShow=True)
    p2.pack(side="left")

    p3 = createImageFrame(iso, images[10], noShow=True)
    p3.pack(side="left")
    p4 = createImageFrame(iso, images[11], noShow=True)
    p4.pack(side="left")

    p5 = createImageFrame(m55, images[12])
    p6 = createImageFrame(m105, images[13])
    p7 = createImageFrame(m155, images[14])
    p8 = createImageFrame(seaLvl, images[15])


def createEnsoOutlookTabs(container, images):
    f = ttk.Notebook(container)
    ta = ttk.Frame(f)
    sa = ttk.Frame(f)
    t = ttk.Frame(f)

    f.add(ta, text="Anomaly")
    f.add(sa, text="Std Anomaly")
    f.add(t, text="Temperature")
    f.grid(row=0, column=1, rowspan=20, columnspan=10)

    p5 = createImageFrame(ta, images[17])
    p6 = createImageFrame(sa, images[18])
    p7 = createImageFrame(t, images[19])


def mjo(container, images):
    f = ttk.Notebook(container)
    cpc = ttk.Frame(f)
    d40 = ttk.Frame(f)
    d90 = ttk.Frame(f)

    f.add(cpc, text="CPC Index")
    f.add(d40, text="40 Day WH")
    f.add(d90, text="90 Day WH")
    f.grid(row=0, column=1, rowspan=20, columnspan=10)

    p5 = createImageFrame(cpc, images[0])
    p6 = createImageFrame(d40, images[1])
    p7 = createImageFrame(d90, images[2])

    return f


def blocking(container, images):
    f = ttk.Notebook(container)
    nh = ttk.Frame(f)
    sh = ttk.Frame(f)

    f.add(nh, text="NH")
    f.add(sh, text="SH")
    f.grid(row=0, column=1, rowspan=20, columnspan=10)

    p1 = createImageFrame(nh, images[0], noShow=True)
    p1.pack(side="left")
    p2 = createImageFrame(nh, images[1], noShow=True)
    p2.pack(side="left")

    p3 = createImageFrame(sh, images[2], noShow=True)
    p3.pack(side="left")
    p4 = createImageFrame(sh, images[3], noShow=True)
    p4.pack(side="left")

    return f
