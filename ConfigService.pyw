from pyautogui import press
import time

class DeCrashService():
    def __init__(self, loadAmount, vidRestartButton, loadButton):
        self.loadAmount = loadAmount
        self.vidRestartButton = vidRestartButton
        self.loadButton = loadButton
        self.loadAmount2 = loadAmount

    def vidRestart(self, Key):

        if Key == self.loadButton:
            self.loadAmount2 -= 1
            print(self.loadAmount2)

        if self.loadAmount2 == 0:
            time.sleep(1)
            press(self.vidRestartButton)
            self.loadAmount2 = self.loadAmount
