import tkinter as tk
import chess
from Decision_class1 import Chessboard1,change_to_ord
from Decision_class2 import Pieces
import time
def strip_moves(moves):
    ans = []
    for move in moves:
        ans.append(move[-2]+move[-1])
    return ans

def strip_moves1(moves):
    ans = []
    for move in moves:
        ans.append(move[0]+move[1])
    return ans


class get_ans(tk.Tk):
    def __init__(self,models,classes,im,camera,color):
        super().__init__()
        self.title("Make move")
        self.geometry("800x800")
        self.models = models
        self.classes = classes
        self.im = im
        self.camera = camera
        self.color = color
        

    def update_color(self,color):
        self.color = color

    def not_my_turn(self,text):
        label = tk.Label(self, text=text, fg="#264370", font=("Arial", 64))
        label.pack()

        
    def clear_frames(self):
        # Destroy all widgets in the root window
        for widget in self.winfo_children():
            widget.destroy()
    
    def run(self, board):
        self.clear_frames()
        self.update()
        while True:
            time.sleep(0.4)


            print("Select a piece (0: Pawn, 1: Rook, 2: Knight, 3: Bishop, 4: Queen, 5: King):")
            piece = Pieces(self, self.im, self.models[0], self.classes[0],self.camera)
            choice = piece.run()
            self.clear_frames()
            self.update()
            if choice < 0 or choice > 5:
                print("Niepoprawny wybór figury.")
                continue
            selected_piece_type = []
            piece_types = [chess.KING, chess.QUEEN, chess.BISHOP, chess.KNIGHT,chess.ROOK ,chess.PAWN]
            selected_piece_type.append(piece_types[choice])
            if choice == 2:
                selected_piece_type.append(piece_types[4])
            piece_moves = []
            for move in board.legal_moves:  
                if board.piece_at(move.from_square).piece_type in selected_piece_type:
                    piece_moves.append(str(move))
                    
            strip_m = strip_moves1(piece_moves)
            chessboard_frame = Chessboard1(self, model=self.models, classes=self.classes, highlight_side="None", selected_squares=strip_m,camera = self.camera,color=self.color)
            chessboard_frame.pack(side=tk.LEFT)
            select_square = chessboard_frame.define_square()
            self.update()
            if select_square == "A1":
                continue
            move = select_square
            square = chess.parse_square(select_square)
            chessboard_frame.destroy()
            possible_moves = list(board.legal_moves)
            filtered_moves = [str(move) for move in possible_moves if move.from_square == square]
            chessboard_frame = Chessboard1(self, model=self.models, classes=self.classes, highlight_side="None", selected_squares=strip_moves(filtered_moves),camera=self.camera,color=self.color)
            chessboard_frame.pack(side=tk.LEFT)
            select_square = chessboard_frame.define_square()
            self.update()
            if select_square == "A1":
                continue
            move += select_square
            
            return move
            break
         
