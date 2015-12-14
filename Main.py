# coding=utf-8
test = open("pos.txt")
file = test.read()
filelines = file.split("\r");
lines = {}
for line in filelines:
	appending = line.replace("\xd7"," ")
	changedcharacters = appending.replace("\x96","ñ")
	if(changedcharacters.count(" ")>1):
		ts = changedcharacters.rfind(" ")
		lines[changedcharacters[:ts]] = changedcharacters[ts+1:]
	else:
		ts = changedcharacters.split(" ")
		if(len(ts)>1):
			lines[ts[0]] = ts[1]
		
		
referencepartsofspeech = {'N':'Noun','p':'Plural','h':'Noun Phrase','V':'Verb usuary participle','t':'Transitive verb','i':'Intransitive verb','A':'Adjective','v':'Adverb','C':'Conjunction','P':'Preposition','!':'Interjection','r':'Pronoun','D':'Definite article','l':'Indefinite article','o':'Nominative'}

def findpartsofspeech(word):
	if(word in lines):
		return lines[word]
	
class Sentence:
	def __init__(self, words):
		if(len(words)>0 and isinstance(words[0],Word)):
			self.words = words
		elif(isinstance(words[0],str)):
			self.words = []
			for word in words:
				self.words.append(Word(word))
		elif(isinstance(words,str)):
			self.words = []
			wordarray = words.split(" ")
			for word in wordarray:
				self.words.append(Word(word))
		else:
			raise TypeError("Problems")
			
	def __repr__(self):
		return self.words.__repr__()

class Word:
	definite = False
	
	def __init__(self, word, partsofspeech=None):
		self.word = word
		self.partsofspeech = partsofspeech if not(partsofspeech==None) else findpartsofspeech(word)
		self.definite = not((len(self.partsofspeech)>1))
		
	def __repr__(self):
		return "'"+self.word+(", a " if self.definite else ", which is probably one of: ")+", ".join([referencepartsofspeech[x] for x in self.partsofspeech])+"'"





# Now to figure out which part of speech something is

sentence = "What is this is a great sentence" #raw_input("Please put in the sentence:\n")
sentence = Sentence(sentence.lower().split(" "))
print sentence.words[0]