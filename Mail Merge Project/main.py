names = open("../Mail Merge Project/Input/Names/invited_names.txt", "r")
names_l = names.readlines()
names.close()


name_op = []
for name in names_l:
    y = name.strip()
    name_op.append(y)

print(name_op)

letter = open("./Input/Letters/starting_letter.txt")
content = letter.read()
letter.close()

for names_s in name_op:
    x = content.replace("[name]", names_s)
    with open(f"./Output/ReadyToSend/letter_for_{names_s}.txt", "w") as l_n:
        l_n.write(x)
