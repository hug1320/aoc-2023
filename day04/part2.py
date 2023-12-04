fd = open("input")
content = fd.read().split("\n")[:-1]

cards = [k.split(":")[1:] for k in content]
cards = [k[0].split("|") for k in cards]
cards = [[k[0].split(), k[1].split()] for k in cards]

size = len(cards[0][1])
nb_card = 0
for i in range(len(cards)):
    matching = 0
    nb_card += 1
    for card in cards[i][1][:size]:
        if card in cards[i][0]:
            matching += 1
    ratio = len(cards[i][1]) // size
    for j in range(1, matching+1):
        nb_card += ratio
        cards[i+j][1] += cards[i+j][1][:size]*ratio

print(nb_card)
