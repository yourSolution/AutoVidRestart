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

        if Key == self.vidRestartButton and self.loadAmount2 > 0: #If user presses Vid_restart key before the countdown ends
            time.sleep(.5)
            self.loadAmount2 = self.loadAmount

        if self.loadAmount2 == 0:
            time.sleep(1)
            press(self.vidRestartButton)
            self.loadAmount2 = self.loadAmount
