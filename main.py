#due to the nature of random numbers, without using the random module
#  we can only produce pseudo-randomic numbers:
# therefore we import the corresponding random module
from random import randint

def main():
    lottery = []
    #we then initiate the loop until the lottery list reaches 6
    while len(lottery) < 6:
        #we assign a random number between the specified range to the variable rand
        rand = randint(1, 49)
        #here we state a shorthand condition in which if the number
        # is not in the list it should be added, otherwiseremoved from the list
        lottery.append(rand) if rand not in lottery else lottery.remove(rand)
    #when the loop has finished the program should return the list
    return lottery

 #the main function is printed w\o the brackets
if __name__ == '__main__':
    print(str(main()).strip('[]'))
