opening = '''                /|  /|  ---------------------------
                ||__||  |         Learning         |
               /   O O\__         English          |
              /          \        Easily!!         |
             /      \     \                        |
            /   _    \     \ ----------------------
           /    |\____\     \      ||
          /     | | | |\____/      ||
         /       \| | | |/ |     __||
        /  /  \   -------  |_____| ||
       /   |   |           |       --|
       |   |   |           |_____  --|
       |  |_|_|_|          |     \----
       /\                  |
      / /\        |        /
     / /  |       |       |
 ___/ /   |       |       |
|____/    c_c_c_C/ \C_c_c_c'''

welcome = '''  (¯`·.¸¸.·´¯`·.¸¸.·´¯)
  ( \                 / )
 ( \ )               ( / )
( ) (    Welcome!!    ) ( )
 ( / )               ( \ )
  ( /                 \ )
   (_.·´¯`·.¸¸.·´¯`·.¸_)'''

welcome_back = '''  (¯`·.¸¸.·´¯`·.¸¸.·´¯)
  ( \                 / )
 ( \ )               ( / )
( ) (  Welcome back!! ) ( )
 ( / )               ( \ )
  ( /                 \ )
   (_.·´¯`·.¸¸.·´¯`·.¸_)'''

remote = '''           ⇓ After learning the meaning of the word ⇓
 -----------------------------------------------------------------
| Read the last words in English and its interpretation in Hebrew |
|    and vice versa, read in Hebrew and translate to English!     |
 -----------------------------------------------------------------'''


num = int(input("Enter a number: "))
small = num
large = num
while num / 100 < 1 or num / 100 > 10:

    num = int(input("Enter a number: "))
    if num < small:
        small = num
    if num > large:
        large = num
print(f"The largest number is {large}, the smallest number is {small}")