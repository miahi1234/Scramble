import random
from Repository import load_variants
from ui import display_message

#we take all the letters in the middle of the words, scramble them together and put them back in
def shuffle_sentence(sentence):
    original_sentence = sentence
    shuffled_sentence = sentence

    while shuffled_sentence == original_sentence:
        words = sentence.split()
        middle_letters = [char for word in words for char in word[1:-1]]
        random.shuffle(middle_letters)

        for i, word in enumerate(words):
            if len(word) > 2:
                words[i] = word[0] + ''.join(middle_letters[:len(word) - 2]) + word[-1]
                middle_letters = middle_letters[len(word) - 2:]

        shuffled_sentence = ' '.join(words)

    return shuffled_sentence
#we get a random sentence, shuffle it, and get the score
def initialize_game():
    variants = load_variants()
    sentence = random.choice(variants)
    shuffled_sentence = shuffle_sentence(sentence)
    score = sum(len(word) for word in sentence.split())
    return sentence, shuffled_sentence, score
#we perform the swap
def perform_swap(shuffled_sentence, word1_position, letter1_position, word2_position, letter2_position, score):
    words = shuffled_sentence.split()

    if 0 <= word1_position < len(words) and 0 <= word2_position < len(words):
        original_word1 = list(words[word1_position])
        original_word2 = list(words[word2_position])

        if 0 <= letter1_position < len(original_word1) and 0 <= letter2_position < len(original_word2):
            original_word1[letter1_position], original_word2[letter2_position] = original_word2[letter2_position], \
                original_word1[letter1_position]

            words[word1_position] = ''.join(original_word1)
            words[word2_position] = ''.join(original_word2)

            updated_sentence = ' '.join(words)
            return updated_sentence, score - 1
        else:
            # Invalid letter position
            display_message("Invalid letter position. Please enter valid positions.")
    else:
        # Invalid word position
        display_message("Invalid word position. Please enter valid positions.")

    return shuffled_sentence, score  # No change due to invalid positions