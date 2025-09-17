def init_colors():
    import random
    colors = ['R', 'G', 'B', 'Y', 'P', 'W']
    soluce = []
    for i in range(4):
        soluce += colors[random.randint(0,3)]
    return soluce

def mastermind() :
    print(init_colors())


mastermind()