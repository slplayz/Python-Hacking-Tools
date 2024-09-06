import hashlib

def crack_password(hash, wordlist):
    with open(wordlist, 'r') as f:
        for word in f.readlines():
            word = word.strip()
            hashed_word = hashlib.md5(word.encode()).hexdigest()
            if hashed_word == hash:
                print(f"Password found: {word}")
                return
    print("Password not found")

hash = input("Enter the MD5 hash: ")
wordlist = input("Enter the wordlist file: ")
crack_password(hash, wordlist)