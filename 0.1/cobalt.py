import voice
import wikipedia
import Util as u
import os
import subprocess as s
import sys


def run(c):

    if c[0:7] == "Cobalt " or c[0:7] == "Kobalt ":

        if c[7:7+8] == "question":

            try:
                voice.speak(wikipedia.summary(c[7+9:]))
            except:
                voice.speak("No resoults found")

        elif c[7:10] == "run":
            
            os.system(c[10:])

        elif c[7:14] == "launch " or c[7:13] == "lunch ":
            
            found = False
            print(c[14:])
            for program in u.programs:
                if program.name == c[14:]:
                    voice.speak(f"Launching {program.name}")
                    s.Popen(program.command)
                    found = True

            if found == False:
                
                voice.speak("No such program!")

        elif c[7:11] == "stop":

            voice.speak("Do you really want me to stop?")
            a = voice.getaudio()
            print(a)
            if a == "Yes" or a == "yes":
                
                voice.speak("OK. Goodbye")
                sys.exit()

            else:
                
                voice.speak("OK")

        elif c[7:7+15] == "you are stupid":

            voice.speak("Thank you but you are more stupid than me. So shut up")

        elif c[7:7+11] == "who are you":

            voice.speak("I am Cobalt. I am a robot made by Hawk_x6x. I am made to help you.")

        elif c[7:7+4] == "help":

            info = "I am Cobalt. My commands are question, run, launch, stop."

            voice.speak(info)

        else:

            print("i dont understand you")
            voice.speak("I dont understand you?")

    else:
        
        pass