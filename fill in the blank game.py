""" MADLIBS game - a fill in the blank project game"""

easy_game = "A common first thing to do while learning a language is display \n'Hello __1__!' In __2__ this is particularly easy; all you have to do is \ntype in: __3__ 'Hello __1__!'\n\nOf course, that isn't a very useful thing to do. However, it is an \nexample of how to output to the user using the __3__ command, and \nproduces a program which does something, so it is useful in that capacity.  \n\nIt may seem a bit odd to do something in a Turing complete language that \ncan be done even more easily with an __4__ file in a browser, but it\'s \na step in learning __2__ syntax, and that's really its purpose.\n"
easy_answer = ['world',
             'Python',
             'print',
             'HTML']
medium_game = "A __1__ is created with the def keyword. We can specify the inputs a __1__ \ntakes by adding __2__ separated by commas between the parentheses. \n__1__s by default returns __3__ if you don't specify the value to return. \n__2__ can be standard data types such as string, integer, dictionary, list, \ntuple, and __4__ or can be more complicated such as objects and lambda functions.\n"
medium_answer = ['function',
                 'arguments',
                 'None',
                 'list']
hard_game = "When we create a __1__, certain __2__s are automatically \ngenerated for us if we don't make them manually. These contain multiple \nunderscores before and after the word defining them. When we write \na __1__, we always include at least the __3__ __2__, defining variables \nfor when __4__s of the __1__ get made. Additionally, we generally \nwant to create a __5__ __2__, which will allow a string representation \nof the method to be viewed by other developers.\n\nWe can also create binary operators, like __6__ and __7__, which \nallow + and - to be used by __4__s of the __1__.  Similarly, __8__, \n__9__, and __10__ allow __4__s of the __1__ to be compared \n(with <, >, and ==).\n"
hard_answer = ['class',
            'method',
            '__init__',
            'instance',
            '__repr__',
            '__add__',
            '__sub__',
            '__lt__',
            '__gt__',
            '__eq__']

def start():
    """The player need to choose the correct difficulty option. If the input is invalid,
    the player is prompted to choose again"""
    print "Welcome to Madlibs game. This is a fill in the blank game."
    while True:
        level = raw_input("Please select the difficulty: easy/medium/hard ").lower()
        if level == "easy" or level == "medium" or level == "hard":
            print "You have chosen "+level.upper()+" level!\n"
            return level
        else:
            print "That's not in the option."

def guesses():
    """This function is to get the maximum number of guesses for the whole quiz"""
    print "How many guesses do you need for these questions?\n"
    while True:
        try:
            max_guess = int(raw_input("Please enter in positive integer number: "))
            if max_guess < 1:
                print "You need at least one guess!"
            else:
                print "\nYou have "+str(max_guess)+" chances to answer the questions below.\n"
                max_guess = max_guess - 1
                return max_guess                
        except:
            print "That is not an integer!"
            
def get_level(level):
    """This function input is the difficulty choice. The output are the question and answer"""
    if level == "easy":
        return (easy_game, easy_answer)
    if level == "medium":
        return (medium_game, medium_answer)
    if level == "hard":
        return (hard_game, hard_answer)

def play(answer, question, attempts_left):
    """This function show again the question if the answer is wrong. It fills the correct answer
        in the blank after the player answers correctly. 'a' is the counter for the answer list"""
    a = 0
    while a < len(answer) and attempts_left >= 0:
        print "The current paragraph reads as such:\n\n"+question
        user_input = raw_input("What should be substituted in for "+str(a+1)+'? ').lower()
        if user_input == answer[a].lower():
            print "\nCorrect! The answer is '"+answer[a]+"'.\n"
            question = question.replace('__'+str(a+1)+'__', str(answer[a]))
            a += 1
            if a == len(answer):
                print question+"\nCongratulations! You have finished the quiz!"
        else:
            if attempts_left > 1:
                print"\nWrong! Please try again to answer the question number "+str(a+1)+". You have "+str(attempts_left)+" tries left!\n"
            elif attempts_left == 1:
                print "\nWrong! Think carefully, this time you only have 1 try left!\n"
            else:
                print "You do not have more guess! Game over!"
            attempts_left -= 1

#Start the game#
level = start()
max_guess = guesses()
question, answer = get_level(level)
play(answer, question, max_guess)
