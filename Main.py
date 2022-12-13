from cgitb import text
from gettext import textdomain
import tkinter as tk


window = tk.Tk()

# window widgets
# 5 columns, 2 rows

frameUpper = tk.Frame(window, borderwidth=5, relief="ridge")
frameUpper.grid(column=0, row=0, columnspan=4)

frameDetail = tk.Frame(window)
frameDetail.grid(column=0, row=1)

frameInactive = tk.Frame(window)
frameInactive.grid(column=1, row=1)

frameActive = tk.Frame(window)
frameActive.grid(column=2, row=1)

frameResults = tk.Frame(window)
frameResults.grid(column=3, row=1)

frameButtons = tk.Frame(window)
frameButtons.grid(column=4, row=1)


# frameUpper widgets
settingsButton = tk.Button(frameUpper, width=15, height=1, text="Settings")
settingsButton.grid(column=0, row=0)

gameFolderButton = tk.Button(frameUpper, width=15, height=1, text="Game Folder")
gameFolderButton.grid(column=0, row=1)
gameFolderEntry = tk.Entry(frameUpper, width=200)
gameFolderEntry.grid(column=1, row=1)

steamModsButton = tk.Button(frameUpper, width=15, height=1, text="Steam Mods")
steamModsButton.grid(column=0, row=2)
steamModsEntry = tk.Entry(frameUpper, width=200)
steamModsEntry.grid(column=1, row=2)



# frameDetail widgets

imageFrame = tk.Frame(frameDetail)
imageFrame.grid(column=0, row=0)

textDetailsFrame = tk.Frame(frameDetail)
textDetailsFrame.grid(column=0, row=1)

textDescriptionFrame = tk.Frame(frameDetail)
textDescriptionFrame.grid(column=0, row=2)
descriptionText = tk.Text(textDescriptionFrame)




# frameInactive widgets
labelInactive = tk.Label(frameInactive, text="Inactive")
labelInactive.grid(column=0, row=0)

allInactiveModsFrame = tk.Frame(frameInactive)
allInactiveModsFrame.grid(column=0, row=1)



# frameInactive widgets
labelActive = tk.Label(frameActive, text="Active")
labelActive.grid(column=0, row=0)

allActiveModsFrame = tk.Frame(frameActive)
allActiveModsFrame.grid(column=0, row=1)





window.grid_columnconfigure(0, weight=4)
window.grid_columnconfigure(1,weight=1)
window.grid_columnconfigure(2,weight=1)
window.grid_columnconfigure(3,weight=1)
window.grid_columnconfigure(4,weight=1)

window.rowconfigure(0, weight=1)
window.rowconfigure(1,weight=10)

tk.mainloop()