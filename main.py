TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]
registred_users = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}
user_name = input("username: ")
password = input("password: ")
print("-"*len("Enter a number btw. 1 and 3 to select: 1"))
if user_name in registred_users:
    if registred_users[user_name] == password:
        print(f"Welcome to app, {user_name}\nWe have {len(TEXTS)} text to be analyzed.")
    else:
        print("unregistered user, terminating the program..")
        exit()
print("-"*len("Enter a number btw. 1 and 3 to select: 1"))
text_choise = (input(f"Enter a number btw. 1 and {len(TEXTS)} to select: "))
if not text_choise.isdigit():
    print("You did not enter a number. Terminating the program..")
    exit()
if not text_choise in range(1, len(TEXTS)):
    print(f"You did not enter a number btw. 1 and {len(TEXTS)}. Terminating the program..") 
    exit()       
choosen_text = TEXTS[int(text_choise)-1]

