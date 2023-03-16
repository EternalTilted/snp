def rps_game_winner(list):

    if len(list) != 2:
        raise Exception('WrongNumberOfPlayersError')
    
    if not {list[0][1], list[1][1]}.issubset({'R', 'P', 'S'}):
        raise Exception('NoSuchStrategyError')
    

    if list[0][1] == 'R':
        if list[1][1] == 'P':
            return 'player2' + ' ' + list[1][1]
        else:
            return 'player1'+ ' ' + list[0][1]
        
    if list[0][1] == 'S':
        if list[1][1] == 'R':
             return 'player2' + ' ' + list[1][1]
        else:
            return 'player1'+ ' ' + list[0][1]
        
    if list[0][1] == 'P':
        if list[1][1] == 'S':
            return 'player2' + ' ' + list[1][1]
        else:
            return 'player1'+ ' ' + list[0][1]
    

print(rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]))
print(rps_game_winner([['player1', 'P'], ['player2', 'A']]) )
print(rps_game_winner([['player1', 'P'], ['player2', 'S']]) )
print(rps_game_winner([['player1', 'P'], ['player2', 'P']]) )

