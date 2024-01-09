import webbrowser
import ascii
from messages import Messages
from file import File


# The main class for learning words and their translation.
class LearningWords:

    def __init__(self, words_list, number, new_words, choose_list):
        self.words_list = words_list
        self.number = number
        self.new_words = new_words
        self.choose_list = choose_list
        self.message = Messages()

    # A method that goes through the new words in the list and checks if the user knows the words.
    def new_word(self):
        while True:
            rev = True
            for i in range(self.number, len(self.words_list)):
                if not rev:
                    break
                files = File(self.number, self.new_words, self.choose_list)
                time_update = True
                files.save_file(time_update)
                self.message.progress_message(self.number)
                self.number += 1
                know = input(f"\nYour new word is:\n\n{self.number}. '{self.words_list[i]}'"
                             "\n\nDo you know this word? If yes press Enter. If you are not sure, press 'n'.\n\n")
                while True:
                    if know == "":
                        print("\nGreat!\n")
                        break
                    elif know.casefold() == "s":
                        self.message.statistic(len(self.new_words), files.number, len(self.words_list))
                        self.number = i - 0
                        rev = False
                        break
                    elif know.casefold() == "n":
                        self.chak_translation(self.words_list[i])
                        break
                    # When the user presses 'r', the program will go back a word in the list.
                    elif know.casefold() == "r" and self.number > 1:
                        self.number = i - 1
                        rev = False
                        break
                    else:
                        know = input("Please, press n / s / r / Enter! ")
                self.message.success_message(len(self.new_words))
            if self.number == len(self.words_list):
                break

    # The method translates the new word.
    def chak_translation(self, current_word):
        chak = input("Write the word and you can get its translation: ")
        while True:
            if chak.casefold() == current_word.casefold():
                break
            else:
                chak = input("Spell the word correctly again: ")
        webbrowser.open(f"https://translate.google.co.il/?hl=iw&sl=en&tl=iw&text={current_word}%0A&op=translate")
        self.memorization(current_word)

    # The method displays the new words the user is learning, for memorization purposes.
    def memorization(self, current_word):
        self.new_words.append(current_word)
        print(f"___________________________________________________________\n\n\n\n\n\n\n\n\n\n{ascii.remote}"
              f"\n\n\nThe last words: >>>>>----------------------->   '{', '.join(self.new_words[-3:])}'")
        if len(self.new_words) >= 7:
            print("And also the old word: >>>>----------------->   '" + self.new_words[-7] + "'")
        print(f"\n\n           If you forgot the meaning of one of the words,"
              f"\nyou can write it down here and get its translation, Otherwise press Enter"
              f"\n      ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓")
        self.free_chak_translation()
        print("\nExcellent! Now that you have memorized the word well, you can move on to the next word!")

    # The method allows the user to translate words freely.
    def free_chak_translation(self):
        translate = input()
        while True:
            if translate == "":
                break
            else:
                webbrowser.open(f"https://translate.google.co.il/?hl=iw&sl=en&tl=iw&text={translate}%0A&op=translate")
            translate = input("You can check another word again. If you wish to continue press Enter ")


# The purpose of the son class is to practice old words, and to make sure that the user does know them.
class BackWords(LearningWords):
    def __init__(self, words_list, number, new_words, choose_list):
        super().__init__(words_list, number, new_words, choose_list)
        self.old_word = []
        self.number = 0
        self.number2 = self.number
        self.num = number
        self.first = 0
        self.last = 1

    # The method goes through the words that the user did not know the previous time,
    # and checks if he already knows them.
    def new_word(self):
        print(f"\n\n\nFirst, we'll go over the: '{len(self.new_words)}' old words you had trouble with,"
              f"\nand then we'll go back to the list again to continue with the new words.")
        self.old_word = len(self.new_words)
        while True:
            rev = True
            for i in range(self.number, self.old_word):
                if not rev:
                    break
                files = File(self.num, self.new_words, self.choose_list)
                time_update = False
                files.save_file(time_update)
                self.number += 1
                self.number2 += 1
                while True:
                    know = input(f"\nYour new word is:\n\n{self.number2}. '{self.new_words[i]}'"
                                 "\n\nDo you know this word? If yes press Enter. If you are not sure, press 'n'.\n\n")
                    if know == "":
                        print("\nGreat!\n")
                        # Deleting words that the user already knows from the list of new words.
                        files.new_words.remove(self.new_words[i])
                        self.old_word -= 1
                        self.number -= 1
                        rev = False
                        break
                    elif know.casefold() == "n":
                        self.chak_translation(self.new_words[i])
                        break
                    else:
                        print("Please, press 'n' or Enter!")
            if self.number >= len(self.new_words):
                break
        print("\n\nExcellent! Now we will return to the list!\n")

    # As in the parent class, but in this method the words appear from the beginning of the list to the end.
    def memorization(self, current_word):
        print(f"___________________________________________________________\n\n\n\n\n\n\n\n\n\n{ascii.remote}"
              f"\n\n\nThe last words: >>>>>-------------------->   '{', '.join(self.new_words[self.first:self.last])}'")
        self.last += 1
        if self.last > 3:
            self.first += 1
        print(f"\n\n           If you forgot the meaning of one of the words,"
              f"\nyou can write it down here and get its translation, Otherwise press Enter"
              f"\n      ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓ ⇓")
        self.free_chak_translation()
        print("\nExcellent! Now that you have memorized the word well, you can move on to the next word!")
