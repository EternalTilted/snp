class WrongNumberOfPlayersError(Exception):
    pass
class NoSuchStrategyError(Exception):
    pass


def rps_game_winner(list):

    if len(list) != 2:
        raise WrongNumberOfPlayersError("WrongNumberOfPlayersError")
    
    if not {list[0][1], list[1][1]}.issubset({'R', 'P', 'S'}):
        raise NoSuchStrategyError("NoSuchStrategyError")
    

    if list[0][1] == 'R':
        if list[1][1] == 'P':
            return 'player2 ' + list[1][1]
        else:
            return 'player1 ' + list[0][1]
        
    if list[0][1] == 'S':
        if list[1][1] == 'R':
             return 'player2 ' + list[1][1]
        else:
            return 'player1 ' + list[0][1]
        
    if list[0][1] == 'P':
        if list[1][1] == 'S':
            return 'player2 ' + list[1][1]
        else:
            return 'player1 ' + list[0][1]
    
try:
    print( rps_game_winner([['player1', 'P'], ['player2', 'S'], ['player3', 'S']]) )
except Exception as error:
    print(error)

try:
    print( rps_game_winner([['player1', 'P'], ['player2', 'A']]) )
except Exception as error:
    print(error)

try:
    print( rps_game_winner([['player1', 'A'], ['player2', 'P']]) )
except Exception as error:
    print(error)

try:
    print( rps_game_winner([['player1', 'A'], ['player2', 'A']]) )
except Exception as error:
    print(error)



