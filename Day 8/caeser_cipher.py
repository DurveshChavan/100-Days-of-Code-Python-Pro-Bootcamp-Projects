from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar_cipher(original_text, shift_amount, direction_which):
    cipher_text = ""
    if direction_which == "decode":
        shift_amount *= -1
    for i in original_text:
        if i not in alphabet:
            cipher_text += i
        else:
            cipher_text += alphabet[(alphabet.index(i) + shift_amount) % len(alphabet)]
    print(f"Here is the decoded result: {cipher_text}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar_cipher(original_text=text, shift_amount=shift, direction_which=direction)
    ans = input("Type 'yes' if you want to go again. Otherwise, type 'no'.").lower()
    if ans == "no":
        should_continue = False
        print("Goodbye!")



