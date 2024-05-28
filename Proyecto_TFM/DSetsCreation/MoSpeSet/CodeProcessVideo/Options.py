import tkinter as tk
from tkinter import *
from tkinter import filedialog, ttk

class OptionsHough:
    def __init__(self):
        self.minRadius = "25"
        self.maxRadius = "45"
        self.param1 = "80"
        self.param2 = "35"
        self.mediumCellSize = "180"
        self.scale = "0.59"
        self.cameraHeight = "10"
        self.diluent = "0"        

    def return_options(self):
        return(int(self.minRadius),
                                       int(self.maxRadius),
                                       int(self.param1),
                                       int(self.param2),
                                       int(self.mediumCellSize),
                                       float(self.scale),
                                       int(self.cameraHeight),
                                       int(self.diluent)
                                       )