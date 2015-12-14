# coding=utf-8
referencepartsofspeech = {'N':'Noun','p':'Plural','h':'Noun Phrase','V':'Verb usuary participle','t':'Transitive verb','i':'Intransitive verb','A':'Adjective','v':'Adverb','C':'Conjunction','P':'Preposition','!':'Interjection','r':'Pronoun','D':'Definite article','l':'Indefinite article','o':'Nominative'}

class Word:
	definite = False
	def __init__(self, word, partsofspeech=None):
		self.word = word
		self.partsofspeech = partsofspeech if not(partsofspeech==None) else posinst.findpartsofspeech(word)
		print word
		self.definite = not((len(self.partsofspeech)>1))
		
	def __repr__(self):
		return "'"+self.word+(", a " if self.definite else ", which is probably one of: ")+", ".join([referencepartsofspeech[x] for x in self.partsofspeech])+"'"

class PartsOfSpeech:
	def __init__(self):
		pos = open("pos.txt")
		filetext = pos.read()
		filelines = filetext.split("\r");
		self.lines = {}
		for line in filelines:
			appending = line.replace("\xd7"," ")
			changedcharacters = appending.replace("\x96","ñ")
			if(changedcharacters.count(" ")>1):
				ts = changedcharacters.rfind(" ")
				self.lines[changedcharacters[:ts]] = changedcharacters[ts+1:]
			else:
				ts = changedcharacters.split(" ")
				if(len(ts)>1):
					self.lines[ts[0]] = ts[1]
		
	def findpartsofspeech(self, word):
		if(word in self.lines):
			return self.lines[word]


posinst = PartsOfSpeech()
