from random import shuffle

def getIntInRange(low, high, prompt = "", errmsg = ""):
    if prompt == "":
        prompt = "Please enter an integer in the range [%d,%d]." % (low, high)
    if errmsg == "":
        errmsg = "The input you entered was not a valid integer in the range [%d,%d]; please retry your input." % (low, high)

    good_input = False
    n = 0

    while(not good_input):
        input = raw_input(prompt)
        try:
            n = int(input)
            if str(n) == input and n >= low and n <= high:
                good_input = True
        except:
            pass

        if not good_input:
            print(errmsg)

    return n
	
n = getIntInRange(1,10,"Please enter the number of decks that you want in the shoe (1-10): ", "That's not a valid number of decks.")

suits = ["C", "D", "H", "S"]
values = {"Ace": 11, "2": 2, "3":3, "4": 4, "5": 5 , "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 10, "Q": 10, "K": 10}

deck = []

for suit in suits:
	for value in values:
		deck.append((suit, value))
		


total_decks = deck * n
shuffle(total_decks)

count = 0 
number_hands = len(total_decks) / 2
stop_hand = len(total_decks) - 1
for i in range(0, stop_hand, 2):
	card1, card2 = total_decks[i], total_decks[i + 1]
	display = "%s%s %s%s" % (card1[1], card1[0], card2[1], card2[0])
	if values[card1[1]] + values[card2[1]] == 21:
		display += " -Blackjack!"
		count += 1
	print display

        
percent = float(count) / float(number_hands) * 100

if count == 0:
    print "There where no blackjacks."
elif count == 1:
    print "After %i hands there was 1 blackjack at %i " % (number_hands, count, percent) + "%."
else:    
    print "After %i hands there were %i blackjacks at %i " % (number_hands, count, percent) + "%."
    
