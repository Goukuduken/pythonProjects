import speech_recognition as sr 
import PyAudio
import os
import sys
import webbrowser
import pyttsx3


def talk(words):
	"""принимаем параметры строки, озвучиваем ее"""
	engine = pyttsx3.init()
	engine.say(words)
	engine.runAndWait()


def listener():
	r = sr.Recognizer()
	with sr.Microphone() as obj_list:
		print('Say me something')
		r.pause_threshold = 1
		r.adjust_for_ambient_noise(obj_list, duration=1) #метод, позволяющий убрать посторонние шумы
		audio = r.listen(obj_list)
	try:
		command = r.recognize_google(audio).lower() #получили список и пихнули в нижний регистр
		print('You told me ' + command)
	except sr.UnknownValueError:
		talk("I don't understand you!")
		command = listener()
	return command


def take_voice(command):
	if 'open github' in command:
		URL = 'https://github.com/'
		talk('Okay! I open now!')
		webbrowser.open(URL)
	elif 'stop' in command:
		talk('Bye Bye! Friend!')
		sys.exit()

while True:
	take_voice(listener())
