# test_hangman_game.py
from hangman_game import HangmanGame


class TestHangmanGameInitialization:
    def test_basic_level_initialization(self):
        """Test that basic level game initializes correctly."""
        game = HangmanGame('basic')
        assert game.level == 'basic'
        assert game.lives == 6
        assert game.game_over is False
        assert hasattr(game, 'answer')

    def test_intermediate_level_initialization(self):
        """Test intermediate level with phrases."""
        game = HangmanGame('intermediate')
        assert game.level == 'intermediate'
        assert ' ' in game.answer  # Should contain spaces for phrases


class TestHangmanDisplay:
    def test_initial_display_shows_underscores(self):
        """Test that initial display shows underscores for letters."""
        game = HangmanGame('basic')
        display = game.get_display()
        assert '_' in display
        assert len(display) == len(game.answer)
        # No actual letters should be visible initially
        assert not any(c.isalpha() for c in display)


class TestInputValidation:
    def test_valid_single_letter_guess(self):
        """Test that single letters are valid guesses."""
        game = HangmanGame('basic')
        assert game.is_valid_guess('a') is True
        assert game.is_valid_guess('Z') is True

    def test_invalid_empty_guess(self):
        """Test that empty guesses are invalid."""
        game = HangmanGame('basic')
        assert game.is_valid_guess('') is False
        assert game.is_valid_guess(None) is False

    def test_invalid_multiple_character_guess(self):
        """Test that multiple character guesses are invalid."""
        game = HangmanGame('basic')
        assert game.is_valid_guess('ab') is False
        assert game.is_valid_guess('hello') is False

    def test_already_guessed_letter_invalid(self):
        """Test that already guessed letters are invalid."""
        game = HangmanGame('basic')
        game.guessed_letters.add('A')
        assert game.is_valid_guess('A') is False
        assert game.is_valid_guess('a') is False  # Case insensitive


class TestGameLogic:
    def test_correct_guess_reveals_letters(self):
        """Test that correct guesses reveal letters and don't reduce lives."""
        game = HangmanGame('basic')
        # Set known answer for predictable testing
        game.answer = "PYTHON"

        success, message = game.make_guess('P')
        assert success is True
        assert 'P' in game.get_display()
        assert game.lives == 6  # Lives shouldn't decrease
        assert "Good guess" in message

    def test_incorrect_guess_reduces_lives(self):
        """Test that incorrect guesses reduce lives."""
        game = HangmanGame('basic')
        game.answer = "PYTHON"
        original_lives = game.lives

        success, message = game.make_guess('Z')
        assert success is False
        assert 'Z' not in game.get_display()
        assert game.lives == original_lives - 1
        assert "Sorry" in message

    def test_winning_condition(self):
        """Test that game recognizes win condition."""
        game = HangmanGame('basic')
        game.answer = "CAT"

        # Guess all letters
        game.make_guess('C')
        game.make_guess('A')
        success, message = game.make_guess('T')

        assert game.game_over is True
        assert hasattr(game, 'won') and game.won is True
        assert "Congratulations" in message
