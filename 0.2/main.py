import voice
import cobalt
import installer

input("press enter when you are ready")
stat = True
while True:
    text = voice.getaudio()
    print(text)
    try:
        stat = cobalt.run(text, stat)
    except:
        break
        
installer.update()
