import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import requests
import webbrowser
from tkinter.scrolledtext import ScrolledText

from io import BytesIO

from bs4 import BeautifulSoup as bshtml

def callClimateReports():
    webbrowser.open_new_tab("https://www.ncdc.noaa.gov/sotc/")

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.images = []
        self.text_prods = []

        self.multipane = None

        self.pack()
        self.downloadImages()
        self.create_widgets()

    def downloadImages(self):
        """
        Downloads all images. The images need to be referenced to the
        application to hide from the garbage collecter, so we do it all here.
        """

        links = [
            "http://www.wpc.ncep.noaa.gov/noaa/noaad1.gif",
            "http://www.wpc.ncep.noaa.gov/noaa/noaad2.gif",
            "http://www.wpc.ncep.noaa.gov/noaa/noaad3.gif",
            "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20181901632_GOES16-ABI-CONUS-GEOCOLOR-1250x750.jpg",
            "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/07/20181901637_GOES16-ABI-CONUS-07-1250x750.jpg",
            "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/09/20181901637_GOES16-ABI-CONUS-09-1250x750.jpg",
            "http://www.wpc.ncep.noaa.gov/medr/9khwbg_conus.gif",
            "http://www.wpc.ncep.noaa.gov/medr/9lhwbg_conus.gif",
            "http://www.wpc.ncep.noaa.gov/medr/9mhwbg_conus.gif",
            "http://www.wpc.ncep.noaa.gov/medr/9nhwbg_conus.gif",
            "https://www.spc.noaa.gov/products/outlook/day1otlk_prt.gif",
            "https://www.spc.noaa.gov/products/outlook/day1probotlk_torn.gif",
            "https://www.spc.noaa.gov/products/outlook/day1probotlk_wind.gif",
            "https://www.spc.noaa.gov/products/outlook/day1probotlk_hail.gif",
            "https://www.spc.noaa.gov/products/outlook/day2otlk_prt.gif",
            "https://www.spc.noaa.gov/products/outlook/day2probotlk_any.gif",
            "https://www.spc.noaa.gov/products/outlook/day3otlk_prt.gif",
            "https://www.spc.noaa.gov/products/outlook/day3prob.gif",
            "https://www.spc.noaa.gov/products/exper/day4-8/day4prob.gif",
            "https://www.spc.noaa.gov/products/exper/day4-8/day5prob.gif",
            "https://www.spc.noaa.gov/products/exper/day4-8/day6prob.gif",
            "https://www.spc.noaa.gov/products/exper/day4-8/day7prob.gif",
            "https://www.spc.noaa.gov/products/exper/day4-8/day8prob.gif"
        ]
        print("DOWNLOADING ... ...")
        for link in links:
            try:
                response = requests.get(link)
                imgFile = Image.open(BytesIO(response.content))
                img = ImageTk.PhotoImage(imgFile)
                self.images.append(img)
            except:
                print(link)

        textLinks = [
            'https://f1.weather.gov/product.php?site=NWS&issuedby=DY1&product=SWO',
            'https://f1.weather.gov/product.php?site=NWS&product=SWO&issuedby=DY2',
            'https://f1.weather.gov/product.php?site=NWS&product=SWO&issuedby=DY3',
            'https://f1.weather.gov/product.php?site=NWS&product=SWO&issuedby=D48',
            'https://f1.weather.gov/product.php?site=NWS&product=SWO&issuedby=MCD',
        ]

        for link in textLinks:
            page = requests.get(link).text
            bs = bshtml(page)
            self.text_prods.append(bs.pre.contents[0])

        print("READY!")


    def create_widgets(self):
        """
        Builds main program
        """
        self.winfo_toplevel().title("Climate Desk")
        self.categories = ttk.Notebook(self)
        # Create tabs
        nationalWx = ttk.Frame(self.categories)
        nationalClimate = ttk.Frame(self.categories)
        regionalClimate = ttk.Frame(self.categories)
        internationalClimate = ttk.Frame(self.categories)

        self.categories.add(nationalWx, text="National Weather")
        self.categories.add(nationalClimate, text="National Climate")
        self.categories.add(regionalClimate, text="Regional Climate")
        self.categories.add(internationalClimate, text="International")
        self.categories.pack()

        panel = tk.Label(nationalWx)

        natlMap1 = tk.Button(nationalWx, text="Forecast Day 1", command=lambda: self.showNewImage(panel, self.images[0]))
        natlMap2 = tk.Button(nationalWx, text="Forecast Day 2", command=lambda: self.showNewImage(panel, self.images[1]))
        natlMap3 = tk.Button(nationalWx, text="Forecast Day 3", command=lambda: self.showNewImage(panel, self.images[2]))
        natlForc = tk.Button(nationalWx, text="Day 3-7 Forecast", command=lambda: self.showMultiPane(panel, nationalWx))

        natlVis = tk.Button(nationalWx, text="Visible Satellite", command=lambda: self.showNewImage(panel, self.images[3]))
        natlIR = tk.Button(nationalWx, text="Infrared Satellite", command=lambda: self.showNewImage(panel, self.images[4]))
        natlWV = tk.Button(nationalWx, text="Water Vapor Satellite", command=lambda: self.showNewImage(panel, self.images[5]))
        
        natlSpc = tk.Button(nationalWx, text="SPC Outlooks", command=lambda: self.showSpcOutlook(panel, nationalWx))
        natlRad = tk.Button(nationalWx, text="Radar")

        natlMap1.grid(row=0, column=0)
        natlMap2.grid(row=1, column=0)
        natlMap3.grid(row=2, column=0)
        natlForc.grid(row=3, column=0)
        natlVis.grid(row=4, column=0)
        natlIR.grid(row=5, column=0)
        natlWV.grid(row=6, column=0)
        natlSpc.grid(row=7, column=0)
        natlRad.grid(row=8, column=0)

        self.showNewImage(panel, self.images[0])

        climateReport = tk.Button(nationalClimate, text="Climate Reports", command=callClimateReports)
        past = tk.Button(nationalClimate, text="Observations")
        outlook = tk.Button(nationalClimate, text="Outlook")
        enso = tk.Button(nationalClimate, text="ENSO")
        mjo = tk.Button(nationalClimate, text="MJO")
        telecon = tk.Button(nationalClimate, text="Teleconnections")
        blocks = tk.Button(nationalClimate, text="Blocking")
        tracks = tk.Button(nationalClimate, text="Storm Tracks")

        climateReport.grid(row=0, column=0)
        past.grid(row=1, column=0)
        outlook.grid(row=2, column=0)
        enso.grid(row=3, column=0)
        mjo.grid(row=4, column=0)
        telecon.grid(row=5, column=0)
        blocks.grid(row=6, column=0)
        tracks.grid(row=7, column=0)

        self.quit = tk.Button(self, text="Exit", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def showNewImage(self, panel, image, parent=False):
        """
        This will update/create an image panel that is always to the right
        of the main button group.
        """
        if parent is False:
            if self.multipane is not None:
                self.multipane.grid_forget()
        panel.configure(image=image)
        panel.image = image
        panel.grid(row=0, column=1, rowspan=20, columnspan=10)

    def showMultiPane(self, panel, container):
        panel.grid_forget()
        self.multipane = ttk.Notebook(container)

        d1 = ttk.Frame(self.multipane)
        d2 = ttk.Frame(self.multipane)
        d3 = ttk.Frame(self.multipane)

        self.multipane.add(d1, text='Day 1')
        self.multipane.add(d2, text='Day 2')
        self.multipane.add(d3, text='Day 3')
        self.multipane.grid(row=0, column=1, rowspan=20, columnspan=10)

        panel1 = tk.Label(d1)
        panel1.configure(image=self.images[6])
        panel1.image = self.images[6]
        panel1.pack(side="bottom")

        panel2 = tk.Label(d2)
        panel2.configure(image=self.images[7])
        panel2.image = self.images[7]
        panel2.pack(side="bottom")

        panel3 = tk.Label(d3)
        panel3.configure(image=self.images[8])
        panel3.image = self.images[8]
        panel3.pack(side="bottom")

    def showSpcOutlook(self, panel, container):
        panel.grid_forget()
        self.multipane = ttk.Notebook(container)

        d1 = ttk.Frame(self.multipane)
        d2 = ttk.Frame(self.multipane)
        d3 = ttk.Frame(self.multipane)
        d4 = ttk.Frame(self.multipane)
        d5 = ttk.Frame(self.multipane)
        d6 = ttk.Frame(self.multipane)
        d7 = ttk.Frame(self.multipane)
        d8 = ttk.Frame(self.multipane)

        self.multipane.add(d1, text='Day 1')
        self.multipane.add(d2, text='Day 2')
        self.multipane.add(d3, text='Day 3')
        self.multipane.add(d4, text='Day 4')
        self.multipane.add(d5, text='Day 5')
        self.multipane.add(d6, text='Day 6')
        self.multipane.add(d7, text='Day 7')
        self.multipane.add(d8, text='Day 8')
        self.multipane.grid(row=0, column=1, rowspan=20, columnspan=10)

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
        panel1.configure(image=self.images[10])
        panel1.image = self.images[10]
        panel1.pack(side="bottom")

        panel2 = tk.Label(d1t)
        panel2.configure(image=self.images[11])
        panel2.image = self.images[11]
        panel2.pack(side="bottom")

        panel3 = tk.Label(d1w)
        panel3.configure(image=self.images[12])
        panel3.image = self.images[12]
        panel3.pack(side="bottom")

        panel4 = tk.Label(d1h)
        panel4.configure(image=self.images[13])
        panel4.image = self.images[13]
        panel4.pack(side="bottom")

        # DAY TWO ---------------
        d2f = ttk.Notebook(d2)

        d2c = ttk.Frame(d2f)
        d2p = ttk.Frame(d2f)

        d2f.add(d2c, text='Categorical')
        d2f.add(d2p, text='Probabilistic')

        d2f.grid(row=0, column=1, rowspan=20, columnspan=10)

        panel5 = tk.Label(d2c)
        panel5.configure(image=self.images[14])
        panel5.image = self.images[14]
        panel5.pack(side="bottom")

        panel6 = tk.Label(d2p)
        panel6.configure(image=self.images[15])
        panel6.image = self.images[15]
        panel6.pack(side="bottom")

        # DAY THREE ---------------
        d3f = ttk.Notebook(d3)

        d3c = ttk.Frame(d3f)
        d3p = ttk.Frame(d3f)

        d3f.add(d3c, text='Categorical')
        d3f.add(d3p, text='Probabilistic')

        d3f.grid(row=0, column=1, rowspan=20, columnspan=10)

        panel5 = tk.Label(d3c)
        panel5.configure(image=self.images[16])
        panel5.image = self.images[16]
        panel5.pack(side="bottom")

        panel6 = tk.Label(d3p)
        panel6.configure(image=self.images[17])
        panel6.image = self.images[17]
        panel6.pack(side="bottom")

        # DAY 4-8

        panel7 = tk.Label(d4)
        panel7.configure(image=self.images[18])
        panel7.image = self.images[18]
        panel7.pack(side="bottom")

        panel8 = tk.Label(d5)
        panel8.configure(image=self.images[19])
        panel8.image = self.images[19]
        panel8.pack(side="bottom")

        panel9 = tk.Label(d6)
        panel9.configure(image=self.images[20])
        panel9.image = self.images[20]
        panel9.pack(side="bottom")

        panel10 = tk.Label(d7)
        panel10.configure(image=self.images[21])
        panel10.image = self.images[21]
        panel10.pack(side="bottom")

        panel11 = tk.Label(d8)
        panel11.configure(image=self.images[22])
        panel11.image = self.images[22]
        panel11.pack(side="bottom")

        self.textWindow()

    def textWindow(self):
        window = tk.Toplevel()
        window.wm_title("DISCUSSION TEXT")

        l = ScrolledText(window)
        l.insert(tk.INSERT, self.text_prods[0])
        l.grid(row=0, column=0)
        b = ttk.Button(window, text="Okay", command=window.destroy)
        b.grid(row=1, column=0)

root = tk.Tk()
app = Application(master=root)
app.mainloop()
