import speech_recognition as sr

file = "16-122828-0002.wav"

r = sr.Recognizer()

# OPEN FILE
with sr.AudioFile(f'src/{file}') as source:
    # LOAD AUDIO TO MEMORY
    audio_data = r.record(source)
    # CONVERT SPEECH TO TEXT
    text = r.recognize_google(audio_data)
    print(text)