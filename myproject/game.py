import time
import chess
from functions import is_game_ready,get_data,is_my_turn,send_move
from Make_move import strip_moves,strip_moves1,get_ans


def game(api_token,models,classes,images,camera):
    ans = get_ans(models,classes,images,camera,1)
    ans.not_my_turn("Turn on Game")
    while True:
        time.sleep(2)
        data = get_data(api_token)
        ans.update()
        ans.update_idletasks()
        print("waiting")
        if is_game_ready(data):
            break

    data = get_data(api_token)
    id_game = data['nowPlaying'][0]['fullId']
    board = chess.Board(data['nowPlaying'][0]['fen'])
    color_str = data['nowPlaying'][0]['color']
    if color_str == "black":
        color = 0
    else:
        color = 1
        
    ans.update()
    ans.update_idletasks()
    ans.update_color(color)
    time.sleep(6)
    while not board.is_game_over() and is_game_ready(data):
        time.sleep(1)
        data = get_data(api_token)
        if not is_game_ready(data):
          break
        if not data['nowPlaying'][0]['isMyTurn']:
            continue

        board = chess.Board(data['nowPlaying'][0]['fen'])
        #move = input("Make move (in UCI format): ")
        move = ans.run(board)
        while True:
            try:
                move = chess.Move.from_uci(move)
                if move in board.legal_moves:
                    break
                else:
                    print("Invalid move. Try again.")
                    #move = input("Make move (in UCI format): ")
                    move = ans.run(board)
                    print(move)
            except ValueError:
                print("Invalid move format. Try again.")
                #move = input("Make move (in UCI format): ")
                move = ans.run(board)
                print(move)
        send_move(id_game, move, api_token)
        ans.not_my_turn("Opponent turn")
        ans.update()
        ans.update_idletasks()
