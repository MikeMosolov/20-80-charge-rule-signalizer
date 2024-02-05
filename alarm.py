import time
import psutil
import simpleaudio as sa


wave_obj = sa.WaveObject.from_wave_file("alert.wav")

def make_noice(sound_file):
	play_obj = wave_obj.play()
	play_obj.wait_done()
	
while True:
	battery = psutil.sensors_battery()
	p = percent = battery.percent
	plugged = battery.power_plugged
	
	if p > 80:
		if plugged == False:
			time.sleep(10800)
		else:
			make_noice(wave_obj)
			time.sleep(20)		
		
	elif p > 20 and p < 80:
		time.sleep(60)

	elif p < 20:
		if plugged:
			time.sleep(1800)
		else:
			make_noice(wave_obj)
			time.sleep(20)
