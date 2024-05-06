import random


class HMPlayer:
    """This is a generic player for the Hangman game."""
    def __init__(self, name: str) -> None:
        self.name = name
        self.lives = 5
        self.score = 0  
    
    def propose_letter(self) -> str:
        """To be reimplemented in derived classes."""
        print("WARNING! To be reimplemented in derived classes")
        return ""
    
    def __str__(self) -> str:
        return "{} has {} lives and {} points".format(self.name, self.lives, self.score)
    
    def __lt__(self, other):
        return self.score < other.score
    
    def __gt__(self, other):
        return self.score > other.score


class HumanPlayer(HMPlayer):
    """This is a human player for the Hangman game."""
    def __init__(self, name: str) -> None:
        super().__init__(name)

    def propose_letter(self) -> str:
        
        letter = input("Please propose a letter: ")
        while len(letter) != 1:
            letter = input("Please propose a single letter: ")
        return letter

class ComputerPlayer(HMPlayer):
    """This is a computer player for the Hangman game."""
    def __init__(self, name: str) -> None:
        super().__init__(name + " (computer)")
        self.proposed_letters = []  

    def propose_letter(self) -> str:
        
        letter = random.choice("abcdefghijklmnopqrstuvwxyz")
        while letter in self.proposed_letters:
            letter = random.choice("abcdefghijklmnopqrstuvwxyz")
        self.proposed_letters.append(letter)
        return letter


class Hangman:
    def __init__(self, players: list):
        self.word = random.choice(["dog", "cat", "house", "girona", "spain"]).lower()
        self.players = players
        self.guessed_letters = []
    
    def display_word(self) -> str:
        
        display = ""
        for letter in self.word:
            if letter in self.guessed_letters:
                display += letter
            else:
                display += "_"
        return display
    
    def play(self):
        for player in self.players:
            while player.lives > 0 and "_" in self.display_word():
                self.turn(player)

            if "_" not in self.display_word():
               
                print("....................................")
                player.score += 10  
            else:
                
                print("Sorry {}, you lose!".format(player.name))
                print("The word was {}".format(self.word))
        
       
        scores = [player.score for player in self.players]
        #winner = self.players[scores.index(max(scores))]
        #loser = self.players[scores.index(min(scores))]

        lives = [player.lives for player in self.players]
        winner1 = self.players[lives.index(max(lives))]
        loser2 = self.players[lives.index(min(lives))]

        
        print("The player that has won the game is {}".format(winner1))
        print("The player that has lost the game is {}".format(loser2))

    def turn(self, player: HMPlayer):
        
        print("Player {}. Word {}".format(player.name, self.display_word()))
        l = player.propose_letter()
        print("Player {} proposes letter {}".format(player.name, l))

        if l not in self.word:
           
            print("Bad guess!\n")
            player.score -= 0.5
            player.lives -= 1
        else:
            if l not in self.guessed_letters:
                
                self.guessed_letters.append(l)
                player.score += 1  
            else:
                print("Letter already guessed!")


human_player = HumanPlayer("Salim")
computer_player = ComputerPlayer("Alain")

game = Hangman([human_player, computer_player])
game.play()
