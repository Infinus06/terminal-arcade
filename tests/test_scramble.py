"""Tests for the Scramble."""

from arcade.games import scramble


def test_is_solved_correct_guess():
    assert scramble.is_solved("apple", "apple")

def test_is_solved_incorrect_guess():
    assert not scramble.is_solved("apple", "paple")

def test_first_guess_scores_the_most():
    assert scramble.total_score(0) > scramble.total_score(2)

def test_shuffle_word_preserves_letters():
    word = "apple"
    shuffled_word = scramble.shuffle_word(word) 
    assert sorted(word) == sorted(shuffled_word)
    assert word != shuffled_word
