chance = 5
answer = 'secret'  # I would like to make it to random
myAnswer = ['_']*len(answer)


print("Let's play Hangman game!")

while chance > 0:
    print(*myAnswer)
    guesse = input()
    guesse = guesse.lower()
    # Chack the letter is one, Alphabet and duplicated
    if len(guesse) == 1:
        if (ord(guesse) >= ord('a')) and (ord(guesse) <= ord('z')):
            hasEmpty = False
            found = False
            # Check input is same with answer and change it
            for i, char in enumerate(answer):
                if guesse == char:
                    found = True
                    if(myAnswer[i]) == guesse:
                        print("You already entered it")
                        break
                    else:
                        myAnswer[i] = guesse

            # Subtract only when myAnswer is wrong
            if found == False:
                chance -= 1
                print("There is no '{}''".format(guesse))
            # Check if there's no more '_' in myAnswer and end the game
            for char in myAnswer:
                if char == '_':
                    hasEmpty = True
            if hasEmpty == False:
                print(*myAnswer)
                print("You win!")
                break
        else:
            print("Please enter Alphabet")
    else:
        print("Please enter one letter")
    print("You have {} chances".format(chance))
if chance == 0 :
    print("You lost! , It was'{}' ".format(answer))
