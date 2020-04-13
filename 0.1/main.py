import voice
import cobalt
import installer

input("press enter when you are ready")
while True:
    text = voice.getaudio()
    print(text)
    cobalt.run(text)
installer.update()