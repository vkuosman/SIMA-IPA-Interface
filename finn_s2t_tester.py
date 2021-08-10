import os
import pyaudio_test
import numpy
from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("S2T Tester")

location = os.path.dirname(os.path.abspath(__file__))

infoArray = []
with open(location + '/default_entries.txt') as infoFile:
    for line in infoFile:
        infoArray.append(line)


# Functions
def s2tFunc():
    dsCommand = "deepspeech --model " + modelEntry.get() + " --scorer " + scorerEntry.get() + " --audio " + location + "/s2t_test_recording.wav > " + location + "/ds_s2t_output.txt"

    # Temporary solution. Look into more elegant methods.
    os.system("cd " + location)
    os.system(dsCommand)

def saveInfo(string1, string2):
    file = open(location + "/default_entries.txt", "a")
    file.truncate(0)
    file.write(string1 + "\n" + string2)
    file.close()

def voiceRecord():
    start = pyaudio_test.voiceRecorder()
    start.record()

def displayIntep(label):
    outputArray = []
    with open(location + '/ds_s2t_output.txt') as outputText:
        for line in outputText:
            outputArray.append(line)
    label.config(text=outputArray[0][:-1])

def onClick():
    print("\nSaving information...\n")

    saveInfo(scorerEntry.get(), modelEntry.get())
    print("\nStarting recording...\n")

    voiceRecord()
    print("\nRecording complete. Starting S2T...\n")

    s2tFunc()
    initialLabel.config(text="S2T complete. Click the button to try again.")

    displayIntep(commandLabel)

# Entry fields
dsEntry = Entry(root, width=80)

scorerEntry = Entry(root, width=80)
scorerEntry.insert(END, infoArray[0][:-1])

modelEntry = Entry(root, width=80)
modelEntry.insert(END, infoArray[1])

# Title
finnLabel = Label(root, text="Finnish S2T Testing Interface")

# Prompt texts
dsLabel = Label(root, text="Please select the DeepSpeech folder (feature not yet implemented): ")
scorerLabel = Label(root, text="Please select the scorer: ")
modelLabel = Label(root, text="Please select the model to be tested: ")
initialLabel = Label(root, text="Recording should end automatically after the user stops speaking. Please wait.")

# Misc
# Temporary solution. Need to look more into the grid system.
nullLabel1 = Label(root, text=" ")
nullLabel2 = Label(root, text=" ")
commandLabel = Label(root, text="Interpretations will be shown here.")

# Buttons
myButton = Button(root, text="Start recording", command=onClick)

finnLabel.grid(row=0, column=0)
finnLabel.configure(font=("Helvetica", 16, "bold"))

dsLabel.grid(row=1, column=0)
dsEntry.grid(row=2, column=0)

scorerLabel.grid(row=3, column=0)
scorerEntry.grid(row=4, column=0)

modelLabel.grid(row=5, column=0)
modelEntry.grid(row=6, column=0)

myButton.grid(row=7, column=0)
initialLabel.grid(row=8, column=0)
nullLabel1.grid(row=9, column=0)
commandLabel.grid(row=10, column=0)
commandLabel.configure(font=("Helvetica", 12, "italic"))
nullLabel2.grid(row=11, column=0)

root.mainloop()