import requests
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.scrolledtext import ScrolledText
from io import BytesIO
from bs4 import BeautifulSoup as bshtml

import spc as spc
import cpc as cpc


def loadingBox(root):
    # get screen width and height
    ws = root.winfo_screenwidth() # width of the screen
    hs = root.winfo_screenheight() # height of the screen

    # calculate x and y coordinates for the Tk root window
    w = 600
    h = 200
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)

    window = tk.Toplevel()
    window.wm_title("About Climate Desk")
    # set the dimensions of the screen 
    # and where it is placed
    window.geometry('%dx%d+%d+%d' % (w, h, x, y))

    info1 = tk.Label(window)
    info1.configure(text="Climate Desk", font='Helvetica 18 bold')
    info1.grid(row=1, column=0, padx=5, pady=5)

    info2 = tk.Label(window)
    info2.configure(text="(c)2018 Warren Pettee")
    info2.grid(row=2, column=0)

    info4 = tk.Label(window)
    info4.configure(text="Climate Desk is a weather and climate data dashboard that aggregates products from across the public space.")
    info4.grid(row=3, column=0)

    info4 = tk.Label(window)
    info4.configure(text="Report bugs on GitHub!")
    info4.grid(row=5, column=0)

    loading = ttk.Progressbar(window)
    loading.grid(row=8, column=0)
    loading.start()
    loadingState = tk.Label(window)
    loadingState.configure(text="LOADING")
    loadingState.grid(row=9, column=0,padx=3, pady=5)
    #b = ttk.Button(window, text="Close", command=window.destroy)
    #b.grid(row=7, column=0)

    window.lift()
    window.update()


    return window, loading, loadingState


def getImageList(links, imageList):
    headers = {
        'User-Agent': 'Climate Desk 0.1'
    }

    for link in links:
        try:
            response = requests.get(link, headers=headers)
            #imgFile = Image.open(BytesIO(response.content))
            #img = ImageTk.PhotoImage(imgFile)
            imageList.append(response.content)
        except:
            print(link)


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.root = master
        self.root.withdraw()

        self.text_prods = []
        self.multipane = None

        self.pack()

        splash = self.downloadImages()

        self.root.deiconify()
        self.root.state('zoomed')
        self.create_widgets(splash)

    def downloadImages(self):
        """
        Downloads all images. The images need to be referenced to the
        application to hide from the garbage collecter, so we do it all here.
        """
        about, loading, loadText = loadingBox(self.root)

        self.wpc = []
        wpc = [
            "http://www.wpc.ncep.noaa.gov/noaa/noaad1.gif",
            "http://www.wpc.ncep.noaa.gov/noaa/noaad2.gif",
            "http://www.wpc.ncep.noaa.gov/noaa/noaad3.gif",
            "http://www.wpc.ncep.noaa.gov/medr/9khwbg_conus.gif",
            "http://www.wpc.ncep.noaa.gov/medr/9lhwbg_conus.gif",
            "http://www.wpc.ncep.noaa.gov/medr/9mhwbg_conus.gif",
            "http://www.wpc.ncep.noaa.gov/medr/9nhwbg_conus.gif"
        ]

        self.sat = []
        sat = [
            "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/GEOCOLOR/20181901632_GOES16-ABI-CONUS-GEOCOLOR-1250x750.jpg",
            "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/07/20181901637_GOES16-ABI-CONUS-07-1250x750.jpg",
            "https://cdn.star.nesdis.noaa.gov/GOES16/ABI/CONUS/09/20181901637_GOES16-ABI-CONUS-09-1250x750.jpg"
        ]

        self.rad = []
        rad = [
            "https://radar.weather.gov/ridge/Conus/Loop/NatLoop.gif"
        ]

        self.spc = []
        spc = [
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

        self.cpcShortRange = []
        cpcShortRange = [
            "http://www.cpc.ncep.noaa.gov/products/predictions/610day/610temp.new.gif",
            "http://www.cpc.ncep.noaa.gov/products/predictions/610day/610prcp.new.gif",
            "http://www.cpc.ncep.noaa.gov/products/predictions/814day/814temp.new.gif",
            "http://www.cpc.ncep.noaa.gov/products/predictions/814day/814prcp.new.gif",
            "http://www.cpc.ncep.noaa.gov/products/predictions/30day/off15_temp.gif",
            "http://www.cpc.ncep.noaa.gov/products/predictions/30day/off15_prcp.gif"
        ]

        self.droughtOutlook = []
        droughtOutlook = [
            "http://www.cpc.ncep.noaa.gov/products/expert_assessment/mdohomeweb.png",
            "http://www.cpc.ncep.noaa.gov/products/expert_assessment/sdohomeweb.png"
        ]

        self.cpcLongRange = []
        cpcLongRange = [
            "http://www.cpc.ncep.noaa.gov/products/predictions/long_range/lead01/off01_temp.gif",
            "http://www.cpc.ncep.noaa.gov/products/predictions/long_range/lead01/off01_prcp.gif",
            "http://www.cpc.ncep.noaa.gov/products/predictions/long_range/lead02/off02_temp.gif",
            "http://www.cpc.ncep.noaa.gov/products/predictions/long_range/lead02/off02_prcp.gif",
            "http://www.cpc.ncep.noaa.gov/products/predictions/long_range/lead03/off03_temp.gif",
            "http://www.cpc.ncep.noaa.gov/products/predictions/long_range/lead03/off03_prcp.gif",
            "http://www.cpc.ncep.noaa.gov/products/predictions/long_range/lead04/off04_temp.gif",
            "http://www.cpc.ncep.noaa.gov/products/predictions/long_range/lead04/off04_prcp.gif",
            "http://www.cpc.ncep.noaa.gov/products/predictions/long_range/lead05/off05_temp.gif",
            "http://www.cpc.ncep.noaa.gov/products/predictions/long_range/lead05/off05_prcp.gif",
            "http://www.cpc.ncep.noaa.gov/products/predictions/long_range/lead06/off06_temp.gif",
            "http://www.cpc.ncep.noaa.gov/products/predictions/long_range/lead06/off06_prcp.gif",
            "http://www.cpc.ncep.noaa.gov/products/predictions/long_range/lead07/off07_temp.gif",
            "http://www.cpc.ncep.noaa.gov/products/predictions/long_range/lead07/off07_prcp.gif",
            "http://www.cpc.ncep.noaa.gov/products/predictions/long_range/lead08/off08_temp.gif",
            "http://www.cpc.ncep.noaa.gov/products/predictions/long_range/lead08/off08_prcp.gif",
            "http://www.cpc.ncep.noaa.gov/products/predictions/long_range/lead09/off09_temp.gif",
            "http://www.cpc.ncep.noaa.gov/products/predictions/long_range/lead09/off09_prcp.gif",
            "http://www.cpc.ncep.noaa.gov/products/predictions/long_range/lead10/off10_temp.gif",
            "http://www.cpc.ncep.noaa.gov/products/predictions/long_range/lead10/off10_prcp.gif",
            "http://www.cpc.ncep.noaa.gov/products/predictions/long_range/lead11/off11_temp.gif",
            "http://www.cpc.ncep.noaa.gov/products/predictions/long_range/lead11/off11_prcp.gif",
            "http://www.cpc.ncep.noaa.gov/products/predictions/long_range/lead12/off12_temp.gif",
            "http://www.cpc.ncep.noaa.gov/products/predictions/long_range/lead12/off12_prcp.gif",
            "http://www.cpc.ncep.noaa.gov/products/predictions/long_range/lead13/off13_temp.gif",
            "http://www.cpc.ncep.noaa.gov/products/predictions/long_range/lead13/off13_prcp.gif"
        ]

        self.observations = []
        observations = [
            "https://hprcc.unl.edu/products/maps/acis/7dPDataUS.png",
            "https://hprcc.unl.edu/products/maps/acis/7dPDeptUS.png",
            "https://hprcc.unl.edu/products/maps/acis/7dPNormUS.png",
            "https://hprcc.unl.edu/products/maps/acis/7dTDataUS.png",
            "https://hprcc.unl.edu/products/maps/acis/7dTDeptUS.png",
            "https://hprcc.unl.edu/products/maps/acis/7dTMAXDataUS.png",
            "https://hprcc.unl.edu/products/maps/acis/7dTMINDataUS.png",
            ""
        ]

        loadText.configure(text="Getting WPC forecast graphics...")
        about.update()
        getImageList(wpc, self.wpc)

        loading.step(12)
        loadText.configure(text="Getting satellite imagery...")
        about.update()
        getImageList(sat, self.sat)

        loading.step(12)
        loadText.configure(text="Getting SPC outlook graphics...")
        about.update()
        getImageList(spc, self.spc)

        loading.step(12)
        loadText.configure(text="Getting latest radar loop...")
        about.update()
        getImageList(rad, self.rad)

        loading.step(12)
        loadText.configure(text="Getting CPC short range outlook graphics...")
        about.update()
        getImageList(cpcShortRange, self.cpcShortRange)

        loading.step(12)
        loadText.configure(text="Getting CPC long range outlook graphics...")
        about.update()
        getImageList(cpcLongRange, self.cpcLongRange)

        loading.step(12)
        loadText.configure(text="Getting drought outlook graphics...")
        about.update()
        getImageList(droughtOutlook, self.droughtOutlook)

        loading.step(12)
        loadText.configure(text="Getting HPRCC observation maps...")
        about.update()
        getImageList(observations, self.observations)
        
        textLinks = [
            'https://f1.weather.gov/product.php?site=NWS&issuedby=DY1&product=SWO',
            'https://f1.weather.gov/product.php?site=NWS&product=SWO&issuedby=DY2',
            'https://f1.weather.gov/product.php?site=NWS&product=SWO&issuedby=DY3',
            'https://f1.weather.gov/product.php?site=NWS&product=SWO&issuedby=D48',
            'https://f1.weather.gov/product.php?site=NWS&product=SWO&issuedby=MCD',
            'http://www.cpc.ncep.noaa.gov/products/predictions/610day/fxus06.html',
            'http://www.cpc.ncep.noaa.gov/products/predictions/long_range/fxus07.html',
            'http://www.cpc.ncep.noaa.gov/products/predictions/long_range/fxus05.html'
        ]
        
        loading.step(12)
        loadText.configure(text="Getting text discussions...")
        about.update()

        for link in textLinks:
            page = requests.get(link).text
            bs = bshtml(page)
            self.text_prods.append(bs.pre.contents[0])

        loading.stop()

        loadText.configure(text="Ready to go!")
        b = ttk.Button(about, text="Close", command=about.destroy)
        b.grid(row=12, column=0)
        about.update()

        return about

    def create_widgets(self, about):
        """
        Builds main program
        """
        self.winfo_toplevel().title("Climate Desk")
        self.categories = ttk.Notebook(self, width=self.root.winfo_width(), height=(self.root.winfo_height() - 50))
        # Create tabs
        nationalWx = ttk.Frame(self.categories, width=(self.categories.winfo_width() - 10), height=(self.categories.winfo_height() - 10))
        nationalClimate = ttk.Frame(self.categories, width=(self.categories.winfo_width() - 10), height=(self.categories.winfo_height() - 10))
        regionalClimate = ttk.Frame(self.categories, width=(self.categories.winfo_width() - 10), height=(self.categories.winfo_height() - 10))
        internationalClimate = ttk.Frame(self.categories, width=(self.categories.winfo_width() - 10), height=(self.categories.winfo_height() - 10))

        self.categories.add(nationalWx, text="National Weather")
        self.categories.add(nationalClimate, text="National Climate")
        self.categories.add(regionalClimate, text="Regional Climate")
        self.categories.add(internationalClimate, text="International")
        self.categories.pack()

        # National Weather Panel
        self.panel = tk.Label(nationalWx)

        natlMap1 = tk.Button(nationalWx, text="Forecast Day 1", command=lambda: self.showNewWxImage(nationalWx, self.wpc[0]))
        natlMap2 = tk.Button(nationalWx, text="Forecast Day 2", command=lambda: self.showNewWxImage(nationalWx, self.wpc[1]))
        natlMap3 = tk.Button(nationalWx, text="Forecast Day 3", command=lambda: self.showNewWxImage(nationalWx, self.wpc[2]))
        natlForc = tk.Button(nationalWx, text="Day 3-7 Forecast", command=lambda: self.createWpc(nationalWx))

        natlVis = tk.Button(nationalWx, text="Visible Satellite", command=lambda: self.showNewWxImage(nationalWx, self.sat[0]))
        natlIR = tk.Button(nationalWx, text="Infrared Satellite", command=lambda: self.showNewWxImage(nationalWx, self.sat[1]))
        natlWV = tk.Button(nationalWx, text="Water Vapor Satellite", command=lambda: self.showNewWxImage(nationalWx, self.sat[2]))

        natlSpc = tk.Button(nationalWx, text="SPC Outlooks", command=lambda: self.createSpc(nationalWx))
        natlRad = tk.Button(nationalWx, text="Radar", command=lambda: self.showNewWxImage(nationalWx, self.rad[0]))

        natlMap1.grid(row=0, column=0, sticky='W')
        natlMap2.grid(row=1, column=0, sticky='W')
        natlMap3.grid(row=2, column=0, sticky='W')
        natlForc.grid(row=3, column=0, sticky='W')
        natlVis.grid(row=4, column=0, sticky='W')
        natlIR.grid(row=5, column=0, sticky='W')
        natlWV.grid(row=6, column=0, sticky='W')
        natlSpc.grid(row=7, column=0, sticky='W')
        natlRad.grid(row=8, column=0, sticky='W')

        self.showNewWxImage(nationalWx, self.wpc[0])

        # National Climate Panel
        self.climPanel = tk.Label(nationalClimate) # Make product panel

        climateReport = tk.Button(nationalClimate, text="Climate Reports (link)", command=cpc.callClimateReports)
        past = tk.Button(nationalClimate, text="Observations")
        outlook = tk.Button(nationalClimate, text="Short Range Outlook", command=lambda: self.createCpcOutlook(nationalClimate))
        lrOutlook = tk.Button(nationalClimate, text="Long Range Outlook", command=lambda: self.createCpcLrOutlook(nationalClimate))
        enso = tk.Button(nationalClimate, text="ENSO")
        mjo = tk.Button(nationalClimate, text="MJO")
        telecon = tk.Button(nationalClimate, text="Teleconnections")
        blocks = tk.Button(nationalClimate, text="Blocking")
        tracks = tk.Button(nationalClimate, text="Storm Tracks")

        climateReport.grid(row=0, column=0, sticky='W')
        past.grid(row=1, column=0, sticky='W')
        outlook.grid(row=2, column=0, sticky='W')
        lrOutlook.grid(row=3, column=0, sticky='W')
        enso.grid(row=4, column=0, sticky='W')
        mjo.grid(row=5, column=0, sticky='W')
        telecon.grid(row=6, column=0, sticky='W')
        blocks.grid(row=7, column=0, sticky='W')
        tracks.grid(row=8, column=0, sticky='W')
        nationalClimate.update_idletasks()

        self.showNewClimImage(nationalClimate, self.cpcShortRange[0])

        self.quit = tk.Button(self, text="Exit", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

        about.lift()

    def showNewWxImage(self, container, image):
        self.panel.destroy()
        self.panel = cpc.createImageFrame(container, image, noShow=True)
        self.panel.grid(row=0, column=1, rowspan=20, columnspan=10)

    def createWpc(self, container):
        self.panel.destroy()
        self.panel = spc.showForecast(container, self.wpc)

    def createSpc(self, container):
        self.panel.destroy()
        self.panel = spc.showSpcOutlook(container, self.spc, self.text_prods)

    def createCpcOutlook(self, container):
        self.climPanel.destroy()
        self.climPanel = cpc.cpcOutlook(container, self.cpcShortRange, self.droughtOutlook)

    def createCpcLrOutlook(self, container):
        self.climPanel.destroy()
        self.climPanel = cpc.cpcLrOutlook(container, self.cpcLongRange)

    def showNewClimImage(self, container, image):
        """
        This will update/create an image panel that is always to the right
        of the main button group.
        """

        self.climPanel.destroy()
        self.climPanel = cpc.createImageFrame(container, image, noShow=True)
        self.climPanel.grid(row=0, column=1, rowspan=20, columnspan=10)

root = tk.Tk()

# root.attributes('-fullscreen', True) # Very fullscreen
app = Application(master=root)
app.mainloop()
