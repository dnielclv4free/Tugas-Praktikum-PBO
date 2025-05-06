


import random

class MinesweeperGame:
    def __init__(self):
        self.rows = 3
        self.cols = 3
        self.num_mines = 1
        self.board = [['?'] * self.cols for _ in range(self.rows)]
        self.mines = set()
        self.revealed = set()
        self.game_over = False
        self.place_mine()

    def place_mine(self):
        row = random.randint(0, self.rows - 1)
        col = random.randint(0, self.cols - 1)
        self.mines.add((row, col))
        print(f"Bom ditempatkan di lokasi tersembunyi.")  # Hanya info, tidak tunjukkan posisi

    def uncover_cell(self, row, col):
        if self.game_over:
            print("Permainan sudah berakhir. Tidak bisa membuka kotak lagi.")
            return

        if (row, col) in self.revealed:
            print("Kotak ini sudah dibuka.")
            return
        
        if (row, col) in self.mines:
            self.board[row][col] = 'X'
            self.game_over = True
            self.print_board()
            print("Boom! Kamu kalah!")
        else:
            self.board[row][col] = 'O'
            self.revealed.add((row, col))
            if self.check_win():
                self.print_board()
                print("Selamat! Kamu menang!")

    def check_win(self):
        return len(self.revealed) == self.rows * self.cols - self.num_mines

    def print_board(self):
        for row in self.board:
            print(" ".join(row))

if __name__ == "__main__":
    game = MinesweeperGame()
    game.print_board()
    
    while not game.game_over:
        try:
            user_input = input("Pilih kotak (format: baris kolom, contoh 0 2): ")
            r, c = map(int, user_input.strip().split())
            if 0 <= r < 3 and 0 <= c < 3:
                game.uncover_cell(r, c)
                if not game.game_over:
                    game.print_board()
            else:
                print("Koordinat di luar jangkauan. Masukkan angka antara 0 dan 2.")
        except ValueError:
            print("Input tidak valid. Masukkan dua angka dipisahkan spasi.")

