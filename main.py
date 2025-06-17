from pathlib import Path
import tkinter as tk
from eval_move import eval_move
from outcome_convention import Outcome




class TicTacToe:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title('Tic-Tac-Toe')
        self.window.resizable(False, False)

        path = Path(__file__).parent / 'assets'
        self.assets = {
            'empty': tk.PhotoImage(file=path/'empty.png'),
            'o': tk.PhotoImage(file=path/'o.png'),
            'x': tk.PhotoImage(file=path/'x.png')
        }
        self.board = None
        self.buttons = None
        self.reset()
        self.window.mainloop()

    def reset(self):
        self.board = [[0 for _ in range(3)] for _ in range(3)]
        self.create_board()

    def popup_message(self, message):
        w, h = 320, 120
        self.window.update_idletasks()
        x = (self.window.winfo_x()) + (self.window.winfo_width() // 2) - (w // 2) + 6
        y = (self.window.winfo_y()) + (self.window.winfo_height() // 2) - (h // 2) + 6

        popup = tk.Toplevel()
        popup.overrideredirect(True)
        popup.geometry(f"{w}x{h}+{x}+{y}")
        bg2, bg3, fg = '#7F7F7F','#777777', '#F1F1F1'
        font = 'Comic Sans MS'
        popup.config(bg=bg2)
        label = tk.Label(popup, text=message, font=(font, 22), bg=bg2, foreground=fg)
        label.pack(pady=10)
        tk.Button(popup, font=(font, 16), text="RESET",
                  bg=bg3, activebackground=bg3, foreground=fg, relief='flat',
                  command=lambda p=popup: self.popup_reset(p)).pack()
        popup.grab_set()

    def popup_reset(self, popup):
        popup.destroy()
        self.reset()

    def create_board(self):
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col] = tk.Button(self.window,
                                                   image=self.assets['empty'],
                                                   width=128, height=128,
                                                   relief='sunken', cursor='hand2',
                                                   activebackground='#1F1F1F', bg='#1F1F1F',
                                                   command=lambda r=row, c=col: self.make_move(r, c))
                self.buttons[row][col].grid(row=row, column=col)

    def redraw(self):
        for r in range(3):
            for c in range(3):
                match self.board[r][c]:
                    case 0: self.buttons[r][c].config(image=self.assets['empty'])
                    case 1: self.buttons[r][c].config(image=self.assets['x'])
                    case -1: self.buttons[r][c].config(image=self.assets['o'])
                    case _: raise ValueError(f"Os estados válidos do tabuleiro são 0, 1 e -1. Foi encontrado '{self.board[r][c]}' na posição [{r}][{c}].")

    def make_move(self, r, c):
        self.board, outcome = eval_move(self.board, (r, c))
        self.redraw()
        match outcome:
            case Outcome.X_WINS: self.popup_message("Jogador 'x' ganhou!")
            case Outcome.O_WINS: self.popup_message("Jogador 'o' ganhou!")
            case Outcome.DRAW: self.popup_message("Empate!")
            case Outcome.INVALID_MOVE: self.window.bell()
            case Outcome.INVALID_STATE: raise ValueError(f"Tabuleiro inválido inválido: {self.board}")
            case Outcome.CONTINUE: pass
            case _: assert False



if __name__ == '__main__':
    TicTacToe()