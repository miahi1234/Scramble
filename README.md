# Scramble
This application is a simple word swapping game where the player tries to unscramble a sentence by swapping letters between words. Here's how it works:

1. The `play_game()` function initializes the game by obtaining a sentence, its shuffled version, and an initial score.
2. The shuffled sentence is displayed to the player along with the current score.
3. The player continues to play the game until the sentence is unscrambled or the score reaches zero.
4. During each turn, the player can input four values representing positions of letters to swap between two words.
5. The player can also input 'undo' to revert the last swap or 'quit' to exit the game.
6. If the sentence is unscrambled, the player wins, and the final score is displayed.
7. If the shuffled sentence is not the same as the original sentence, and the score is zero, the game ends, and the player loses.

The game uses functions from the `services` module to initialize the game and perform swaps, as well as functions from the `ui` module to display messages and get user input. The `previous_shuffled_sentence` variable keeps track of the previous shuffled sentence to enable the 'undo' functionality.
