import time
from threading import Thread, Timer


class ReminderThread(Thread):
    def __init__(self, message):
        super().__init__(daemon=True)
        self.message = message

    def run(self):
        while True:
            print(self.message)
            time.sleep(2)


reminder = ReminderThread("This is a reminder")
reminder.start()


def alarm():
    print("Alarm! Time to wrap up")


Timer(5, alarm).start()

time.sleep(10)
print("Main finishes; reminder (daemon) stops.")
