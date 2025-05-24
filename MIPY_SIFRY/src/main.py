from cipher.cipher_util import CypherUtil


print("hello world")

a = CypherUtil("VLZODTQHUXWSERMCFKNYIBJGP_A");
print(a.key);
print(a.DEFAULT_KEY);

b = a.encrypt("TEST_TEST")

print(b)
print(a.decrypt(b))