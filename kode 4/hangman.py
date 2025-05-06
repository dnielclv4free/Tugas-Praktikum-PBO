
import random

class HangmanGame:
    def __init__(self, words, stages):
        self.words = words
        self.stages = stages
        self.max_tries = len(stages) - 1 #sesuai gambar yang disediakan ada 7-1 maka ada 6 kali percobaan maksimal
        self.word = random.choice(words)#memilih kata random dari yang disediakan
        self.word_letters = set(self.word)
        self.guessed_letters = set()
        self.tries = 0 #set 0 dan bertambah seiring percobaan

    def display_progress(self):
        current_word = [letter if letter in self.guessed_letters else "_" for letter in self.word]#jika hurufnya sesuai maka menampilkan huruf, jika tidak sesuai maka masih '_'
        print(" ".join(current_word))
        print(self.stages[self.tries])#menampilkan stages sesuai dengan jumlah percobaan

    def get_guess(self):
        while True:
            guess = input("Tebak satu huruf: ").lower() #membuat menjadi lowercase semua
            if len(guess) == 1 and guess.isalpha(): 
                if guess in self.guessed_letters:
                    print("Huruf sudah ditebak.")
                else:
                    return guess
            else:
                print("Masukkan satu huruf alfabet saja.")

    def play(self):
        print("Selamat datang di permainan Hangman!")
        self.display_progress()

        while self.tries < self.max_tries and self.word_letters:
            guess = self.get_guess()
            self.guessed_letters.add(guess)

            if guess in self.word_letters:
                self.word_letters.remove(guess)
                print("Tebakan benar!")
            else:
                self.tries += 1 #menambah jumlah tries dan menambah stages atau stages berubah ke depan atau meenuju game over
                print("Tebakan salah!")

            self.display_progress()

        if not self.word_letters:
            print(f"Selamat! Kamu berhasil menebak kata '{self.word}'.")
        else:
            print(f"Kamu gagal menebak kata. Kata yang benar adalah '{self.word}'.")
            print("Game Over!")

# Daftar kata dan gambar
words = [
    'algorithm', 'binary', 'boolean', 'byte', 'cache', 'compiler', 'debugger',
    'encryption', 'framework', 'function', 'garbage', 'hash', 'index', 'iterator',
    'javascript', 'json', 'library', 'loop', 'namespace', 'object', 'operator',
    'overload', 'polymorphism', 'queue', 'recursion', 'serialization', 'stack',
    'template', 'variable', 'virtual', 'web', 'xml', 'yaml', 'zip'
]

stages = ["""
    ------
    |    |
    |
    |
    |
    |
    |
------------
""", """
    ------
    |    |
    |    O
    |
    |
    |
    |
------------
""", """
    ------
    |    |
    |    O
    |    |
    |    |
    |
    |
------------
""", """
    ------
    |    |
    |    O
    |    |
    |    |
    |   /
    |
------------
""", """
    ------
    |    |
    |    O
    |    |
    |    |
    |   / \\
    |
------------
""", """
    ------
    |    |
    |    O
    |  --|
    |    |
    |   / \\
    |
------------
""", """
    ------
    |    |
    |    O
    |  --|--
    |    |
    |   / \\
    |
------------
"""]

# Jalankan game
if __name__ == "__main__":
    game = HangmanGame(words, stages)
    game.play()
