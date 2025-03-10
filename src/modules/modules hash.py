import hashlib
from hmac import digest

pass_found=0

i_hash = input("Enter the hashed password:")
p_doc = input("\nEnter password filename inclvding path:")

p_file = open(p_doc, 'r')

for word in p_file:
    enc_word = word.encode('utf-8')
    hash_word = hashlib.md5(enc_word.strip())
    digest = hash_word.hexdigest()

    if digest == i_hash:
        print("password found : ", word)
        pass_found=1
        break

if not pass_found:
    print("password not found")
    