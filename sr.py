import speech_recognition as sr

filename = "16-122828-0002.wav"

r = sr.Recognizer()

# open the file
with sr.AudioFile(f'src/{filename}') as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text = r.recognize_google(audio_data)
    print(text)