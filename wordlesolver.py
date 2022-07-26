from operator import contains
import wordlist

class WordleSolver():
    
    def __init__(self):
        self.green_letters = input('Write pattern of known ("Green") letters in the following format: P_A_E ')
        self.yellow_letters = input('List any other known letters ("Yellow")')
        self.gray_letters = input('List any gray letters - letters known to not be in the clue. Separate the letteres by comma (e.g. a,e,t,y,etc.)')
        self.words_guessed = []
        self.five_letter_words = self.wordle_clues()
        self.play_turn()
        print(self.green_letters)
        print(self.yellow_letters)
        print(self.words_guessed)
        print(self.possible_matches())

    def wordle_clues(self):
        #Generates a list of words that have exactly five letters
        w = wordlist.Wordlist()
        return w.five_letter_words()

    def possible_matches(self):
        #Finds a list of possible matches from the five_letter_words list, based on the known letters.
        wordle_matches = []
        w = wordlist.Wordlist()
        #A list of possible words based on known green letters
        green_letter_wordlist = w.possible_matches(self.green_letters)
        #Reduce that list to only words that contain the known yellow letters somewhere in those words.
        #   Convert list of yellow letters into a list of letters
        yellow_letters = list(filter(lambda x: (x.isalpha()), self.yellow_letters))
        #   Make list of yellow letters lowercase
        gray_letters = list(filter(lambda x: (x.isalpha()), self.gray_letters))
        yl = list(map(lambda l: l.lower(), yellow_letters))
        gl = list(map(lambda l: l.lower(), gray_letters))
        #Return a list of possible matches, given known yellow letters and green letters
        matches = list(filter(lambda w: all(l in w for l in yl), green_letter_wordlist))
        #Further refine list of possible matches, eliminating any words that contain letters known to not be in the clue
        matches = list(filter(lambda w: all(l not in w for l in gl), matches))
        #Filter out any words that have already been guessed:
        guessed_words = [w.lower() for w in self.words_guessed]
        result = []
        for word in matches:
            if word not in guessed_words:
                result.append(word)
        return result
    

    def play_turn(self):
        print(f'Green letters: {self.green_letters}')
        print(f'Yellow letters: {self.yellow_letters}')
        choice = input('Press 1 to guess a word, press 2 to see possible results, 3 to update Green letters, and 4 to update Yellow Letters.')
        if choice == '1':
            guessed_word =input('Type a word that you have guessed already: ')
            self.words_guessed.append(guessed_word)
            print(self.words_guessed)
            self.play_turn()
        if choice == '2':
            print(f'These are the possible words: {self.possible_matches()}')
            self.play_turn()
        if choice == '3':
            green_letters = input('Write pattern of known ("Green") letters in the following format: P_A_E ')
            self.green_letters = green_letters
            print(self.green_letters)
            self.play_turn
        if choice == '4':
            yellow_letters = input('List any other known letters ("Yellow")')
            self.yellow_letters = yellow_letters
            print(self.yellow_letters)
            self.play_turn

        

        
w = WordleSolver()