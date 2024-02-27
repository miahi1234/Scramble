from services import initialize_game, perform_swap
from ui import display_message, get_user_input
previous_shuffled_sentence = None

def play_game():
#previous shuffled sentence keeps track of the shuffle there was before a swap so we can use the undo
    global previous_shuffled_sentence

    sentence, shuffled_sentence, score = initialize_game()
    display_message(f"Shuffled Sentence: {shuffled_sentence}\n Score:{score}")
#the game plays as long as the sentence is still scrambled or we have score
    while score > 0:
        user_input = get_user_input().lower().split()
#to make it easier, we will write the position we want using normal counting from 1 and it will automatically decrease it by 1 for the program
        if len(user_input) == 4:
            try:
                word1_position, letter1_position, word2_position, letter2_position = map(int, user_input)
                word1_position -= 1
                word2_position -= 1
                letter1_position -= 1
                letter2_position -= 1
            except ValueError:
                display_message("Invalid input. Please enter valid integers.")
                continue

            shuffled_sentence, score = perform_swap(shuffled_sentence, word1_position, letter1_position, word2_position,
                                                    letter2_position, score)
            previous_shuffled_sentence = shuffled_sentence
            display_message(f"Shuffled Sentence: {shuffled_sentence}\nScore: {score}")
#check if the game is won
            if shuffled_sentence == sentence:
                display_message(f"Congratulations! You've unscrambled the sentence.\n Final Score: {score} ")
                break
#we turn the PSS back to none so we dont keep undoing into the same sentence
        elif user_input[0] == 'undo':
            if previous_shuffled_sentence is not None:
                shuffled_sentence = previous_shuffled_sentence
                previous_shuffled_sentence = None
                display_message(f"Undone. Shuffled Sentence: {shuffled_sentence}\nScore: {score}")
            else:
                display_message("Nothing to undo.")
                #upon using quit the program closes
        elif user_input[0] == 'quit':
            display_message("Quitting the program.")
            break
        else:
            display_message("Invalid input format. Please enter 4 values (word1_position letter1_position word2_position letter2_position), 'undo', or 'quit'.")
#we check in the end if we have the correct sentence otherwise the game is lost
    if shuffled_sentence != sentence:
        display_message("Game Over. Better luck next time.")