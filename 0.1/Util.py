import subprocess


class program(object):
    def __init__(self, name, command):
        self.name = name
        self.command = command


programs = [
    program("Spotify", "spotify"),
    program("obs", "C:/Program Files/obs-studio/bin/64bit/obs64.exe")
]