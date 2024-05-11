def encrypt(text, shift):
    encrypted_text = []
    words = text.split()

    for i, word in enumerate(words):
        # Reverse every second word
        if i % 2 == 1:
            word = word[::-1]

        # Shift each letter in the word by the specified number of places
        encrypted_word = ""
        for char in word:
            if char.isalpha():
                shifted_char = chr((ord(char) - ord('a') + shift) % 26 + ord('a')) if char.islower() else chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
                encrypted_word += shifted_char
            else:
                encrypted_word += char

        encrypted_text.append(encrypted_word)

    return ' '.join(encrypted_text)

def decrypt(text, shift):
    decrypted_text = []
    words = text.split()

    for i, word in enumerate(words):
        # Reverse back every second word
        if i % 2 == 1:
            word = word[::-1]

        # Shift each letter in the word back by the specified number of places
        decrypted_word = ""
        for char in word:
            if char.isalpha():
                shifted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a')) if char.islower() else chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
                decrypted_word += shifted_char
            else:
                decrypted_word += char

        decrypted_text.append(decrypted_word)

    return ' '.join(decrypted_text)
# Example usage:
plaintext = "welcome to bilateral solutions"
shift = 3
encrypted_text = encrypt(plaintext, shift)
print("Encrypted Text:", encrypted_text)

print("Do you want to decrypt the above encryption: Y/N")
n=input()
if n.lower()=='y':
    decrypted_text = decrypt(encrypted_text, shift)
    print("Decrypted Text:", decrypted_text)
else:
    exit