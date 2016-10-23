#	Pig latin translator
#	can translate sentences, modified version of CodeAcademy single word translator assignment 
#	A.Woodward
#	January 2016


print "Welcome to the Python Pig Latin Translator!"

while True:   
	original_sentence = raw_input('Enter a sentence: ')
	test = original_sentence.replace(' ', '')
	if test.isalpha() == False:
		print "That is not a valid sentence, please try again."
	else:
		break

def split_sentence(sentence):
	dict = {}
	i = 0
	j = 0
	k = 0
	while i < len(sentence):
		if sentence[i] == ' ':
			dict[j] = sentence[k:i]
			j += 1
			k = i + 1
		i += 1
	dict[j] = sentence[k:i]
	dict[j+1] = ''
	return dict
	
def pig_latin_sentence(sentence_broken):
	i = 0
	pyg = 'ay'
	new_sentence = ''
	while sentence_broken[i] != '':
		original = sentence_broken[i]
		first = original[0]
		new_word = original + first + pyg
		new_word = new_word[1:len(new_word)]
		if new_sentence == '':
			new_sentence = new_sentence + new_word
		else:
			new_sentence = new_sentence + ' ' + new_word
		i += 1
	print new_sentence
	
		
pig_latin_sentence(split_sentence(original_sentence))