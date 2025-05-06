# Prints a command-line argument
# from sys import argv

# if len(argv) == 2:
#     print(f"hello, {argv[1]}") 
# else:
#     print("hello, world") 

# i/o
# open("readme.txt", "w") # Open file for writing

# f = open('readme.txt', 'w') 
# f.write('readme') 
# f.close()  # Harus menutup file secara manual

# with open('readme.txt', 'w') as f:
#     f.write('readme')
# # File otomatis ditutup di sini, tanpa perlu memanggil f.close()

quote = '成功を収める人とは人が投げてきたレンガでしっかりした基盤を築くことができる人のことである。'

with open('quotes.txt', 'w', encoding='utf-8') as f:
    f.write(quote)