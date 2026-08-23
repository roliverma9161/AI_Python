import moviepy  as mp
import speech_recognition as sr

video=mp.VideoFileClip("test.mp4")
audio_file=video.audio
audio_file.write_audiofile("test.wav")
r=sr.Recognizer()
with sr.AudioFile("test.wav")as source:
    data=r.record(source)
text=r.recognize_google(data)
print("\n the resultant text from video is: \n")
print(text)  