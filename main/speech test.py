import win32com.client
import sys
speak=win32com.client.Dispatch("SAPI.SpVoice")
print("Enter the word you want to speak it out by computer or ""stop"" to stop.")
try:
    while 1: 
        s=input("-->>") 
        if (s=="stop" or s=="quit" or s=="exit"):
            break
        else:
            speak.Speak(s)
except:
    print("User or Connection Error")
finally:
    print("thanks for using, by ayushmaan karmokar")
    
