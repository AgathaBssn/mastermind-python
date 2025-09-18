COLORS = ['R', 'G', 'B', 'Y', 'P', 'W']
NB_TRY = 12
GUESS_LENGHT = 4
#Drawing of 4 colors for the round
def init_colors():
    import random
    soluce = []
    for i in range(GUESS_LENGHT):
        soluce.append(random.choice(COLORS))
    return soluce

def reminder_color():
     print("Colors are R, G, B, Y, P , W")

#Transform the user input in tab
def split_colors(input_str):
     tab_input = []
     for letter in input_str:
          tab_input.append(letter)
     return tab_input

#Get a valid answer from the player
def ask_color():
    while True:
        try:
            guess = input(f"Submit {GUESS_LENGHT} colors : ")

            #check if there are  characters
            if len(guess) != GUESS_LENGHT :
                raise TypeError("Wrong length")
            
            guess = split_colors(guess)

            #check valid input
            for color in guess :
                if color not in COLORS:
                    raise ValueError("Invalid input")
                
            #all good
            return guess
        # if player kill program
        except KeyboardInterrupt:
                print("\nInterruption du programme.")
                exit()
        except TypeError:
            print("Write your answer in the format : YBRW")
        except ValueError:
            reminder_color()

def check_guess(soluce, player_input, found):
    # init count
    right = 0
    wplace = 0

    # well placed
    soluce_rest = []
    input_rest = []
    for i in range(len(soluce)):
        if soluce[i] == player_input[i]:
            right += 1
        else:
            #keep value to count missed place
            soluce_rest.append(soluce[i])
            input_rest.append(player_input[i])

    
    for color in input_rest:
        if color in soluce_rest:
            wplace += 1
            #remove match in soluce list to avoid double
            soluce_rest.remove(color)

    print(f"Right color and position: {right}, correct color wrong position: {wplace}")

    if right == len(soluce):
        found = False

    return found

def round() -> bool:
    soluce = init_colors()
    turn = 1
    print(soluce)
    reminder_color()
    playing = True
    while playing and turn <= NB_TRY:
        print(f"Turn number : {turn}")
        guess = ask_color()
        playing = check_guess(soluce, guess, playing)
        turn += 1
    if playing:
        win = False
        print("You loose")
    else:
        win = True
        print("Congrats")
    return win

def update_score(current_score, current_nbgames):
    f = open('scores', 'r', encoding="utf-8")
    #first line is nbgames in total
    total_nbgames = int(f.readline())
    #second is score
    total_score =  int(f.readline())
    f.close()

    total_nbgames += current_nbgames
    total_score += current_score

    f = open('scores', 'w', encoding="utf-8")
    f.write(f"{total_nbgames}\n{total_score}\n")
    f.close()





def menu():
    var_score = 0
    var_nbgames = 0
    while True :
        try :
            answer = input("What do you want to do : \n" \
            "   1 - Play \n"
            "   2 - Leave \n"
            "   3 - Score \n")
            if answer == str("1"):
                score = round()
                var_nbgames += 1
                if score :
                    var_score += 1
            elif answer == str("2"):
                print("See you next time !")
                exit()
            elif answer == str("3"):
                update_score(var_score, var_nbgames)
            else :
                print("Choose a valid option")
        except KeyboardInterrupt:
                    print("\nProgram interruption.")
                    exit()

def mastermind() :
    
    menu()
    
    
        



if __name__ == "__main__":
    mastermind()