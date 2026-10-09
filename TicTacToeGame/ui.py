import tkinter as tk
from tkinter import messagebox

win = tk.Tk()
win.title("Tic Tac Toe")
win.geometry("430x560")
win.resizable(False, False)
win.configure(bg="#111827")

board = []
turn = "X"
startgame = None



#  Start game


def start(gamestart):
    global startgame
    startgame = gamestart

    showhome()
    win.mainloop()



# Home screen


def showhome():
    for item in win.winfo_children():
        item.destroy()

    title = tk.Label(
        win,
        text="TIC TAC TOE",
        font=("Arial", 30, "bold"),
        bg="#111827",
        fg="#60a5fa"
    )
    title.pack(pady=(55, 10))

    sub = tk.Label(
        win,
        text="Classic X and O Game",
        font=("Arial", 13),
        bg="#111827",
        fg="#d1d5db"
    )
    sub.pack(pady=(0, 45))

    play = tk.Button(
        win,
        text="PLAY GAME",
        font=("Arial", 16, "bold"),
        bg="#2563eb",
        fg="white",
        activebackground="#1d4ed8",
        activeforeground="white",
        relief="flat",
        width=15,
        height=2,
        command=playgame
    )
    play.pack()

    info = tk.Label(
        win,
        text="Tap any box to place your mark",
        font=("Arial", 11),
        bg="#111827",
        fg="#9ca3af"
    )
    info.pack(pady=30)



#  Game screen


def playgame():
    global board
    global turn

    for item in win.winfo_children():
        item.destroy()

    board, turn = startgame()

    title = tk.Label(
        win,
        text="TIC TAC TOE",
        font=("Arial", 25, "bold"),
        bg="#111827",
        fg="#60a5fa"
    )
    title.pack(pady=(20, 5))

    turnbox = tk.Label(
        win,
        text="Player X Turn",
        font=("Arial", 14, "bold"),
        bg="#1f2937",
        fg="#f9fafb",
        width=20,
        pady=8
    )
    turnbox.pack(pady=10)

    area = tk.Frame(win, bg="#374151")
    area.pack(pady=15, padx=15)

    board.clear()

    for i in range(9):
        box = tk.Button(
            area,
            text="",
            font=("Arial", 35, "bold"),
            width=3,
            height=1,
            bg="#1f2937",
            fg="#60a5fa",
            activebackground="#374151",
            activeforeground="#60a5fa",
            relief="flat",
            bd=0,
            command=lambda pos=i: move(pos, turnbox)
        )

        row = i // 3
        col = i % 3

        box.grid(
            row=row,
            column=col,
            padx=3,
            pady=3,
            ipadx=8,
            ipady=8
        )

        board.append(box)

    reset = tk.Button(
        win,
        text="NEW GAME",
        font=("Arial", 13, "bold"),
        bg="#10b981",
        fg="white",
        activebackground="#059669",
        activeforeground="white",
        relief="flat",
        width=14,
        height=1,
        command=playgame
    )
    reset.pack(pady=15)

    home = tk.Button(
        win,
        text="HOME",
        font=("Arial", 11),
        bg="#374151",
        fg="#f9fafb",
        activebackground="#4b5563",
        activeforeground="white",
        relief="flat",
        width=10,
        command=showhome
    )
    home.pack()



# STEP 5: Player move


def move(pos, turnbox):
    global turn

    if board[pos]["text"] != "":
        return

    board[pos]["text"] = turn

    if turn == "X":
        board[pos]["fg"] = "#60a5fa"
    else:
        board[pos]["fg"] = "#f472b6"

    marks = []

    for box in board:
        marks.append(box["text"])


    # Check winner


    ways = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    winmark = ""

    for way in ways:
        a = way[0]
        b = way[1]
        c = way[2]

        if marks[a] != "" and marks[a] == marks[b] and marks[b] == marks[c]:
            winmark = marks[a]
            break

    if winmark != "":
        turnbox.config(text="Player " + winmark + " Wins!")

        for box in board:
            box.config(state="disabled")

        messagebox.showinfo("Game Over", "Player " + winmark + " Wins!")
        return


    # Check draw
   

    full = True

    for mark in marks:
        if mark == "":
            full = False

    if full:
        turnbox.config(text="Game Draw!")
        messagebox.showinfo("Game Over", "It  a Draw!")
        return

    # Change player

    if turn == "X":
        turn = "O"
    else:
        turn = "X"

    turnbox.config(text="Player " + turn + " Turn")


#  Close application


win.protocol("WM_DELETE_WINDOW", win.destroy)
