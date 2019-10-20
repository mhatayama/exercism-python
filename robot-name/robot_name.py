import random
import string

class Robot(object):
    def __init__(self):
        self.name = self.create_a_name()

    def reset(self):
        while True:
            new_name = self.create_a_name()
            if new_name != self.name:
                self.name = new_name
                break

    def create_a_name(self):
        letters = [random.choice(string.ascii_uppercase) for _ in range(2)]
        digits = [str(random.randint(0, 9)) for _ in range(3)]
        return ''.join(letters + digits)