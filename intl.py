import tkinter as tk
import cpc
from tkinter import ttk


def createIntlFrame(container, images):
    """
    This creates the time-product tabs within an international region
    """
    f = ttk.Notebook(container)

    products = ['Total Precipitation', 'Maximum Temperature',
                'Minimum Temperature', 'Temperature Anomaly']

    times = ['Weekly', 'Monthly', '3-Month']

    wk = ttk.Frame(f)
    mnth = ttk.Frame(f)
    m3 = ttk.Frame(f)

    f.add(wk, text='Weekly')
    f.add(mnth, text='Monthly')
    f.add(m3, text='3-Month')
    f.grid(row=0, column=1, rowspan=20, columnspan=10)

    frames = [wk, mnth, m3]
    for idx, frame in enumerate(frames):
        timeFrame = ttk.Notebook(frame)

        tp = ttk.Frame(timeFrame)
        mx = ttk.Frame(timeFrame)
        mn = ttk.Frame(timeFrame)
        ano = ttk.Frame(timeFrame)

        timeFrame.add(tp, text='Total Precipitation')
        timeFrame.add(mx, text='Maximum Temperature')
        timeFrame.add(mn, text='Minimum Temperature')
        timeFrame.add(ano, text='Temperature Anomaly')

        timeFrame.grid(row=0, column=1, rowspan=20, columnspan=10)

        p1 = cpc.createImageFrame(tp, images[idx][0])
        p2 = cpc.createImageFrame(mx, images[idx][1])
        p3 = cpc.createImageFrame(mn, images[idx][2])
        p4 = cpc.createImageFrame(ano, images[idx][3])


def africa(container, images):
    """Creates the Africa tab container within a parent container"""
    multipane = ttk.Notebook(container)

    f11 = ttk.Frame(multipane)
    f12 = ttk.Frame(multipane)

    multipane.add(f11, text='South Africa')
    multipane.add(f12, text='Northwest Africa')

    multipane.grid(row=0, column=1, rowspan=20, columnspan=10)

    createIntlFrame(f11, images[11])
    createIntlFrame(f12, images[12])

    return multipane


def asia(container, images):
    """ Creates the Asia tab container within a parent container"""
    multipane = ttk.Notebook(container)

    f2 = ttk.Frame(multipane)
    f5 = ttk.Frame(multipane)
    f6 = ttk.Frame(multipane)

    multipane.add(f2, text='East Asia')
    multipane.add(f5, text='Southeast Asia')
    multipane.add(f6, text='South Asia')

    multipane.grid(row=0, column=1, rowspan=20, columnspan=10)

    createIntlFrame(f2, images[2])
    createIntlFrame(f5, images[5])
    createIntlFrame(f6, images[6])

    return multipane


def australia(container, images):
    """ Creates the Australia tab container within a parent container"""
    multipane = ttk.Notebook(container)

    f2 = ttk.Frame(multipane)

    multipane.add(f2, text='Australia')

    multipane.grid(row=0, column=1, rowspan=20, columnspan=10)

    createIntlFrame(f2, images[7])

    return multipane


def canada(container, images):
    """ Creates the Canada tab container within a parent container"""
    multipane = ttk.Notebook(container)

    f2 = ttk.Frame(multipane)
    f5 = ttk.Frame(multipane)

    multipane.add(f2, text='Southeast Canada')
    multipane.add(f5, text='Canadian Prairie')

    multipane.grid(row=0, column=1, rowspan=20, columnspan=10)

    createIntlFrame(f2, images[18])
    createIntlFrame(f5, images[10])

    return multipane


def europe(container, images):
    """ Creates the Europe tab container within a parent container"""
    multipane = ttk.Notebook(container)

    f2 = ttk.Frame(multipane)

    multipane.add(f2, text='Europe')

    multipane.grid(row=0, column=1, rowspan=20, columnspan=10)

    createIntlFrame(f2, images[1])

    return multipane


def caucas(container, images):
    """ Creates the East Europe tab container within a parent container"""
    multipane = ttk.Notebook(container)

    f2 = ttk.Frame(multipane)
    f5 = ttk.Frame(multipane)
    f6 = ttk.Frame(multipane)

    multipane.add(f2, text='Western')
    multipane.add(f5, text='Newlands')
    multipane.add(f6, text='Central')

    multipane.grid(row=0, column=1, rowspan=20, columnspan=10)

    createIntlFrame(f2, images[3])
    createIntlFrame(f5, images[4])
    createIntlFrame(f6, images[14])

    return multipane


def mexico(container, images):
    """ Creates the Mexico tab container within a parent container"""
    multipane = ttk.Notebook(container)

    f2 = ttk.Frame(multipane)

    multipane.add(f2, text='Mexico')

    multipane.grid(row=0, column=1, rowspan=20, columnspan=10)

    createIntlFrame(f2, images[9])

    return multipane


def mideast(container, images):
    """ Creates the Middle East tab container within a parent container"""
    multipane = ttk.Notebook(container)

    f2 = ttk.Frame(multipane)

    multipane.add(f2, text='Middle East')

    multipane.grid(row=0, column=1, rowspan=20, columnspan=10)

    createIntlFrame(f2, images[13])

    return multipane


def southAmerica(container, images):
    """ Creates the South America tab container within a parent container"""
    multipane = ttk.Notebook(container)

    f2 = ttk.Frame(multipane)
    f5 = ttk.Frame(multipane)
    f6 = ttk.Frame(multipane)

    multipane.add(f2, text='North')
    multipane.add(f5, text='South')

    multipane.grid(row=0, column=1, rowspan=20, columnspan=10)

    createIntlFrame(f2, images[15])
    createIntlFrame(f5, images[8])

    return multipane
