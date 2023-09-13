import tkinter as tk
import tkinter.ttk as ttk
from py import startup as startup
class window:

    def sort_names_by_current(self, data):
        sorted_names = sorted(data.keys(), key=lambda name: data[name]['current'], reverse=True)
        sorted_current_values = [data[name]['current'] for name in sorted_names]
        return [sorted_names, sorted_current_values]
    def goButtonClicked(self):
        self.matchupArray = startup.getMatchupsArray()
        #Get Champion Names
        selectedChampions = []
        selectedAllies = []
        selectedChampions.append(self.enemy1Picklist.get())
        selectedChampions.append(self.enemy2Picklist.get())
        selectedChampions.append(self.enemy3Picklist.get())
        selectedChampions.append(self.enemy4Picklist.get())
        selectedChampions.append(self.enemy5Picklist.get())
        selectedAllies.append(self.ally1Picklist.get())
        selectedAllies.append(self.ally2Picklist.get())
        selectedAllies.append(self.ally3Picklist.get())
        selectedAllies.append(self.ally4Picklist.get())

        adcArray = []
        with open('data/champions.txt') as f:
            champions = f.readlines()
        for champion in champions:
            adcArray.append(champion.strip())

        for i in range(0, len(self.matchupArray)):
            index = adcArray[i]
            for status in self.matchupArray[index]:
                if status == 'name' or status == 'current':
                    continue
                if status == '-':
                    for champion in selectedChampions:
                        if champion in self.matchupArray[index][status]:
                            self.matchupArray[index]['current'] -= 1
                elif status == '+':
                    for champion in selectedAllies:
                        if champion in self.matchupArray[index][status]:
                            self.matchupArray[index]['current'] += 1
        sorted_adcArray = self.sort_names_by_current(self.matchupArray)
        self.result1Label.config(text=sorted_adcArray[0][0].capitalize() + ':')
        self.result2label.config(text=sorted_adcArray[0][1].capitalize() + ':')
        self.result3label.config(text=sorted_adcArray[0][2].capitalize() + ':')
        self.result4label.config(text=sorted_adcArray[0][3].capitalize() + ':')
        self.result1ValueLabel.config(text=sorted_adcArray[1][0])
        self.result2ValueLabel.config(text=sorted_adcArray[1][1])
        self.result3ValueLabel.config(text=sorted_adcArray[1][2])
        self.result4ValueLabel.config(text=sorted_adcArray[1][3])
        if self.youPicklist.get() != '':
            yourPickScore = 0
            for status in self.matchupArray[self.youPicklist.get().lower()]:
                if status == 'name' or status == 'current':
                    continue
                if status == '-':
                    for champion in selectedChampions:
                        if champion in self.matchupArray[self.youPicklist.get().lower()][status]:
                            yourPickScore -= 1
                elif status == '+':
                    for champion in selectedAllies:
                        if champion in self.matchupArray[self.youPicklist.get().lower()][status]:
                            yourPickScore += 1
            self.yourPickLabel.config(text=self.youPicklist.get().capitalize() + ':')
            self.yourPickValueLabel.config(text=str(yourPickScore))






    def __init__(self, allChampions, adcArray, matchupArray):
        #Assign Parameters to Variables
        self.allChampions = allChampions
        self.adcArray = adcArray
        self.matchupArray = matchupArray

        #Create Window
        self.root = tk.Tk()
        self.root.title('ADC Champion Picker')
        self.root.geometry('820x400')
        self.root.resizable(False, False)

        # Create Main Frame
        self.mainFrame = tk.Frame(self.root, width=600, bg='#e6e6e6')
        self.mainFrame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        # Main Frame
        self.mainFrameLabel = tk.Label(self.mainFrame, text='Fill in Champion Details', bg='#e6e6e6', font=('Arial', 20))
        self.mainFrameLabel.pack(side=tk.TOP, fill=tk.X)

        # Champion Select Frame
        self.championSelectFrame = tk.Frame(self.mainFrame, bg='#e6e6e6')
        self.championSelectFrame.pack(side=tk.TOP, fill=tk.X)

        # Enemy 1
        self.enemy1Label = tk.Label(self.championSelectFrame, text='Enemy 1', bg='#e6e6e6', font=('Arial', 16))
        self.enemy1Label.grid(row=0, column=0, padx=10, pady=10)
        self.enemy1Picklist = ttk.Combobox(self.championSelectFrame, values=self.allChampions, state='readonly')
        self.enemy1Picklist.grid(row=1, column=0, padx=10, pady=10)

        # Enemy 2
        self.enemy2Label = tk.Label(self.championSelectFrame, text='Enemy 2', bg='#e6e6e6', font=('Arial', 16))
        self.enemy2Label.grid(row=0, column=1, padx=10, pady=10)
        self.enemy2Picklist = ttk.Combobox(self.championSelectFrame, values=self.allChampions, state='readonly')
        self.enemy2Picklist.grid(row=1, column=1, padx=10, pady=10)

        # Enemy 3
        self.enemy3Label = tk.Label(self.championSelectFrame, text='Enemy 3', bg='#e6e6e6', font=('Arial', 16))
        self.enemy3Label.grid(row=0, column=2, padx=10, pady=10)
        self.enemy3Picklist = ttk.Combobox(self.championSelectFrame, values=self.allChampions, state='readonly')
        self.enemy3Picklist.grid(row=1, column=2, padx=10, pady=10)

        # Enemy 4
        self.enemy4Label = tk.Label(self.championSelectFrame, text='Enemy 4', bg='#e6e6e6', font=('Arial', 16))
        self.enemy4Label.grid(row=0, column=3, padx=10, pady=10)
        self.enemy4Picklist = ttk.Combobox(self.championSelectFrame, values=self.allChampions, state='readonly')
        self.enemy4Picklist.grid(row=1, column=3, padx=10, pady=10)

        # Enemy 5
        self.enemy5Label = tk.Label(self.championSelectFrame, text='Enemy 5', bg='#e6e6e6', font=('Arial', 16))
        self.enemy5Label.grid(row=0, column=4, padx=10, pady=10)
        self.enemy5Picklist = ttk.Combobox(self.championSelectFrame, values=self.allChampions, state='readonly')
        self.enemy5Picklist.grid(row=1, column=4, padx=10, pady=10)

        # Ally 1
        self.ally1Label = tk.Label(self.championSelectFrame, text='Ally 1', bg='#e6e6e6', font=('Arial', 16))
        self.ally1Label.grid(row=2, column=0, padx=10, pady=10)
        self.ally1Picklist = ttk.Combobox(self.championSelectFrame, values=self.allChampions, state='readonly')
        self.ally1Picklist.grid(row=3, column=0, padx=10, pady=10)

        # Ally 2
        self.ally2Label = tk.Label(self.championSelectFrame, text='Ally 2', bg='#e6e6e6', font=('Arial', 16))
        self.ally2Label.grid(row=2, column=1, padx=10, pady=10)
        self.ally2Picklist = ttk.Combobox(self.championSelectFrame, values=self.allChampions, state='readonly')
        self.ally2Picklist.grid(row=3, column=1, padx=10, pady=10)

        # Ally 3
        self.ally3Label = tk.Label(self.championSelectFrame, text='Ally 3', bg='#e6e6e6', font=('Arial', 16))
        self.ally3Label.grid(row=2, column=2, padx=10, pady=10)
        self.ally3Picklist = ttk.Combobox(self.championSelectFrame, values=self.allChampions, state='readonly')
        self.ally3Picklist.grid(row=3, column=2, padx=10, pady=10)

        # You
        self.youLabel = tk.Label(self.championSelectFrame, text='You', bg='#e6e6e6', font=('Arial', 16))
        self.youLabel.grid(row=2, column=3, padx=10, pady=10)
        self.youPicklist = ttk.Combobox(self.championSelectFrame, values=self.adcArray, state='readonly')
        self.youPicklist.grid(row=3, column=3, padx=10, pady=10)

        # Ally 4
        self.ally4Label = tk.Label(self.championSelectFrame, text='Ally 4', bg='#e6e6e6', font=('Arial', 16))
        self.ally4Label.grid(row=2, column=4, padx=10, pady=10)
        self.ally4Picklist = ttk.Combobox(self.championSelectFrame, values=self.allChampions, state='readonly')
        self.ally4Picklist.grid(row=3, column=4, padx=10, pady=10)

        # Go Button
        self.goButton = tk.Button(self.championSelectFrame, text='Go', bg='#c4ffd4', font=('Arial', 16), command=self.goButtonClicked)
        self.goButton.grid(row=4, column=2, padx=10, pady=10)

        # Results Frame
        self.resultsFrame = tk.Frame(self.mainFrame, bg='#e6e6e6')
        self.resultsFrame.pack(side=tk.TOP, fill=tk.X)

        # Result Labels
        self.result1Label = tk.Label(self.resultsFrame, text='Result 1:', bg='#e6e6e6', font=('Arial', 16))
        self.result1Label.grid(row=0, column=0, padx=10, pady=10)
        self.result1ValueLabel = tk.Label(self.resultsFrame, text='0', bg='#e6e6e6', font=('Arial', 16))
        self.result1ValueLabel.grid(row=1, column=0, padx=10, pady=10)
        self.result2label = tk.Label(self.resultsFrame, text='Result 2:', bg='#e6e6e6', font=('Arial', 16))
        self.result2label.grid(row=0, column=1, padx=10, pady=10)
        self.result2ValueLabel = tk.Label(self.resultsFrame, text='0', bg='#e6e6e6', font=('Arial', 16))
        self.result2ValueLabel.grid(row=1, column=1, padx=10, pady=10)
        self.result3label = tk.Label(self.resultsFrame, text='Result 3:', bg='#e6e6e6', font=('Arial', 16))
        self.result3label.grid(row=0, column=2, padx=10, pady=10)
        self.result3ValueLabel = tk.Label(self.resultsFrame, text='0', bg='#e6e6e6', font=('Arial', 16))
        self.result3ValueLabel.grid(row=1, column=2, padx=10, pady=10)
        self.result4label = tk.Label(self.resultsFrame, text='Result 4:', bg='#e6e6e6', font=('Arial', 16))
        self.result4label.grid(row=0, column=3, padx=10, pady=10)
        self.result4ValueLabel = tk.Label(self.resultsFrame, text='0', bg='#e6e6e6', font=('Arial', 16))
        self.result4ValueLabel.grid(row=1, column=3, padx=10, pady=10)
        self.yourPickLabel = tk.Label(self.resultsFrame, text='Your Pick:', bg='#e6e6e6', font=('Arial', 16))
        self.yourPickLabel.grid(row=0, column=4, padx=10, pady=10)
        self.yourPickValueLabel = tk.Label(self.resultsFrame, text='0', bg='#e6e6e6', font=('Arial', 16))
        self.yourPickValueLabel.grid(row=1, column=4, padx=10, pady=10)


    def mainloop(self):
        self.root.mainloop()