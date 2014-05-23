#Pig Latin Translator

pyg = 'ay'
original = raw_input('Enter a word:')
word = original.lower()
if len(original) > 0 and original.isalpha(): #check for validity
	word = original.lower()
	first = word[0]
	if first == "a" or first=="e" or first=="i" or first=="o" or first=="u": #check for vowel
		new_word= word+pyg
		print new_word
	else: #consonant
		N = len(word)
		S = word[1:N]
		new_word = S+first+pyg
		print new_word
else: #not valid
	print 'empty'