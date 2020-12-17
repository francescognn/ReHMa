from project.runner.runner import Runner
import RPi.GPIO as GPIO


class PlatformRunner(Runner):
    def read_temperatures(self):
        # TODO: to be reviewed, there is a library for the sensor
        GPIO.setmode(GPIO.BCM)
        INPUT_PIN = self.IOs["TIN"].pin
        GPIO.setup(INPUT_PIN, GPIO.IN)
        self.temperatures["Sala"] = GPIO.input(INPUT_PIN)
