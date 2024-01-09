# Notifications to the user during the program.
class Messages:
    def __init__(self):
        self.counter = 1

    # Success message every time you progress 20 words from the list.
    def progress_message(self, numbers):
        if numbers > 0 and numbers % 20 == 0:
            print(f"👏🏼👏🏼👏🏼 You already know '{numbers}' words from the list!!! 👏🏼👏🏼👏🏼")

    # Success message for every learning of 5 new words.
    def success_message(self, old_num):
        if old_num > self.counter:
            self.counter = old_num
        if self.counter % 5 == 0:
            print(f"👏🏼👏🏼👏🏼 Wow!! Today you already learned '{old_num}' new words!!! 👏🏼👏🏼👏🏼")
            self.counter += 1

    # Statistics on program progress for the user.
    def statistic(self, old_num, numbers, length_list):
        words_left = length_list - numbers
        percentage = round((numbers - old_num) / length_list * 100)
        print(f"\n               statistics"
              f"\n-------------------------------------------"
              f"\n Words you have already learned: {numbers}"
              f"\n Words still left: {words_left}"
              f"\n Percentage of words you already know: {percentage}%"
              f"\n New words you learned today: {old_num}"
              f"\n-------------------------------------------\n")
