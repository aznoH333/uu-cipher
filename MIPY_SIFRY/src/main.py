from os import listdir
from cipher.bygram_matrix import create_bygram_matrix, get_bygrams, make_matrix_relative
from file_processing.file_processing import process_file


# create matrix
krakatit_file = open("./Krakatit.txt")
krakatit_matrix = make_matrix_relative(create_bygram_matrix(get_bygrams(krakatit_file.read())))
krakatit_file.close()

# get test files
files = listdir("./Testovaci_soubory")

# process files
for file_index in range(0, len(files)):
    print(f"Total progress {file_index} / {len(files)}")
    file = "./Testovaci_soubory/" + files[file_index]
    process_file(file, krakatit_matrix, 40000)

print("Processing finished!")
