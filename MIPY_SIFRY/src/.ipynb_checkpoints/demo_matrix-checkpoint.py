# create matrix
from cipher.bygram_matrix import create_bygram_matrix, get_bygrams


krakatit_file = open("./Krakatit.txt")
krakatit_matrix = create_bygram_matrix(get_bygrams(krakatit_file.read()))
krakatit_file.close()

print(krakatit_matrix)
