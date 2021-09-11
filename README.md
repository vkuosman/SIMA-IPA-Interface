# SIMA-IPA-Interface
Basic tkinter GUI for the Finnish intelligent personal assistant SIMA.

SIMA has many features also found in other similar virtual assistants, such as asking for the time, controlling smart lights etc.
Currently SIMA has only been tested on a desktop PC running Ubuntu 18.04 and compatibility with other platforms cannot be guaranteed.
At the moment users will be required to provide their own model and scorer, but these may become publicly available in the future.

To ensure that IFTTT requests work correctly you will have to setup following IFTTT applets:
"LightViolet" > Set the lights to purple
"LightGreen" > Set the lights to green
LightBlue" > Set the lights to blue
"LightRed" > Set the lights to red
"LightRed2" > Set the lights to the fireplace setting
"LightOff" > Toggle the lights
"LightWhite" > Set the lights to daylight
"PythonMusic" > Play music
"PythonCalendar" > Add event to Google Calendar

Names of these applets and their functions are subject to change and may need to be updated with future revisions.

Requirements:
gtts
playsound
pyaudio
wave
pygooglenews
selenium
wikipediaapi
chrome webdriver
