# hangman_game.py
import random
import time
import threading


class HangmanGame:
    """
    Hangman game implementation following TDD principles.
    """

    # Word and phrase dictionaries
    BASIC_WORDS = [
        'PYTHON', 'COMPUTER', 'PROGRAMMING', 'SOFTWARE', 'TESTING',
        'DEVELOPMENT', 'ALGORITHM', 'FUNCTION', 'VARIABLE', 'OBJECT'
    ]

    INTERMEDIATE_PHRASES = [
        'TEST DRIVEN DEVELOPMENT',
        'OBJECT ORIENTED PROGRAMMING',
        'SOFTWARE ENGINEERING PRINCIPLES',
        'DATABASE MANAGEMENT SYSTEM',
        'USER INTERFACE DESIGN'
    ]

    def __init__(self, level='basic', lives=6):
        """Initialize the Hangman game."""
        self.level = level.lower()
        self.lives = lives
        self.max_lives = lives
        self.game_over = False
        self.won = False
        self.guessed_letters = set()
        self.incorrect_guesses = set()
        self.time_limit = 15  # seconds per guess
        self.timer_active = False
        self.time_up = False

        # Select word or phrase based on level
        if self.level == 'basic':
            self.answer = random.choice(self.BASIC_WORDS)
        else:
            self.answer = random.choice(self.INTERMEDIATE_PHRASES)

    def get_display(self):
        """Get current display state showing underscores."""
        result = []
        for char in self.answer:
            if char.isalpha():
                if char in self.guessed_letters:
                    result.append(char)
                else:
                    result.append('_')
            else:
                result.append(char)  # Keep spaces and punctuation
        return ''.join(result)

    def is_valid_guess(self, guess):
        """Validate if the guess is a single letter and not guessed."""
        if not guess or len(guess) != 1 or not guess.isalpha():
            return False
        return guess.upper() not in self.guessed_letters

    def make_guess(self, guess):
        """Process a player's guess and return success status and message."""
        if self.game_over:
            return False, "Game is already over!"

        guess = guess.upper()

        if not self.is_valid_guess(guess):
            return False, "Invalid guess or already guessed!"

        self.guessed_letters.add(guess)

        if guess in self.answer:
            # Check for win condition
            if '_' not in self.get_display():
                self.won = True
                self.game_over = True
                return True, "Congratulations! You won!"
            return True, f"Good guess! '{guess}' is in the answer."
        else:
            # Incorrect guess - reduce lives
            self.incorrect_guesses.add(guess)
            self.lives -= 1
            if self.lives <= 0:
                self.game_over = True
                self.won = False
                return False, f"Game Over! The answer was: {self.answer}"
            msg = f"Sorry, '{guess}' is not in the answer. Lives: {self.lives}"
            return False, msg

    def start_timer(self):
        """Start the 15-second timer for a guess."""
        self.time_up = False
        self.timer_active = True

        def timer_thread():
            time.sleep(self.time_limit)
            if self.timer_active:
                self.time_up = True
                if not self.game_over:
                    self.lives -= 1
                    if self.lives <= 0:
                        self.game_over = True

        threading.Thread(target=timer_thread, daemon=True).start()

    def stop_timer(self):
        """Stop the current timer."""
        self.timer_active = False

    def is_time_up(self):
        """Check if time is up for current guess."""
        return self.time_up

    def get_game_state(self):
        """Get current game state."""
        return {
            'level': self.level,
            'display': self.get_display(),
            'lives': self.lives,
            'max_lives': self.max_lives,
            'guessed_letters': sorted(list(self.guessed_letters)),
            'incorrect_guesses': sorted(list(self.incorrect_guesses)),
            'game_over': self.game_over,
            'won': self.won,
            'answer': self.answer if self.game_over else None
        }


class HangmanGameUI:
    """Simple console-based UI for the Hangman game."""

    def __init__(self):
        self.game = None

    def display_menu(self):
        """Display the main menu."""
        print("\n" + "="*50)
        print("           WELCOME TO HANGMAN GAME")
        print("="*50)
        print("1. Basic Level (Words)")
        print("2. Intermediate Level (Phrases)")
        print("3. Quit Game")
        print("="*50)

    def get_level_choice(self):
        """Get level choice from user."""
        while True:
            choice = input("Enter your choice (1-3): ").strip()
            if choice == '1':
                return 'basic'
            elif choice == '2':
                return 'intermediate'
            elif choice == '3':
                return None
            else:
                print("Invalid choice! Please try again.")

    def display_game_state(self):
        """Display current game state."""
        state = self.game.get_game_state()
        print("\n" + "-"*40)
        print(f"Level: {state['level'].title()}")
        print(f"Lives: {state['lives']}/{state['max_lives']}")
        print(f"Word/Phrase: {state['display']}")
        if state['guessed_letters']:
            letters = ', '.join(state['guessed_letters'])
            print(f"Guessed letters: {letters}")
        print("-"*40)

    def get_guess(self):
        """Get a guess from the user with timer."""
        print(f"\nYou have {self.game.time_limit} seconds to make a guess!")
        self.game.start_timer()

        try:
            guess = input("Enter a letter: ").strip()
            self.game.stop_timer()

            if self.game.is_time_up():
                print("Time's up! You lose a life.")
                return ""

            return guess
        except KeyboardInterrupt:
            self.game.stop_timer()
            return "quit"

    def play_game(self):
        """Main game loop."""
        while True:
            self.display_menu()
            level = self.get_level_choice()

            if level is None:
                print("Thanks for playing! Goodbye!")
                break

            self.game = HangmanGame(level)
            print(f"\nStarting {level.title()} Level!")
            print("Try to guess the word/phrase. You have 6 lives.")

            while not self.game.game_over:
                self.display_game_state()

                guess = self.get_guess()
                if guess.lower() == "quit":
                    print("Game quit by user.")
                    break

                if self.game.is_time_up():
                    if self.game.lives <= 0:
                        answer = self.game.answer
                        print(f"Game Over! The answer was: {answer}")
                        break
                    continue

                success, message = self.game.make_guess(guess)
                print(message)

            if hasattr(self.game, 'won') and self.game.won:
                print("\n🎉 Congratulations! You won! 🎉")

            play_again = input("\nPlay again? (y/n): ").strip().lower()
            if play_again != 'y':
                break

        print("Thanks for playing Hangman!")


if __name__ == "__main__":
    game_ui = HangmanGameUI()
    game_ui.play_game()
