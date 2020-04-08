import time
import random
import simpleaudio as sa
from threading import Timer
import threading


#wma_list = [AudioSegment.from_file('желтый.wma','wma'), AudioSegment.from_file('красный.wma','wma'),
		    #AudioSegment.from_file('зеленый.wma','wma'), AudioSegment.from_file('синий.wma','wma')]


wma_list = ['1.wav', '2.wav', '3.wav', '4.wav']

timing = time.time()
stop = input('Введите количество секунд:\n')
end_sound = '10.wav'
while True:
	random.shuffle(wma_list)
	for wav in wma_list:
			wave_obj = sa.WaveObject.from_wave_file(wav)
			play_obj = wave_obj.play()
			play_obj.wait_done()
			time.sleep(0.500)
	if time.time() - timing >float(stop):
		wave_obj_end = sa.WaveObject.from_wave_file(end_sound)
		play_obj_end = wave_obj_end.play()
		play_obj_end.wait_done()
		print('Time is over!')
		break


