from random import shuffle

n = int(raw_input("How many decks are there?"))

suits = ["C", "D", "H", "S"]
value = ["Ace", "2", "3", "4" , "5" , "6" , "7" , "8" , "9" , "10" , "J", "Q" , "K" ]

ten_pointers = ["10", "J", "Q", "K"]

aces =[]
for s in suits:
    aces.append("Ace" + s)

ten_pointers_suits = []
for t in ten_pointers:
    for s in suits:
        ten_pointers_suits.append(t+s)

blackjack = []
for a in aces:
    for t in ten_pointers_suits:
        blackjack.append(a + "," + t)
        blackjack.append(t + ","+ a)

deck = []

for i in suits:
    for j in value:
        deck.append(j + i)

total_decks = deck * n

shuffle(total_decks)

number_hands = len(total_decks) / 2

draw = []
for i in range(0, len(total_decks) -1, 2):
    draw.append(total_decks[i] + "," + total_decks[i +1])
  
count = 0 
for i in draw:
    if i in blackjack:
        print i + " -Blackjack!"
        count += 1
    else:
        print i
        
percent = float(count) / float(number_hands) * 100

if count == 0:
    print "There where no blackjacks."
elif count == 1:
    print "After %i hands there was 1 blackjack at %i " % (number_hands, count, percent) + "%."
else:    
    print "After %i hands there were %i blackjacks at %i " % (number_hands, count, percent) + "%."
    
