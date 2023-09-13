import tkinter as tk
from py import startup as startup
from py import window as window

# Create Matchup Array
matchupArray = startup.getMatchupsArray()

# Create All Champions Array
championArray = startup.getChampionsArray()

# Create ADC Array
adcArray = startup.getADCArray()

#Create Window
window = window.window(championArray, adcArray, matchupArray)
window.mainloop()