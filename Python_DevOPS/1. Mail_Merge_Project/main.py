with open("Input/Names/invited_names.txt") as file:
    names = file.readlines()

for name in names:
    name = name.strip("\n")
    with open("Input/Letters/starting_letter.txt") as file:
        content = file.read()
        content = content.replace("[name]", name)

    with open(f"Output/ReadyToSend/letter_for_{name}.txt", mode = "w") as file:
        file.write(content)


