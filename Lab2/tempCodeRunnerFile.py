def play(self, guess):
        if self.finished:
            return "Game over"

        result = self.process_guess(guess)
        if result.startswith("Guess must"):
            return result

        self.attempts += 1

        if guess.lower() == self.word:
            self.player.update_win(self.attempts)
            self.won = True
            self.finished = True
            return "You won the game"

        if self.attempts >= self.max_attempts:
            self.player.update_loss()
            self.finished = True
            return f"The word was {self.word}"

        return result