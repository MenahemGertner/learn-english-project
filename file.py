from datetime import date


# The purpose of the class is to deal with saving and reading data,
# for the purpose of saving the user's location in the program.
class File:
    def __init__(self, number, new_words, choose):
        self.number = number
        self.new_words = new_words
        self.choose = choose
        self.old_time = None
        self.new_time = None

    # Saving user location data in the program.
    def save_file(self, time_update):
        if time_update:
            time = date.today()
        else:
            time = None
        file_list = [self.number, self.new_words, time, self.choose]
        with open("save.txt", mode="w") as file:
            for item in file_list:
                file.write(str(item) + "\n")

    # Opening and reading user location data in the program.
    def open_file(self):
        with open("save.txt", mode="r") as file:
            file_list = []
            for line in file:
                file_list.append(line.strip())
        self.number = int(file_list[0])
        self.new_words = eval(file_list[1])
        self.old_time = file_list[2]
        self.choose = file_list[3]
        self.new_time = date.today()
