import requests
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter.scrolledtext import ScrolledText
from io import BytesIO
from bs4 import BeautifulSoup as bshtml

import spc
import cpc
import resources
import intl

headers = {
    'User-Agent': 'Climate Desk 0.1'
}


def loadingBox(root):
    """This creates the main loading dialog"""
    # get screen width and height
    ws = root.winfo_screenwidth()  # width of the screen
    hs = root.winfo_screenheight()  # height of the screen

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

    info4 = tk.Label(window)
    info4.configure(text="Climate Desk is a weather and climate data dashboard\
 that aggregates products across the public space.")
    info4.grid(row=3, column=0)

    info4 = tk.Label(window)
    info4.configure(text="Report bugs on GitHub!")
    info4.grid(row=5, column=0)

    loading = ttk.Progressbar(window)
    loading.grid(row=8, column=0)
    loading.start()
    loadingState = tk.Label(window)
    loadingState.configure(text="LOADING")
    loadingState.grid(row=9, column=0, padx=3, pady=5)
    # b = ttk.Button(window, text="Close", command=window.destroy)
    # b.grid(row=7, column=0)

    window.lift()
    window.update()

    return window, loading, loadingState


def getImageList(links, imageList):
    """
    This downloads images from a given link list and appends them to an
    image data list.
    """
    for link in links:
        try:
            response = requests.get(link, headers=headers)
            response.raise_for_status()
            # imgFile = Image.open(BytesIO(response.content))
            # img = ImageTk.PhotoImage(imgFile)
            imageList.append(response.content)
        except requests.exceptions.RequestException:
            print(e, link)


def getHprccList(links, imageList):
    """
    This handles downloading the multiple products and timescales from
    HPRCC links and saves them to an image data list.
    """
    for timescale in links:
        timeList = []
        for link in timescale:
            try:
                response = requests.get(link, headers=headers)
                # imgFile = Image.open(BytesIO(response.content))
                # img = ImageTk.PhotoImage(imgFile)
                timeList.append(response.content)
            except:
                print(link)
        imageList.append(timeList)


def getIntlImageList(links, imageList):
    """
    This handles downloading the multiple products and timescales from
    the CPC international map links and saves them to an image data list
    """
    for region in links:
        regionList = []
        for time in region:
            timeList = []
            for link in time:
                try:
                    response = requests.get(link, headers=headers)
                    timeList.append(response.content)
                except:
                    print(link)
            regionList.append(timeList)
        imageList.append(regionList)


class Application(tk.Frame):
    """
    This is the main application class. Primarily coordinating functions
    surrounding the main application window.
    """

    def __init__(self, master=None):
        """Initializes the application"""
        super().__init__(master)
        self.root = master
        self.root.withdraw()

        self.text_prods = []
        self.multipane = None

        self.pack()

        splash = self.downloadImages()

        self.root.deiconify()
        self.root.state('normal')
        self.create_widgets(splash)

    def downloadImages(self):
        """
        Downloads all images. The images need to be referenced to the
        application to hide from the garbage collecter, so we do it all here.
        """
        about, loading, loadText = loadingBox(self.root)

        self.wpc = []
        self.sat = []
        self.rad = []
        self.spc = []
        self.cpcShortRange = []
        self.droughtOutlook = []
        self.cpcLongRange = []
        self.observations = []
        self.ensoImg = []
        self.mjoImg = []
        self.teleconImg = []
        self.intl = []
        self.blockingImg = []

        nationalObs = resources.getHprccNatl()
        globalObs = resources.getIntlMaps()

        loadText.configure(text="Getting WPC forecast graphics...")
        about.update()
        getImageList(resources.wpc, self.wpc)

        loading.step(12)
        loadText.configure(text="Getting satellite imagery...")
        about.update()
        getImageList(resources.sat, self.sat)

        loading.step(12)
        loadText.configure(text="Getting SPC outlook graphics...")
        about.update()
        getImageList(resources.spc, self.spc)

        loading.step(12)
        loadText.configure(text="Getting latest radar loop...")
        about.update()
        getImageList(resources.rad, self.rad)

        loading.step(12)
        loadText.configure(text="Getting CPC short range outlook graphics...")
        about.update()
        getImageList(resources.cpcShortRange, self.cpcShortRange)

        loading.step(12)
        loadText.configure(text="Getting CPC long range outlook graphics...")
        about.update()
        getImageList(resources.cpcLongRange, self.cpcLongRange)

        loading.step(12)
        loadText.configure(text="Getting drought outlook graphics...")
        about.update()
        getImageList(resources.droughtOutlook, self.droughtOutlook)

        loading.step(12)
        loadText.configure(text="Getting HPRCC observation maps...")
        about.update()
        getHprccList(nationalObs, self.observations)

        loading.step(12)
        loadText.configure(text="Getting CPC ENSO Information...")
        about.update()
        getImageList(resources.enso, self.ensoImg)

        loading.step(12)
        loadText.configure(text="Getting CPC MJO Information...")
        about.update()
        getImageList(resources.mjo, self.mjoImg)

        loading.step(12)
        loadText.configure(text="Getting CPC Blocking Information...")
        about.update()
        getImageList(resources.blocking, self.blockingImg)

        loading.step(12)
        loadText.configure(text="Getting CPC Teleconnection Information...")
        about.update()
        getImageList(resources.telecon, self.teleconImg)

        loading.step(12)
        loadText.configure(text="Getting CPC Global Climate Maps... (This will\
 take a minute)")
        about.update()
        getIntlImageList(globalObs, self.intl)

        loading.step(12)
        loadText.configure(text="Getting text discussions...")
        about.update()

        for link in resources.textLinks:
            page = requests.get(link).text
            bs = bshtml(page, "html.parser")
            self.text_prods.append(bs.pre.contents)

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
        self.categories = ttk.Notebook(self)
        # Create tabs
        nationalWx = ttk.Frame(self.categories)
        nationalClimate = ttk.Frame(self.categories)
        # regionalClimate = ttk.Frame(self.categories)
        internationalClimate = ttk.Frame(self.categories)

        self.categories.add(nationalWx, text="National Weather")
        self.categories.add(nationalClimate, text="National Climate")
        # self.categories.add(regionalClimate, text="Regional Climate")
        self.categories.add(internationalClimate, text="International")
        self.categories.pack()

        # National Weather Panel
        self.panel = tk.Label(nationalWx)

        natlMap1 = tk.Button(nationalWx, text="Forecast Day 1",
                             command=lambda: self.showNewWxImage(nationalWx,
                                                                 self.wpc[0]))
        natlMap2 = tk.Button(nationalWx, text="Forecast Day 2",
                             command=lambda: self.showNewWxImage(nationalWx,
                                                                 self.wpc[1]))
        natlMap3 = tk.Button(nationalWx, text="Forecast Day 3",
                             command=lambda: self.showNewWxImage(nationalWx,
                                                                 self.wpc[2]))
        natlForc = tk.Button(nationalWx, text="Day 3-7 Forecast",
                             command=lambda: self.createWpc(nationalWx))

        natlVis = tk.Button(nationalWx, text="Visible Satellite",
                            command=lambda: self.showNewWxImage(nationalWx,
                                                                self.sat[0]))
        natlIR = tk.Button(nationalWx, text="Infrared Satellite",
                           command=lambda: self.showNewWxImage(nationalWx,
                                                               self.sat[1]))
        natlWV = tk.Button(nationalWx, text="Water Vapor Satellite",
                           command=lambda: self.showNewWxImage(nationalWx,
                                                               self.sat[2]))

        natlSpc = tk.Button(nationalWx, text="SPC Outlooks",
                            command=lambda: self.createSpc(nationalWx))
        natlRad = tk.Button(nationalWx, text="Radar",
                            command=lambda: self.showNewWxImage(nationalWx,
                                                                self.rad[0]))

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
        self.climPanel = tk.Label(nationalClimate)  # Make product panel

        climateReport = tk.Button(nationalClimate,
                                  text="Climate Reports (link)",
                                  command=cpc.callClimateReports)

        past = tk.Button(nationalClimate, text="Observations",
                         command=lambda:
                         self.createObservations(nationalClimate))

        outlook = tk.Button(nationalClimate, text="Short Range Outlook",
                            command=lambda:
                            self.createCpcOutlook(nationalClimate))

        lrOutlook = tk.Button(nationalClimate, text="Long Range Outlook",
                              command=lambda:
                              self.createCpcLrOutlook(nationalClimate))

        cpcDiscuss = tk.Button(nationalClimate, text="CPC Discussions",
                               command=lambda:
                               cpc.showDiscussions(self.text_prods))

        enso = tk.Button(nationalClimate, text="ENSO",
                         command=lambda: self.createEnso(nationalClimate))

        mjo = tk.Button(nationalClimate, text="MJO",
                        command=lambda: self.createMjo(nationalClimate))

        telecon = tk.Button(nationalClimate, text="Teleconnections",
                            command=lambda:
                            self.createTelecon(nationalClimate))

        blocks = tk.Button(nationalClimate, text="Blocking",
                           command=lambda:
                           self.createBlocking(nationalClimate))

        climateReport.grid(row=0, column=0, sticky='W')
        past.grid(row=1, column=0, sticky='W')
        outlook.grid(row=2, column=0, sticky='W')
        lrOutlook.grid(row=3, column=0, sticky='W')
        cpcDiscuss.grid(row=4, column=0, sticky='W')
        enso.grid(row=5, column=0, sticky='W')
        mjo.grid(row=6, column=0, sticky='W')
        telecon.grid(row=7, column=0, sticky='W')
        blocks.grid(row=8, column=0, sticky='W')
        nationalClimate.update_idletasks()

        self.showNewClimImage(nationalClimate, self.cpcShortRange[0])

        # International Panel
        self.intlPanel = tk.Label(internationalClimate)

        africa = tk.Button(internationalClimate, text="Africa",
                           command=lambda:
                           self.createAfrica(internationalClimate))

        asia = tk.Button(internationalClimate, text="Asia",
                         command=lambda: self.createAsia(internationalClimate))

        australia = tk.Button(internationalClimate, text="Australia",
                              command=lambda:
                              self.createAustralia(internationalClimate))

        canada = tk.Button(internationalClimate, text="Canada",
                           command=lambda:
                           self.createCanada(internationalClimate))

        europe = tk.Button(internationalClimate, text="Europe",
                           command=lambda:
                           self.createEurope(internationalClimate))

        caucas = tk.Button(internationalClimate, text="East Europe",
                           command=lambda:
                           self.createCaucas(internationalClimate))

        mexico = tk.Button(internationalClimate, text="Mexico",
                           command=lambda:
                           self.createMexico(internationalClimate))

        mideast = tk.Button(internationalClimate, text="Middle East",
                            command=lambda:
                            self.createMideast(internationalClimate))

        southAmerica = tk.Button(internationalClimate, text="South America",
                                 command=lambda:
                                 self.createSouthAmerica(internationalClimate))

        africa.grid(row=0, column=0, sticky='W')
        asia.grid(row=1, column=0, sticky='W')
        australia.grid(row=2, column=0, sticky='W')
        canada.grid(row=3, column=0, sticky='W')
        europe.grid(row=4, column=0, sticky='W')
        caucas.grid(row=5, column=0, sticky='W')
        mexico.grid(row=6, column=0, sticky='W')
        mideast.grid(row=7, column=0, sticky='W')
        southAmerica.grid(row=8, column=0, sticky='W')
        internationalClimate.update_idletasks()

        self.quit = tk.Button(self, text="Exit", fg="red",
                              command=root.destroy)
        self.quit.pack(side="bottom")

        about.lift()

    def showNewWxImage(self, container, image):
        """Generic function to show an image in the weather pane"""
        self.panel.destroy()
        self.panel = cpc.createImageFrame(container, image, noShow=True)
        self.panel.grid(row=0, column=1, rowspan=20, columnspan=10)

    def createWpc(self, container):
        """Helper function to show the WPC forecast images"""
        self.panel.destroy()
        self.panel = spc.showForecast(container, self.wpc)

    def createSpc(self, container):
        """Helper function to show the SPC outlook images"""
        self.panel.destroy()
        self.panel = spc.showSpcOutlook(container, self.spc, self.text_prods)

    def createCpcOutlook(self, container):
        """Helper function to show the CPC outlook images"""
        self.climPanel.destroy()
        self.climPanel = cpc.cpcOutlook(container, self.cpcShortRange,
                                        self.droughtOutlook)

    def createCpcLrOutlook(self, container):
        """Helper function to show the CPC long range outlook images"""
        self.climPanel.destroy()
        self.climPanel = cpc.cpcLrOutlook(container, self.cpcLongRange)

    def createObservations(self, container):
        """Helper function to show the HPRCC observation images"""
        self.climPanel.destroy()
        self.climPanel = cpc.hprccObs(container, self.observations)

    def createEnso(self, container):
        """Helper function to show the CPC ENSO images"""
        self.climPanel.destroy()
        self.climPanel = cpc.enso(container, self.ensoImg)

    def createTelecon(self, container):
        """Helper function to show the CPC teleconnection images"""
        self.climPanel.destroy()
        self.climPanel = cpc.telecon(container, self.teleconImg)

    def createMjo(self, container):
        """Helper function to show the CPC MJO indices"""
        self.climPanel.destroy()
        self.climPanel = cpc.mjo(container, self.mjoImg)

    def createBlocking(self, container):
        self.climPanel.destroy()
        self.climPanel = cpc.blocking(container, self.blockingImg)

    def createAfrica(self, container):
        """Helper function to show the Africa products"""
        self.intlPanel.destroy()
        self.intlPanel = intl.africa(container, self.intl)

    def createAsia(self, container):
        """Helper function to show the Asia products"""
        self.intlPanel.destroy()
        self.intlPanel = intl.asia(container, self.intl)

    def createAustralia(self, container):
        """Helper function to show the Australia products"""
        self.intlPanel.destroy()
        self.intlPanel = intl.australia(container, self.intl)

    def createCanada(self, container):
        """Helper function to show the Canada products"""
        self.intlPanel.destroy()
        self.intlPanel = intl.canada(container, self.intl)

    def createEurope(self, container):
        """Helper function to show the Europe products"""
        self.intlPanel.destroy()
        self.intlPanel = intl.europe(container, self.intl)

    def createCaucas(self, container):
        """Helper function to show the East Europe products"""
        self.intlPanel.destroy()
        self.intlPanel = intl.caucas(container, self.intl)

    def createMexico(self, container):
        """Helper function to show the Mexico products"""
        self.intlPanel.destroy()
        self.intlPanel = intl.mexico(container, self.intl)

    def createMideast(self, container):
        """Helper function to show the Middle East products"""
        self.intlPanel.destroy()
        self.intlPanel = intl.mideast(container, self.intl)

    def createSouthAmerica(self, container):
        """Helper function to show the South American products"""
        self.intlPanel.destroy()
        self.intlPanel = intl.southAmerica(container, self.intl)

    def showNewClimImage(self, container, image):
        """
        This will update/create an image panel that is always to the right
        of the main button group.
        """

        self.climPanel.destroy()
        self.climPanel = cpc.createImageFrame(container, image, noShow=True)
        self.climPanel.grid(row=0, column=1, rowspan=20, columnspan=10)


""" Start Application """
root = tk.Tk()

# root.attributes('-fullscreen', True) # Very fullscreen
app = Application(master=root)
app.mainloop()
