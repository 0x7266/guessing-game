import random


class Game:
    def __init__(self) -> None:
        self.game_over = False
        self.score = 10
        self.target = random.randint(1, 10)

    def guess(self, number: int):
        self.score -= 1
        if self.target == number:
            self.win()
            self.game_over = True
            return
        print("\nWRONG!")
        print(f"Score: {self.score}\n")
        if self.score == 0:
            self.lose()
            self.game_over = True
            return

    def start(self):
        print(f"Initial score: {self.score}")
        while not self.game_over:
            self.guess(int(input("Pick a number between 1 and 10\n")))

    def win(self):
        print("\nCORRECT")
        print(f"Final score: {self.score + 1}\n")
        print("You win\n\n")

    def lose(self):
        print("GAME OVER")
        print("You lose\n\n")


game = Game()
game.start()

# TODO: keep track of already guessed numbers
