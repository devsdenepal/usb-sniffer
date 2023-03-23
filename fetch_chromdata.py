import csv
import os
import time
import pyautogui

# Set the path to your Chrome user data directory
chrome_data_dir = os.path.expanduser("~") + "/AppData/Local/Google/Chrome/User Data/"

# Set the path to the Chrome password export file
export_file_path = os.path.join(os.getcwd(), "chrome_passwords.csv")

# Launch Chrome and navigate to the passwords page
pyautogui.press("win")
pyautogui.typewrite("chrome")
pyautogui.press("enter")
time.sleep(1)
pyautogui.hotkey("ctrl", "l")
pyautogui.typewrite("chrome://settings/passwords")
pyautogui.press("enter")
time.sleep(2)

# Click the export passwords button and save the CSV file
pyautogui.hotkey("ctrl", "shift", "i")
time.sleep(1)
pyautogui.hotkey("ctrl", "shift", "p")
pyautogui.typewrite("Export passwords")
pyautogui.press("enter")
time.sleep(1)
pyautogui.hotkey("ctrl", "s")
time.sleep(1)
pyautogui.typewrite(export_file_path)
pyautogui.press("enter")
time.sleep(1)
pyautogui.hotkey("ctrl", "w")

# Read the exported passwords from the CSV file
with open(export_file_path, newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        # Do something with the password data
        print(row)
