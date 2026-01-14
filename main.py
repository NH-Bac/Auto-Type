import json
import pyautogui
import keyboard
import pyperclip

pyautogui.FAILSAFE = True

with open("Logon.json", "r", encoding="utf-8") as f:
    data = json.load(f)

def init(username, password, hotkey):

    for key in hotkey.lower().split("+"):
        keyboard.release(key)

    pyperclip.copy(username)
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("tab")
    pyperclip.copy(password)
    pyautogui.hotkey("ctrl", "v")

for user in data["users"]:
    keyboard.add_hotkey(
        user["hotkey"],
        init,
        args=(user["username"], user["password"], user["hotkey"]),
    )
keyboard.wait()