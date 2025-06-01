from cipher.cipher_util import generate_random_key, sanitize_text, text_correctness
from cipher.substitute_cipher import decrypt, encrypt

plain_text = sanitize_text("The quick brown fox jumps over the lazy dog")
key = generate_random_key()
key_str = "".join(key)

print(f"Original text : plain_text")
print(f"Cypher key = {key_str}")

encrypted = encrypt(key, plain_text)

print(f"Encrypted text : {encrypted}")

decrypted = decrypt(key, encrypted)

print(f"Decrypted : {decrypted}")

score = text_correctness(plain_text, decrypted)

print(f"Score : {score}")