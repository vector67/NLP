# coding=utf-8
def findWords(word):
	if(word in posinst.lines):
		return posinst.lines[word][:]
	return "No words found"

def createWord(word, pos, inflection, basicword = None, lesspreferred = 0, preferredword = None, equivalentword = None):
	if(not(len(word)>0)):
		return []
	if((word[0]=="{" or word[-1]=="}") and not(" " in word)):
		return []
	if(word[0]==" " or word[0]=="~" or (word[0]=="-" and len(word)>1 and not(word[1]==" ")) or word[0]=="(" or word[0]=="@"):
		return createWord(word[1:],pos,inflection,basicword,lesspreferred,preferredword,equivalentword)
	if(word[-1]==")"):
		return createWord(word[:-1],pos,inflection,basicword,lesspreferred,preferredword,equivalentword)
	if(word[0]=="-" and ((len(word)>1 and not(word[1]==" ")) or len(word)==1)):
		if(isinstance(basicword,Word)):
			word = basicword.word
		else:
			print "Big problems, basicword doesn't exist, but we need it because we are a dash" + basicword
	if("/" in word or "|" in word):
		equivalentwords = word.split(" / " if "/" in word else " | ")
		equivalentword = createWord(equivalentwords[0], pos, inflection, basicword, 0, None, equivalentword)
		returninglist = equivalentword
		del equivalentwords[0]
		for w in equivalentwords:
			newwords = createWord(w, pos, inflection, basicword, lesspreferred, preferredword, equivalentword[0])
			for neww in newwords:
				equivalentword[0].equivalentword = neww
			returninglist.extend(newwords)
		#print returninglist
		return returninglist
	if(" " in word):
		preferredwords = word.split(" ")
		preferredword = createWord(preferredwords[0], pos, inflection,basicword,lesspreferred,preferredword,equivalentword)
		returninglist = preferredword
		del preferredwords[0]
		for lpw in preferredwords:
			returninglist.extend(createWord(lpw,pos,inflection,basicword,1,preferredword,equivalentword))
		return returninglist
	test = False
	for i in word:
		ordnum = ord(i.lower())
		if(not(97<=ordnum<=122 or ordnum==39)):
			test = True
	if(test):
		print word
	else:
		return [Word(word,pos,inflection,basicword,lesspreferred,preferredword,equivalentword)]

referencepartsofspeech = {'N':'Noun','p':'Plural','h':'Noun Phrase','V':'Verb usuary participle','t':'Transitive verb','i':'Intransitive verb','A':'Adjective','v':'Adverb','C':'Conjunction','P':'Preposition','!':'Interjection','r':'Pronoun','D':'Definite article','l':'Indefinite article','o':'Nominative'}
POSFILE = 2 # 1=pos.txt, 2=2of12id.txt


class WordPossibilities:
	wordprobabilities = []
	current = 0
	def __init__(self, word):
		self.wordprobabilities = []
		justwords = findWords(word)
		if(isinstance(justwords,list)):
			probability = 1/len(justwords)
			for w in justwords:
				self.wordprobabilities.append([w,probability])
	
	def __getitem__(self, key):
		listtotake = []
		for w in self.wordprobabilities:
			listtotake.append(w[0])
		return listtotake[key]
	
	def __len__(self):
		return len(self.wordprobabilities)
	
	def __repr__(self):
		return self.wordprobabilities.__repr__()
	
	def index(self, key):
		for w in self.wordprobabilities:
			if(key in w):
				return self.wordprobabilities.index(w)
		return None
	
	def __delitem__(self, key):
		del self.wordprobabilities[key]


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
		return self.pos
	
	def isVerb(self):
		if(self.pos=="V"):
			return True
		return False
	
	def __repr__(self):
		return self.word+" "+str(self.pos)#+","+str(self.inflection)+"'" + (" an inflection of "+self.basicword.word if isinstance(self.basicword,Word) else "")
	
	def __eq__(self, other):
		return (isinstance(other, self.__class__) and self.__dict__ == other.__dict__)
	
	def __ne__(self, other):
		return not self.__eq__(other)


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
				mainword = createWord(wordpos[0], wordpos[1],0)
				mainword = mainword[0]
				self.addPOStoWord(mainword)
				if(wordpos[0]=="be" or wordpos[0]=="@wit"):
					if(wordpos[0]=="be"):
						# Do the word be entirely manually, it is not worth writing generic code for one entry in the entire file
						mainword = Word("be","V",0)
						self.addPOStoWord(mainword)
						pasttense = Word("were","V",1,mainword)
						self.addPOStoWord(pasttense)
						pasttense2 = Word("been","V",1,mainword)
						self.addPOStoWord(pasttense2)
						ingtense = Word("being","V",2,mainword)
						self.addPOStoWord(ingtense)
						present1 = Word("am","V",0,mainword)
						self.addPOStoWord(present1)
						present2 = Word("is","V",0,mainword)
						self.addPOStoWord(present2)
						present3 = Word("are","V",3,mainword)
						self.addPOStoWord(present3)
						auxillary = Word("be","v",0)
						self.addPOStoWord(auxillary)
				else:
					# For all normal words split the part after the colon and call it the inflections
					inflections = parts[1].split("  ")
					if(wordpos[1]=="V" and len(parts[1])>0):
						# The format for inflections is <past tense>  [<past participle>]  <-ing form>  <plural form>
						# the ing form of a word always has "ing" at the end of it therefor we can use it as a marker
						mode = 1 # 1 is before the ing word, 2 is after the ing wword
						pasttense = 0 # 0 is if the past tense hasn't happened, becomes one when we get the past tense
						for word in inflections: #Cycle through all the words
							if(mode==1):
								#We are before the ing word
								if(len(inflections)==3 and word=="-" and not(mode==2)): # This is a special test which checks if we have a dash where the ing word should be and then simply pretends that we found an ing word
									mode=2
								elif(word[-3:]=="ing" or word[-4:]=="ing)"): # Test if this is the ing word
									inflectedword = createWord(word,"V",3,mainword)
									self.addPOStoWord(inflectedword)
									mode=2
								else:
									if(pasttense == 0):
										inflectedword = createWord(word,"V",1,mainword)
										pasttense = 0
									else:
										inflectedword = createWord(word,"V",2,mainword)
									self.addPOStoWord(inflectedword)
							elif(mode==2):
								inflectedword = createWord(word,"V",4,mainword)
								self.addPOStoWord(inflectedword)
					elif(wordpos[1]=="A"):
						if(len(inflections)>1 and inflections[0]):
							#check
							erform = createWord(inflections[0],"A",1,mainword)
							estform = createWord(inflections[1],"A",2,mainword)
							self.addPOStoWord(erform)
							self.addPOStoWord(estform)
						elif(len(inflections)>0 and inflections[0]):
							print "Problems with "+line
					elif(wordpos[1]=="N"):
						if(len(inflections)>0 and inflections[0]):
							plural = createWord(inflections[0],"N",1,mainword)
							self.addPOStoWord(plural)
					else:
						if(len(inflections)>0):
							pass
							#print line
		#print self.lines['be']
	
	def addPOStoWord(self,wordobject):
		word = ""
		if(isinstance(wordobject,Word)):
			word = wordobject.word
		elif(isinstance(wordobject,list)):
			for wo in wordobject:
				self.addPOStoWord(wo)
			return
		if(word in self.lines):
			self.lines[word].append(wordobject)
		else:
			self.lines[word] = [wordobject]
	
	def findpartsofspeech(self, word):
		if(word in self.lines):
			return self.lines[word]


posinst = PartsOfSpeech()
