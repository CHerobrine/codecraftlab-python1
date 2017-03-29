import pyautogui, msvcrt
time=int(input('how many seconds would you like this to run for?'))
for i in range(time*10):
    pyautogui.click()
