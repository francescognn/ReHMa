from project.runner import Runner
import RPi.GPIO as GPIO


class PlatformRunner(Runner):
    def update_input(self):
        GPIO.setmode(GPIO.BCM)
        INPUT_PIN = self.IOs["TIN"].pin
        GPIO.setup(INPUT_PIN, GPIO.IN)
        self.input_data["TIN"] = GPIO.input(INPUT_PIN)