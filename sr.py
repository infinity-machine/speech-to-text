import speech_recognition as sr

filename = "charles-manson.mp3"

r = sr.Recognizer()

# OPEN FILE
with sr.AudioFile(f'src/{filename}') as source:
    # LOAD AUDIO TO MEMORY
    audio_data = r.record(source)
    # CONVERT SPEECH TO TEXT
    text = r.recognize_google(audio_data)
    print(text)