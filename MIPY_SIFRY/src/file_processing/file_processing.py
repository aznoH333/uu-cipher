from cipher.substitute_cipher import break_encryption, decrypt


def process_file(path: str, probability_matrix: dict, attempts_per_file: int):
    file = open(path)
    contents = file.read()
    file.close()

    file_id = get_file_id(path)

    print(f"Processing file {file_id}")

    key = break_encryption(contents, probability_matrix, attempts_per_file)
    plain_text = decrypt(key, contents)

    save_decrypted("./output/", key, plain_text, file_id)



def get_file_id(path: str) -> int:
    return path.split("_")[4]


def save_decrypted(path: str, key: list, plain_text: str, id: int):
    plain_text_file_name = f"text_{len(plain_text)}_sample_{id}_plaintext.txt"
    key_file_name = f"text_{len(plain_text)}_sample_{id}_key.txt"

    write_to_file(path + plain_text_file_name, plain_text)
    write_to_file(path + key_file_name, "".join(key))


def write_to_file(path, contet):
    file = open(path, "w")
    file.write(contet)
    file.close()
