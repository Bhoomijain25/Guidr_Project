import gtts
import playsound

text  = input("Enter text :")
sound = gtts.gTTS(text, lang="en",tld="co.in")

sound.save("ayush.mp3")
playsound.playsound("ayush.mp3")