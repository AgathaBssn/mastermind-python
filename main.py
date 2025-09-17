COLORS = ['R', 'G', 'B', 'Y', 'P', 'W']
#Drawing of 4 colors for the round
def init_colors():
    import random
    
    soluce = []
    for i in range(4):
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
            guess = input("Submit 4 colors : ")

            #check if there are 4 characters
            if len(guess) != 4 :
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

def check_guess(soluce, player_input):
    # init count
    right = 0
    wplace = 0

    # well placed
    soluce_rest = []
    input_rest = []
    for i in range(4):
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

        
        


        

def mastermind() :
    soluce = init_colors()
    print(soluce)
    reminder_color()
    guess =ask_color()
    check_guess(soluce, guess)


if __name__ == "__main__":
    mastermind()