import speech_recognition as sr
#imported the speech_recognition library

r = sr.Recognizer()
#associate a recogniser

# Get the microphone as input
with sr.Microphone() as source:
     print("Please Speak:")
     audio = r.listen(source)

try:
    print("You just said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Sorry, I didn't get that...")
except sr.RequestError as e:
    print("Could not get results; {0}".format(e))


