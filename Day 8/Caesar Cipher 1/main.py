alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text,shift_amount):
    text_list = list(plain_text)
    for i in range(len(text_list)):
        if text_list[i] not in alphabet:
            continue
        else:
            text_list[i] = alphabet[(alphabet.index(text_list[i]) + shift_amount) % 26]

    encrypted_text = "".join(text_list)
    print(f"Encrypted massage : {encrypted_text}")

def decrypt(encrypted_text,shift_amount):
    text_list = list(encrypted_text)
    for i in range(len(text_list)):
        if text_list[i] not in alphabet:
            continue
        else:
            text_list[i] = alphabet[(alphabet.index(text_list[i])- shift_amount) % 26]

    decrypted_text = "".join(text_list)
    print(f"Decrypted massage : '{decrypted_text}'")


if direction=="encode":
    encrypt(text,shift)
else:
    decrypt(text,shift)
