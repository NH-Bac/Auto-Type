import json
import pyautogui
import keyboard

with open("config.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def init(text, hotkey):
    for key in hotkey.lower().split("+"):
        keyboard.release(key)

    pyautogui.write(text, interval=data["interval"])
    if data["autoEnter"] == 1: pyautogui.press("enter")

for s in data["type"]:
    keyboard.add_hotkey(
        s["key"],
        init,
        args=(s["string"], s["key"]),)

keyboard.wait()