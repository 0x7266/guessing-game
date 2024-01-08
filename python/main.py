import random


class Game:
    already_tried = []
    game_over = False
    lower_bound = 1
    upper_bound = 10
    score = 10
    target = random.randint(lower_bound, upper_bound)

    def start(self):
        print(self.target)
        print(f"Initial score: {self.score}")
        while not self.game_over:
            self.guess(
                int(
                    input(
                        f"Pick a number between {self.lower_bound} and {self.upper_bound}\n"
                    )
                )
            )

    def guess(self, number: int):
        if self.target == number:
            self.win()
            self.game_over = True
            return
        self.check_already_tried(number)
        print("\nWRONG!")
        print(f"Score: {self.score}\n")
        self.print_already_tried()
        if self.score == 0:
            self.lose()
            self.game_over = True
            return

    def check_already_tried(self, number):
        if number in self.already_tried:
            print("You've already tried this number")
            return
        self.already_tried.append(number)
        self.score -= 1

    def print_already_tried(self):
        print(f"NUMBERS YOU'VE ALREADY TRIED: { self.already_tried }\n")

    def win(self):
        print("\nCORRECT!")
        print(f"Final score: {self.score}\n")
        print("You win\n\n")

    def lose(self):
        print("GAME OVER!")
        print("You lose\n\n")


game = Game()
game.start()

# TODO: fix score logic
