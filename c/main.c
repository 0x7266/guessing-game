#include <process.h>
#include <stdio.h>
#include <stdlib.h>
#include <windows.h>

int random_number(int max) {
  int x;
  x = rand() % max + 1;
  return x;
}

int main() {
  int balance = 1000, bet, guess, dice;
  srand(getpid());

  while (balance > 0) {
    printf("Please place a bet: ");
    fflush(stdout);
    scanf("%d", &bet);
    if (bet > balance) {
      printf("\nInsuficient credit\n");
      continue;
    }
    printf("Please guess a number between 1 and 6 or pick 0 to quit: ");
    scanf("%d", &guess);
    if (guess == 0) {
      return 0;
    }
    Sleep(2);
    dice = random_number(6);
    printf("DICE: %d\n", dice);
    if (guess != dice) {
      balance -= bet;
    } else {
      bet *= 3;
      balance += bet;
    }
    if (balance == 0) {
      printf("\n\nGAME OVER!\n");
      return 0;
    }
    printf("Balance: %d\n", balance);
  }
  return 0;
}
