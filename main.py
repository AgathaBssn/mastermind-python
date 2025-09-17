COLORS = ['R', 'G', 'B', 'Y', 'P', 'W']
#Drawing of 4 colors for the round
def init_colors():
    import random
    
    soluce = []
    for i in range(4):
        soluce += COLORS[random.randint(0,3)]
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

        

def mastermind() :
    print(init_colors())
    print(ask_color())

if __name__ == "__main__":
    mastermind()