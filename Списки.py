def print_board():
    chars = ['-', 'X', 'O']
    for r in range(3):
        for c in range(3):
            print(chars[game.B[r][c]], end=' ')
        print()
tic_tac_toe()

game = while game.check_for_winner() == -1:
    print_board()
    r,c = eval(input('Enter spot, player ' + str(game.player)
    + ': '))
    game.make_move(r,c)

print_B()
x = game.check_for_winner()
if x == 0:
    print("It's a draw.")
else:
    print('Player', x, 'wins!')




    
        
        

