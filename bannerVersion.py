import psutil
from time import sleep
#import simpleaudio as sa
from tkinter import *

# Tkinter Function
def banner(label): # Battery Charge 20 or 80
        w = 360
        h = 80
        x = (1920/2) - 180
        y = (1080/2) - 40

        splash_root = Tk()

        splash_root.geometry("%dx%d+%d+%d" % (w, h, x, y))
        splash_root.attributes('-alpha', 0.5)
        splash_label = Label(splash_root, text=label, font=("Terminal",18))
        splash_label.pack()

        splash_root.mainloop()

# Simpeaudio Function
# wave_obj = sa.WaveObject.from_wave_file("alert.wav")

#def make_noice(sound_file):
#       play_obj = wave_obj.play()
#       play_obj.wait_done()

while True:
        battery = psutil.sensors_battery()
        p = percent = battery.percent
        plugged = battery.power_plugged

        if p > 80:
                if plugged == False:
                        sleep(60)
                else:
                        banner(f"\nBattery Charge {percent}%")
                        #make_noice(wave_obj)
                        sleep(2)

        elif p > 20 and p < 80:
                sleep(60)

        elif p < 20:
                if plugged:
                        sleep(60)
                else:
                        banner("\nBattery Charge {percent}%")
                        #make_noice(wave_obj)
                        sleep(2)
