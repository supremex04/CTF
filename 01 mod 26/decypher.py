import binascii
encoded_text = input("Enter the encoded text: ")
decoded_text = ""
for char in encoded_text:
    if (char >= "A" and char <= "Z"):
        decoded_text = decoded_text + chr((ord(char)-ord("A") + 13) % 26 + ord("A"))
    elif (char >= "a" and char <= "z"):
        decoded_text = decoded_text + chr((ord(char)-ord("a") + 13) % 26 + ord("a"))
    else:
        decoded_text += char

print(f"ROT-13 decoded string: {decoded_text}")
