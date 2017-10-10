"""Mad-Libs quiz game. This is a Bible Quiz."""

easy = ["1. Jesus' parents lived in the city of ____ ","2. God created plant in day ____ ",
        "3. There are ____ people in Noah's ark ",
        "4. Jesus disciple who was given the keys of the kingdom of heaven is ____ "]
easy_answer = ["Nazareth", "3", "8", "Peter"]

medium = ["1. Who is the name of the prophet that warned David of his adultery sin? ",
          "2. Moses is from which Israel tribe? ",
          "3. Who asked: 'How can someone be born when they are old?'? ",
          "4. How many brothers does David have? "]
med_answer = ["Nathan", "Levites", "Nicodemus", "7"]

hard = ["1. Who is the name of the first judge of Israel? ",
        "2. God ask Noah to make ark from ____ wood. ",
        "3. Blessed are those who mourn, for they shall be ____ ",
        "4. Who is the apostle that was killed by King Herod? "]
hard_answer = ["Othniel", "gopher", "comforted", "James"]

question = [easy, medium, hard]
ans = [easy_answer, med_answer, hard_answer]
"""question and ans are the difficulty level for the question and the answer"""

def show_question(welcome,a):
    """This function is to show the question. 'a' is counter.
    If the answer is correct (True), it goes to the next question."""
    level = int(welcome) - 1
    """level is for difficulty level. It is in integer because list indices must be integer."""
    while a < len(question[level]):
        while True:
            answer = raw_input(question[level][a]).lower()
            if check(welcome,answer,a) == True:
                break   
        a += 1
               
def check(welcome,answer,a):
    """This function is to check whether the answer from show_question is inside the answer list."""
    level = int(welcome) - 1
    while answer == ans[level][a].lower():
        print "Correct! The answer is '"+ans[level][a]+"'"
        return True
    if answer == "give up":
        print "Do you want to give up? The answer is '"+ans[level][a]+"'"
        return True
    else:
        print "Wrong! Please try different answer. Type 'give up' if you want to give up."
        return False
    
print "Welcome to the Bible Quiz. How much do you know about the Bible?"
while True:
    welcome = raw_input("Please type in the difficulty level: 1/2/3 (1 is the easiest) ")
    if welcome == "1" or welcome == "2" or  welcome == "3":
        break

print "Let's get started. Please answer the next question."
show_question(welcome,0)
print("Awesome, you have completed the game!")
