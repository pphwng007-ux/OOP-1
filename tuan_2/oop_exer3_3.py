# grid 2*2
def print_grid():
    for i in range(2):
        print("+ - - - -" * 2, "+")
        for j in range(4):
            print("|        " * 2, "|")
    print("+ - - - -" * 2, "+")

print_grid()

# grid 4*4
def print_grid2():
    for i in range(4):
        print("+ - - - -" * 4, "+")
        for j in range(4):
            print("|        " * 4, "|")
    print("+ - - - -" * 4, "+")

print_grid2()
