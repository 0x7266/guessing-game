import random


class Game:
    already_tried = []
    game_over = False
    lower_bound = 1
    upper_bound = 10
    score = 10
    target = random.randint(lower_bound, upper_bound)

    def get_level_input(self):
        level = input(
            f"""
Please choose a level

{' - ' * 3}
| EASY   |
| MEDIUM |
| HARD   |
| LEGEND |
{' - ' * 3}

"""
        )
        self.level = level

    def validate_input(self, input_type):
        match input_type:
            case "level":
                if self.level.lower() not in ("easy", "medium", "hard", "legend"):
                    print("Invalid level!")
                    self.get_level_input()
                    self.validate_input("level")
                else:
                    print(f"LEVEL: {self.level.upper()}")
            case "guess":
                pass

    def start(self):
        print(self.target)

        self.get_level_input()
        self.validate_input("level")
        print(
            f"""

Initial score: {self.score}

"""
        )
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
        if self.check_guess_in_range(number):
            self.check_already_tried(number)
            print("\nWRONG!")
            print(f"Score: {self.score}\n")
            self.print_already_tried()
        if self.score == 0:
            self.lose()
            self.game_over = True
            return

    def check_guess_in_range(self, number):
        if number not in range(self.lower_bound, self.upper_bound + 1):
            print(
                """Not a valid number
Please enter a number between 1 and 10"""
            )
            return False
        return True

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
