import art
print(art.logo)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


def caesar(text, shift, direction = direction):
    for i in range(len(text)):
      if text[i].isalpha():
        ind = alphabet.index(text[i])
        if direction == "encode":
          shift_amount = 1
        if direction == "decode":
          shift_amount = -1
        ind1 = (ind + shift_amount * shift)%26
        temp = list(text)
        temp[i] = alphabet[ind1]
        text = "".join(temp)
    print(f"Your {direction}d message: {text}")


caesar(text, shift, direction)