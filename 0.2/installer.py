import requests
import os
import json


files = []
version = ""
verpath = "https://oneonenot.github.io/cobalt.json"


def init():
    os.mkdir("C:/cobalt")


def download(name):
    x = requests.get(f"https://oneonenot.github.io/Cobalt/{version}/{name}")

    with open(f"C:/cobalt/{name}", "w") as f:
        f.write(x.text)


def getversion():
    global version
    version = requests.get("https://oneonenot.github.io/Cobalt/cobalt.version").text


def analyze(text):
    global files
    global version
    history = json.loads(text)
    ver = history[version]
    files = ver[files]


def update():
    getversion()
    analyze(requests.get(verpath).text)
    for f in files:
        download(f)