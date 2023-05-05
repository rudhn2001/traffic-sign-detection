import pyttsx3  
speech_say = pyttsx3.init()
import time
# SPEECH INDICATION  ONCE IMAGE DETECTED IT WILL CONVERT TO SPEECH
                        
# traffic_sign_text = names[c]+"Sign Ahead"
traffic_sign_text = "Sign ahead"
speech_say.say(traffic_sign_text)
speech_say.runAndWait()
time.sleep(5)