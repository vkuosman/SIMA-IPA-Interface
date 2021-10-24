import os
import pyaudio_test
import command_guess
from request_sender import sendRequest
from t2s_tester import speakLine
from tkinter import *

import playsound
from gtts import gTTS

root = Tk()
root.title("SIMA Interface")

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

def saveInfo(string1, string2, string3, string4):
    file = open(location + "/default_entries.txt", "a")
    file.truncate(0)
    file.write(string1 + "\n" + string2 + "\n" + string3 + "\n" + string4)
    file.close()

def voiceRecord():
    start = pyaudio_test.voiceRecorder()
    start.record()

def displayIntep(label):
    outputArray = []
    with open(location + '/ds_s2t_output.txt') as outputText:
        for line in outputText:
            outputArray.append(line)
    sentence = outputArray[0][:-1]
    label.config(text=sentence)
    return(sentence)

def speakLine(input_string):
    tts = gTTS(input_string, lang='fi')
    audio_file = "s2t-audio.mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)

def onClick():
    print("\nSaving information...\n")

    saveInfo(scorerEntry.get(), modelEntry.get(), iftttEntry.get(), searchEntry.get())
    print("\nStarting recording...\n")

    voiceRecord()
    print("\nRecording complete. Starting S2T...\n")
    root.update()

    s2tFunc()
    initialLabel.config(text="S2T complete. Click the button to try again.")
    root.update()

    command = displayIntep(commandLabel)
    root.update()

    t2s_input = sendRequest(command_guess.check_score(command),guessLabel, iftttEntry.get())
    root.update()

    speakLine(t2s_input)

    # Currently outputs are not cleared when an error occurs. Needs updating in the future.
    os.remove(location + '/ds_s2t_output.txt')
    os.remove(location + '/s2t_test_recording.wav')
    os.remove(location + '/s2t-audio.mp3')

    print("\nDONE\n")

# Entry fields
searchEntry = Entry(root, width=80)
searchEntry.insert(END, infoArray[3])

iftttEntry = Entry(root, width=80)
iftttEntry.insert(END, infoArray[2][:-1])

scorerEntry = Entry(root, width=80)
scorerEntry.insert(END, infoArray[0][:-1])

modelEntry = Entry(root, width=80)
modelEntry.insert(END, infoArray[1][:-1])

# Title
finnLabel = Label(root, text="SIMA Interface")

# Prompt texts
searchLabel = Label(root, text="You may enter a supported search engine url here (optional): ")
iftttLabel = Label(root, text="Please enter your IFTTT key to control smart devices: ")
scorerLabel = Label(root, text="Please select the scorer: ")
modelLabel = Label(root, text="Please select the model to be tested: ")
initialLabel = Label(root, text="Recording should end automatically after the user stops speaking. Please wait.")

# Misc
# Temporary solution. Need to look more into the grid system.
nullLabel1 = Label(root, text=" ")
nullLabel2 = Label(root, text=" ")
nullLabel3 = Label(root, text=" ")
commandLabel = Label(root, text="Interpretations will be shown here.")
guessLabel = Label(root, text="Assumed commands will be shown here.")

# Buttons
testingButton = Button(root, text="Start recording", command=onClick)

# Settting up the initial grid

# Title
finnLabel.grid(row=0, column=0)
finnLabel.configure(font=("Helvetica", 16, "bold"))

# Search input field
searchLabel.grid(row=1, column=0)
searchEntry.grid(row=2, column=0)

# DS input field
iftttLabel.grid(row=1+2, column=0)
iftttEntry.grid(row=2+2, column=0)

# Scorer input field
scorerLabel.grid(row=3+2, column=0)
scorerEntry.grid(row=4+2, column=0)

# Model input field
modelLabel.grid(row=5+2, column=0)
modelEntry.grid(row=6+2, column=0)

# Recording button
testingButton.grid(row=7+2, column=0)

# Instruction texts
initialLabel.grid(row=8+2, column=0)

nullLabel1.grid(row=9+2, column=0)

# Interpreted text
commandLabel.grid(row=1+20, column=0)
commandLabel.configure(font=("Helvetica", 12, "italic"))

nullLabel2.grid(row=1+21, column=0)

# Estimated command
guessLabel.grid(row=1+22, column=0)
guessLabel.configure(font=("Helvetica", 12))

nullLabel3.grid(row=1+23, column=0)

root.mainloop()