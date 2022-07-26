import re

class Wordlist:

    def __init__(self):
        self.words = []
        with open('words.txt', 'r') as f:
            words = [line.strip() for line in f]
            for word in words:
                if '\"' not in word:
                    self.words.append(word)

    def five_letter_words(self):
        #Returns a list of possible Wordle Clues - those with exactly five letters
        five_letter_words = []
        for word in self.words:
            if len(word) == 5:
                five_letter_words.append(word)
        return five_letter_words

    def same_length_as(self,inputword):
        #Returns a list of words of the same length as the input word
        possible_length_words = []
        for word in self.words:
            if len(inputword) == len(word):
                possible_length_words.append(word)
        return possible_length_words

    def possible_matches(self,word):
        #returns a list of possible matches for a word with blanks and known letters.
        #Word Example: possible_matches('m__ic') = ['magic', 'manic', 'medic', 'mimic', 'mimic', 'music']
        testword = ''
        word = word.lower()
        for letter in word:
            if letter.isalpha():
                testword += letter
            else:
                testword += '.'

        possible_words = ''
        words_of_same_length = self.same_length_as(testword)
        for wrd in words_of_same_length:
            possible_words += f'{wrd}'
        wordlist = re.findall(f"{testword}", possible_words)
        return wordlist

    def find_words_with_letter(self,wordlist,letter):
        #Returns a list of words containing a particular letter, takes a list of words and a letter. If the word has that letter, add it to the list.
        matching_wordlist = []
        for word in wordlist:
            if letter in word:
                matching_wordlist.append(word)
        return matching_wordlist

    def test_wordlist(self,wordlist):
        tested_wordlist = []
        for word in wordlist:
            number_of_matches = len(self.possible_matches(word))
            tested_wordlist.append(number_of_matches)
        return tested_wordlist

    def isworking(self):
        print('it is working')



#list = Wordlist()
#sample_wordlist = ['This','is','a','sample','example']
#words_with_x = list.find_words_with_letter(sample_wordlist,'x')
#words_with_s = list.find_words_with_letter(sample_wordlist,'s')
#print(words_with_x) #['example']
#print(words_with_s) #['This', 'is', 'sample']
#m__ic_matches = list.possible_matches('m__ic')
#print(m__ic_matches)
#test_wordlist = list.test_wordlist(['m__ic', 'm_me___', '_re', 'm__ic'])
#print(test_wordlist) #[6, 4, 12, 6]
