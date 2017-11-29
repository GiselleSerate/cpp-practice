def isConsonant(c):
	'''Returns whether a character is a consonant or not.'''
	if c in ['a', 'e', 'i', 'o', 'u', 'y']:
		return False
	else:
		return True

def naivePig(rawText):
	'''Translates text to Pig Latin.''' 
	# Handles punctuation terribly (by assuming it's a consonant) and only transposes initial letter, not sound.
	textArr = rawText.split(" ")
	retStr = ""
	for word in textArr:
		if isConsonant(word[0]): # "ananab"
			retStr += word[1:] + word[0]
		else: # "apple"
			retStr += word
		retStr += "ay"
		retStr += " " # Hmm. Spaces. 
	return retStr

def soundPig(rawText):
	'''Translates text to Pig Latin.'''
	# Still handles punctuation terribly (by assuming it's a consonant) but now transposes all initial consonants.
	textArr = rawText.split(" ")
	retStr = ""
	for word in textArr:
		transpose = ""
		while len(word) != 0 and isConsonant(word[0]): # "ananab"
			transpose += word[0]
			word = word[1:]
		retStr += word + transpose + "ay"
		retStr += " " # Hmm. Spaces. 
	return retStr

# Main function
def main():
	print(soundPig(input("What text would you like to translate to Pig Latin?\n")))

# Run main automagically
if __name__ == '__main__':
	main()