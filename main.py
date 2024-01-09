import list_word
import ascii
from learning_words import LearningWords, BackWords
from file import File

num = 0
new_words = []

# The opening of the program
print(f"\n{ascii.opening}")

# Continuation of the program or from the beginning.
run_program = input("\nFeeling ready? to start from the beginning press 's'"
                    "\nto continue from the stopping point, Press Enter!: ")

while True:
    # Choosing a dictionary to study.
    if run_program.casefold() == "s":
        print(f"\n\n{ascii.welcome}")
        choose_list = input("\n\nFor the '1,000' useful words write 'w'"
                            "\nfor the '2,000' useful words write 't'"
                            "\nfor the 'high-tech' useful words write 'h': ")
        break
    elif run_program == "":
        print(f"\n{ascii.welcome_back}")

        # Opening the data and continuing the practice from the last end point.
        files = File(number=None, new_words=None, choose=None)
        files.open_file()
        choose_list = files.choose
        new_words = files.new_words
        num = files.number

        # When the current practice day is different from the previous practice day,
        # the program repeats the words that require repetition.
        if files.old_time != str(files.new_time) and len(files.new_words) > 0:
            learn = BackWords(files.new_words, num, new_words, choose_list)
            learn.new_word()
        break
    else:
        run_program = input("\nPlease enter 's' or press Enter: ")

# The program selects the list that the user selected.
while True:
    if choose_list.casefold() == "w":
        learn = LearningWords(list_word.words, num, new_words, choose_list)
        break
    elif choose_list.casefold() == "h":
        learn = LearningWords(list_word.high_tech, num, new_words, choose_list)
        break
    elif choose_list.casefold() == "t":
        learn = LearningWords(list_word.two_thousand_words, num, new_words, choose_list)
        break
    else:
        choose_list = input("\nPlease enter w / h / t : ")

# Learning the new words from the selected list.
learn.new_word()

# End of the program
if len(new_words) != 0:
    print("amm.. you're almost done with the program.. come back tomorrow to repeat your last words..")
else:
    print("Well done!! You have successfully learned all the words!!!!👏🏼👏🏼👏🏼👏🏼👏🏼👏🏼👏🏼👏🏼👏🏼👏🏼")
