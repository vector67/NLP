# coding=utf-8
def findWords(word):
	if(word in posinst.lines):
		return posinst.lines[word]
	return "No words found"
referencepartsofspeech = {'N':'Noun','p':'Plural','h':'Noun Phrase','V':'Verb usuary participle','t':'Transitive verb','i':'Intransitive verb','A':'Adjective','v':'Adverb','C':'Conjunction','P':'Preposition','!':'Interjection','r':'Pronoun','D':'Definite article','l':'Indefinite article','o':'Nominative'}
POSFILE = 2 # 1=pos.txt, 2=2of12id.txt
class Word:
	definite = False
	word = "" # the string which represents the actual word
	pos = "" # A=Adjective or Adverb, V=Verb, N=Noun, C=Conjunction, p=Preposition, P=pronoun, I=Interjection, S=Spoken Contraction
	inflection = 0 # depends on the pos 0=noun,2=adjective basic, 3=adjective er form, 4=adjective est form,5=verb present tense, 6=verb past tense, 7=verb past participle,8=verb ing form,9=verb plural form
	basicword = None # references the word which this inflection is an inflection of, only relevant if inflection=3,4,6,7,8 or 9
	lesspreferred = 0 # 0 =fine, 1 = less preferred, 2 = even less preferred
	preferredword = None # references the word that should be used instead of this one, only set if not(lesspreferred==0)
	equivalentword = None # references the word that is equivalent
	def __init__(self, word, pos, inflection, basicword = None, lesspreferred = 0, preferredword = None, equivalentword = None):
		self.word = word
		self.pos = pos
		self.inflection = inflection
		self.basicword = basicword
		self.lesspreferred = lesspreferred
		self.preferredword = preferredword
		self.equivalentword = equivalentword
		#self.partsofspeech = partsofspeech if not(partsofspeech==None) else posinst.findpartsofspeech(word)
		#self.definite = not((len(self.partsofspeech)>1))
	def getPOS(self):
		returning = ""
		for x in inflections:
			returning = returning + str(x.inflection)
		return returning
	def __repr__(self):
		return "'"+self.word+(", the ")+str(self.pos)+","+str(self.inflection)+"'"
	
class PartsOfSpeech:
	def __init__(self):
		if(POSFILE==1):
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
		else:
			pos = open("2of12id.txt")
			filetext = pos.read()
			filelines = filetext.split("\n");
			del filelines[-1]
			self.lines = {}
			for line in filelines:
				parts = line.split(":")
				if(len(parts)>2):
					print "Bad things"
				wordpos = parts[0].split(" ")
				mainword = Word(wordpos[0], wordpos[1],0)
				self.addPOStoWord(mainword.word,mainword)
				if(wordpos[0]=="be" or wordpos[0]=="@wit"):
					if(wordpos[0]=="be"):
						mainword = Word("be","V",0)
						self.addPOStoWord("be",mainword)
						pasttense = Word("were","V",1,mainword)
						self.addPOStoWord("were",pasttense)
						pasttense2 = Word("been","V",1,mainword)
						self.addPOStoWord("been",pasttense2)
						ingtense = Word("being","V",2,mainword)
						self.addPOStoWord("being",ingtense)
						present1 = Word("am","V",0,mainword)
						self.addPOStoWord("am",present1)
						present2 = Word("is","V",0,mainword)
						self.addPOStoWord("is",present2)
						present3 = Word("are","V",3,mainword)
						self.addPOStoWord("are",present3)
						
					#do inflections for these words manually
					pass
				else:
					inflections = parts[1].split("  ")
					if("|" in parts[1]):
						#We do something else in this case
						pass
					elif(wordpos[1]=="V" and len(parts[1])>0):
						mode = 1
						beforeing = []
						ing = []
						aftering = []
						for word in inflections:
							if(mode==1):
								if(len(inflections)==3 and word=="-" and not(mode==2)):
									mode=2
								elif(word[-3:]=="ing" or word[-4:]=="ing)"):
									ing.append(ing)
									inflectedword = Word(word,"V",8,mainword)
									self.addPOStoWord(word,inflectedword)
									mode=2
								else:
									beforeing.append(word)
									inflectedword = Word(word,"V",6,mainword)
									#TODO: Fix this so that it correctly selects either 6 or 7 for the inflection type
									self.addPOStoWord(word,inflectedword)
							elif(mode==2):
								aftering.append(word)
								inflectedword = Word(word,"V",9,mainword)
								self.addPOStoWord(word,inflectedword)
							
						if(not(mode==2)):
							print line
			print self.lines
	def addPOStoWord(self,word,wordobject):
		if(word in self.lines):
			self.lines[word].append(wordobject)
		else:
			self.lines[word] = [wordobject]
	def findpartsofspeech(self, word):
		if(word in self.lines):
			return self.lines[word]


posinst = PartsOfSpeech()
