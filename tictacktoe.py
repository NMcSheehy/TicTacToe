board = []

def main():
    ## Setup the Tic Tac Toe board. ##
    print('Welcome to Tic Tac Toe')
    print('What size board would you like?')
    print()
    width = int(input('(minimum 3) width: '))
    height = int(input('(minimum 3) height: '))

    create_board(width, height)
    while True:
        player1 = int(input("Player 1's turn. [X]: "))
        board[player1 - 1] = 'X'
        show_board(width, height)
        print()

        player2 = int(input("Player 2's turn. [O]: "))
        board[player2 - 1] = 'O'
        show_board(width, height)
        print()



def show_board(width, height):
    count = 0
    for _ in range(1, width + 1):
        print()
        print()
        for _ in range(1, height + 1):
            count += 1
            print(f'{board[count - 1]:>2}', end = ' ')
    print()

def create_board(width, height):
    count = 0
    for _ in range(1, width + 1):
        print()
        print()
        for _ in range(1, height + 1):
            count += 1
            print(f'{count:>2}', end = ' ')
            board.append(str(count))
    print()



                



    


main()

