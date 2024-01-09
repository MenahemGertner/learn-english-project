'''
A program for learning useful words in English.

The purpose of the program is to teach useful words in English or specifically useful words in high-tech.
The program allows the user to learn continuously.
That is to open the program again and continue the study from the stopping point.

The plan in stages:

A. The program will ask the user if he wants to continue from the point where he left the program for the last time,
   or if he wants to start from the beginning. When the user chooses to start the program begins:

    a. The user must select the list he would like to study.
       the 1,000 or 2,000 most useful words in English or 100 useful words in high-tech.

    b. After selecting the list, the program will start to go word by word and ask the user if he knows the word?
       The user can choose one of the following options:

        1. Yes. The program will move to the next word in the list.
        2. No. The program will move to the next stage of memorizing the word.
        3. The user can go back a step in the list by pressing 'r'.
        4. User can get statistics of his progress by pressing 's'.

    c. When the user does not know the word:
       the user is asked to write the word and then get its translation in the 'Google Translate' fields.

    d. After the translation:
       the last word or up to the last 3 words will appear again and the user will be asked to memorize them.
        2. Also, after 7 new words the first word will appear again for another repeat.

    e. The program will allow the user to re-translate freely any word he chooses by 'Google Translate'.

    f. The program will save the user's data for the purpose of continuing the program at a later date.

    g. Progress messages:
        1. At every progress of 20 new words, the program will print a progress message.
        2. Every time you learn 5 new words, the program will print a progress message.

B. When the user has exited the program and wants to continue from the point where he stopped the program:

    a. The program will open the saved progress data of the user.

    b. The program will check whether the user returned to the program that day.
       If so, the program will return to the list of words from the point where the user left the program.
       if not:

    c. The program will repeat all the words that the user did not know in the previous use
       and ask him again if he already knows these words:
        1. Yes. The word will be deleted from the list.
           (If the user exits the program and logs in again, the program will not display the same word again)
        2. No. The word will remain in the list for further memorization.

    d. As with new words, here too, the user will have to write the word and receive its translation,
       again up to the last 3 words that he marked that he does not know will appear to the user,
       and the user will also be able to translate words freely using 'Google Translate'.

    e. After completing the transition over all the old words,
       the program will return to the original list for further study,
       and the difficult words will be saved for further memorization.
'''