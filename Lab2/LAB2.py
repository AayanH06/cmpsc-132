# LAB2
# REMINDER: The work in this assignment must be your own original work and must be completed alone.

import math

# -------- SECTION 1
class Instructor:
    '''
        >>> t1= Instructor('John Doe')
        >>> t1.get_name()
        'John Doe'
        >>> t1.get_courses()
        []
        >>> t1.add_course('MATH140')
        >>> t1.get_courses()
        ['MATH140']
        >>> t1.add_course('STAT100')
        >>> t1.get_courses()
        ['MATH140', 'STAT100']
        >>> t1.add_course('STAT100')
        >>> t1.get_courses()
        ['MATH140', 'STAT100']
        >>> t1.remove_course('MATH141')
        >>> t1.get_courses()
        ['MATH140', 'STAT100']
        >>> t1.remove_course('MATH140')
        >>> t1.get_courses()
        ['STAT100']
    '''

    def __init__(self, name):
        self.name = name
        self.courses = []

    def get_name(self):
        return self.name
        

    def set_name(self, new_name):
        if new_name:
            self.name = new_name
        

    def get_courses(self):
        return self.courses

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
        
        
    def add_course(self,course):
        if course not in self.courses:
            self.courses.append(course)


# -------- SECTION 2      
class Pantry:
    """"
        >>> sara_pantry = Pantry()                
        >>> sara_pantry.stock_pantry('Bread', 2)
        'Pantry Stock for Bread: 2.0'
        >>> sara_pantry.stock_pantry('Cookies', 6) 
        'Pantry Stock for Cookies: 6.0'
        >>> sara_pantry.stock_pantry('Chocolate', 4) 
        'Pantry Stock for Chocolate: 4.0'
        >>> sara_pantry.stock_pantry('Pasta', 3)     
        'Pantry Stock for Pasta: 3.0'
        >>> sara_pantry
        I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 6.0, 'Chocolate': 4.0, 'Pasta': 3.0}
        >>> sara_pantry.get_item('Pasta', 2)     
        'You have 1.0 of Pasta left'
        >>> sara_pantry.get_item('Pasta', 6) 
        'Add Pasta to your shopping list!'
        >>> sara_pantry
        I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 6.0, 'Chocolate': 4.0, 'Pasta': 0.0}
        >>> ben_pantry = Pantry()                    
        >>> ben_pantry.stock_pantry('Cereal', 2)
        'Pantry Stock for Cereal: 2.0'
        >>> ben_pantry.stock_pantry('Noodles', 5) 
        'Pantry Stock for Noodles: 5.0'
        >>> ben_pantry.stock_pantry('Cookies', 9) 
        'Pantry Stock for Cookies: 9.0'
        >>> ben_pantry.stock_pantry('Cookies', 8) 
        'Pantry Stock for Cookies: 17.0'
        >>> ben_pantry.get_item('Pasta', 2)       
        "You don't have Pasta"
        >>> ben_pantry.get_item('Cookies', 2.5) 
        'You have 14.5 of Cookies left'
        >>> sara_pantry.transfer(ben_pantry, 'Cookies')
        >>> sara_pantry
        I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 20.5, 'Chocolate': 4.0, 'Pasta': 0.0}
        >>> ben_pantry.transfer(sara_pantry, 'Rice')
        >>> ben_pantry.transfer(sara_pantry, 'Pasta')
        >>> ben_pantry
        I am a Pantry object, my current stock is {'Cereal': 2.0, 'Noodles': 5.0, 'Cookies': 0.0}
        >>> ben_pantry.transfer(sara_pantry, 'Pasta')
        >>> ben_pantry
        I am a Pantry object, my current stock is {'Cereal': 2.0, 'Noodles': 5.0, 'Cookies': 0.0}
        >>> sara_pantry
        I am a Pantry object, my current stock is {'Bread': 2.0, 'Cookies': 20.5, 'Chocolate': 4.0, 'Pasta': 0.0}
    """

    def __init__(self):
        self.items = {}

    def __repr__(self):
        return f"I am a Pantry object, my current stock is {self.items}"

    def stock_pantry(self, item, qty):
        qty = float(qty)
        if item in self.items:
            self.items[item] += qty
        else:
            self.items[item] = qty
        return f"Pantry Stock for {item}: {self.items[item]}"

    def get_item(self, item, qty):
        qty = float(qty)
        if item not in self.items:
            return f"You don't have {item}"
        if self.items[item] >= qty:
            self.items[item] -= qty
            return f"You have {self.items[item]} of {item} left"
        else:
            self.items[item] = 0.0
            return f"Add {item} to your shopping list!"

    def transfer(self, other_pantry, item):
        if item in other_pantry.items and other_pantry.items[item] > 0:
            if item in self.items:
                self.items[item] += other_pantry.items[item]
            else:
                self.items[item] = other_pantry.items[item]
            other_pantry.items[item] = 0.0


# -------- SECTION 3
class Player:
    """
        >>> p1 = Player('Susy')
        >>> print(p1)
        No game records for Susy
        >>> p1.update_loss()
        >>> p1
        *Game records for Susy*
        Total games: 1
        Games won: 0
        Games lost: 1
        Best game: None
        >>> p1.update_win(5)
        >>> p1.update_win(2)
        >>> p1
        *Game records for Susy*
        Total games: 3
        Games won: 2
        Games lost: 1
        Best game: 2 attempts
    """
    def __init__(self, name):
        self.name = name
        self.total_games = 0
        self.wins = 0
        self.losses = 0
        self.best_game = None

    def update_win(self, att):
        self.wins += 1
        self.total_games += 1
        if self.best_game is None or att < self.best_game:
            self.best_game = att

    def update_loss(self):
        self.losses += 1
        self.total_games += 1

    def __str__(self):
        if self.total_games == 0:
            return f"No game records for {self.name}"
        result = f"*Game records for {self.name}*\n"
        result += f"Total games: {self.total_games}\n"
        result += f"Games won: {self.wins}\n"
        result += f"Games lost: {self.losses}\n"
        if self.best_game is not None:
            result += f"Best game: {self.best_game} attempts"
        else:
            result += "Best game: None"
        return result

    __repr__ = __str__

class Wordle:
    """
        >>> p1 = Player('Susy')
        >>> p2 = Player('Taylor')
        >>> w1 = Wordle(p1, 'water')
        >>> w2 = Wordle(p2, 'cloud')
        >>> w3 = Wordle(p1, 'jewel')
        >>> w1.play('camel')
        '_A_E_'
        >>> w1.play('ranes')
        'rA_E_'
        >>> w1.play('baner')
        '_A_ER'
        >>> w1.play('pacer')
        '_A_ER'
        >>> w1.play('water')
        'You won the game'
        >>> w1.play('rocks')
        'Game over'
        >>> w1.play('other')
        'Game over'
        >>> w3.play('beast')
        '_E___'
        >>> w3.play('peace')
        '_E__e'
        >>> w3.play('keeks')
        '_Ee__'
        >>> w3.play('jewel')
        'You won the game'
        >>> w2.play('classes')
        'Guess must be 5 letters long'
        >>> w2.play('cs132')
        'Guess must be all letters'
        >>> w2.play('audio')
        '_ud_o'
        >>> w2.play('kudos')
        '_udo_'
        >>> w2.play('would')
        '_oulD'
        >>> w2.play('bound')
        'The word was cloud'
        >>> w2.play('cloud')
        'Game over'
        >>> p1
        *Game records for Susy*
        Total games: 2
        Games won: 2
        Games lost: 0
        Best game: 4 attempts
        >>> p2
        *Game records for Taylor*
        Total games: 1
        Games won: 0
        Games lost: 1
        Best game: None
    """
    def __init__(self, player, word):
        self.player = player
        self.word = word.lower()
        self.attempts = 0
        self.max_attempts = 6
        self.won = False
        self.finished = False

    def process_guess(self, guess):
        guess = guess.lower()
        if len(guess) != 5:
            return "Guess must be 5 letters long"
        if not guess.isalpha():
            return "Guess must be all letters"

        feedback = ""
        for i in range(5):
            if guess[i] == self.word[i]:
                feedback += guess[i].upper()
            elif guess[i] in self.word:
                feedback += guess[i].lower()
            else:
                feedback += "_"
        return feedback

    def play(self, guess):
        if self.finished:
            return "Game over"

        guess = guess.lower()
        if len(guess) != 5:
            return "Guess must be 5 letters long"
        if not guess.isalpha():
            return "Guess must be all letters"

        if guess == self.word:
            self.attempts += 1
            self.player.update_win(self.attempts)
            self.won = True
            self.finished = True
            return "You won the game"

        self.attempts += 1

        if self.attempts == self.max_attempts:
            self.player.update_loss()
            self.finished = True
            return f"The word was {self.word}"

        # Generate feedback
        feedback = ""
        for i in range(5):
            if guess[i] == self.word[i]:
                feedback += guess[i].upper()
            elif guess[i] in self.word:
                feedback += guess[i].lower()
            else:
                feedback += "_"
        return feedback




       



# -------- SECTION 4
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line: 
    ''' 
        >>> p1 = Point2D(-7, -9)
        >>> p2 = Point2D(1, 5.6)
        >>> line1 = Line(p1, p2)
        >>> line1.getDistance
        16.648
        >>> line1.getSlope
        1.825
        >>> line1
        y = 1.825x + 3.775
        >>> line2 = line1*4
        >>> line2.getDistance
        66.592
        >>> line2.getSlope
        1.825
        >>> line2
        y = 1.825x + 15.1
        >>> line1
        y = 1.825x + 3.775
        >>> line3 = line1*4
        >>> line3
        y = 1.825x + 15.1
        >>> line5=Line(Point2D(6,48),Point2D(9,21))
        >>> line5
        y = -9.0x + 102.0
        >>> Point2D(45,3) in line5
        False
        >>> Point2D(34,-204) in line5
        True
        >>> line6=Line(Point2D(2,6), Point2D(2,3))
        >>> line6.getDistance
        3.0
        >>> line6.getSlope
        inf
        >>> isinstance(line6.getSlope, float)
        True
        >>> line6
        Undefined
        >>> line7=Line(Point2D(6,5), Point2D(9,5))
        >>> line7.getSlope
        0.0
        >>> line7
        y = 5.0
        >>> Point2D(9,5) in line7
        True
        >>> Point2D(89,5) in line7
        True
        >>> Point2D(12,8) in line7
        False
        >>> (9,5) in line7
        False
    '''
    def __init__(self, point1, point2):
        self.p1 = point1
        self.p2 = point2

    @property
    def getDistance(self):
        dx = self.p2.x - self.p1.x
        dy = self.p2.y - self.p1.y
        return round(math.sqrt(dx**2 + dy**2), 3)

    @property
    def getSlope(self):
        dx = self.p2.x - self.p1.x
        if dx == 0:
            return float('inf')
        dy = self.p2.y - self.p1.y
        return round(dy / dx, 3)

    def __str__(self):
        slope = self.getSlope
        if slope == float('inf'):
            return "Undefined"
        elif slope == 0:
            return f"y = {round(self.p1.y, 3)}"
        else:
            b = self.p1.y - slope * self.p1.x
            return f"y = {slope}x + {round(b, 3)}"

    __repr__ = __str__

    def __mul__(self, other):
        if not isinstance(other, int):
            return None
        new_p1 = Point2D(self.p1.x * other, self.p1.y * other)
        new_p2 = Point2D(self.p2.x * other, self.p2.y * other)
        return Line(new_p1, new_p2)

    def __contains__(self, point):
        if not isinstance(point, Point2D):
            return False
        slope = self.getSlope
        if slope == float('inf'):
            return False
        expected_y = slope * point.x + (self.p1.y - slope * self.p1.x)
        return math.isclose(point.y, expected_y)

def run_tests():
    import doctest

    # Run tests in all docstrings
    doctest.testmod(verbose=False)
    
    # Run tests per function - Uncomment the next line to run doctest by function. Replace Pantry with the name of the class you want to test
    #doctest.run_docstring_examples(Pantry, globals(), name='LAB2',verbose=True)

if __name__ == "__main__":
    run_tests()