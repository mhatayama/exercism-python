# Game status categories
# Change the values as you see fit
STATUS_WIN = "win"
STATUS_LOSE = "lose"
STATUS_ONGOING = "ongoing"


class Hangman(object):
    def __init__(self, word):
        self.word = word
        self.guesses = set()
        self.remaining_guesses = 9
        self.status = STATUS_ONGOING

    def guess(self, char):
        if self.status == STATUS_WIN:
            raise ValueError("You already won!")
        if self.status == STATUS_LOSE:
            raise ValueError("You already lost!")

        if char in self.word and char not in self.guesses:
            self.guesses.add(char)
            if self.word == self.get_masked_word():
                self.status = STATUS_WIN
        else:
            self.remaining_guesses -= 1
            if self.remaining_guesses < 0:
                self.status = STATUS_LOSE

    def get_masked_word(self):
        return ''.join(x if x in self.guesses else '_' for x in self.word)

    def get_status(self):
        return self.status
