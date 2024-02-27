import unittest
from services import  shuffle_sentence, initialize_game, perform_swap
from Repository import load_variants

class TestWordShufflingGame(unittest.TestCase):
    def test_load_variants(self):
        # Assuming variants.txt contains sample variants
        variants = load_variants("variants.txt")
        self.assertTrue(variants, "Variants list is not empty")



    def test_shuffle_sentence(self):
        sentence = "the quick brown fox jumps over the lazy dog"
        shuffled_sentence = shuffle_sentence(sentence)
        self.assertEqual(len(shuffled_sentence), len(sentence), "Shuffled sentence has the same length as the original")

    def test_initialize_game(self):
        sentence, shuffled_sentence, score = initialize_game()
        self.assertTrue(sentence, "Initialized sentence is not empty")
        self.assertTrue(shuffled_sentence, "Initialized shuffled sentence is not empty")
        self.assertGreaterEqual(score, 0, "Initialized score is non-negative")

    def test_perform_swap(self):
        shuffled_sentence = "the quick brown fox jumps over the lazy dog"
        word1_position, letter1_position, word2_position, letter2_position = 1, 1, 2, 2
        _, updated_score = perform_swap(shuffled_sentence, word1_position, letter1_position, word2_position, letter2_position, 0)
        self.assertNotEqual(updated_score, 0, "Perform swap changes the score")

if __name__ == "__main__":
    unittest.main()
