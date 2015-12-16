# coding=utf-8
import Word
from xml.dom.minidom import parse
import xml.dom.minidom

class Sentence:
	punctuation = ""
	def __init__(self, wordlist):
		if(len(wordlist)>0 and isinstance(wordlist[0],Word.Word)):
			self.words = wordlist
		elif(isinstance(wordlist,list)):
			self.words = []
			if(not(97<=ord(wordlist[-1][-1].lower())<=122)):
				self.punctuation = wordlist[-1][-1]
				wordlist[-1] = wordlist[-1][:-1]
			for word in wordlist:
				tobeadded = Word.WordPossibilities(word)
				self.words.append(tobeadded)
		elif(isinstance(wordlist,str)):
			self.words = []
			if(not(97<=ord(wordlist[-1].lower())<=122)):
				self.punctuation = wordlist[-1]
				wordlist = wordlist[:-1]
			wordarray = wordlist.split(" ")
			for word in wordarray:
				self.words.append(Word.WordPossibilities(word))
		else:
			raise TypeError("Problems")
		self.cullUselessInflections()

	def cullUselessInflections(self):
		for wordlist in self.words:
			for word1 in wordlist:
				for word2 in wordlist:
					if(not(word1 is word2)):
						if(word1.pos == word2.pos):
							del wordlist[wordlist.index(word1)]
	def __repr__(self):
		return self.words.__repr__()
	def findVerbs(self):
		possibleverbs = []
		definiteverbs = []
		for word in self.words:
			#pos = word.getPOS()
			if(len(word)==1):
				if(word[0].pos=="V" and not(word[0].inflection==3)):
					definiteverbs.append(self.words.index(word))
			elif(len(word)>0):
				for w in word:
					if(w.pos=="V"):
						possibleverbs.append(self.words.index(word))
		if(len(definiteverbs)==0 and len(possibleverbs)==0):
			return("No verbs, this phrase must be a fragment")
		if(len(possibleverbs)==0):
			return definiteverbs
		if(len(definiteverbs)==0 and len(possibleverbs)==1):
			return possibleverbs
		return [definiteverbs, possibleverbs]
	def findPrepositions(self):
		possibleprepositions = []
		definiteprepositions = []
		for word in self.words:
			#pos = word.getPOS()
			if(len(word)==1):
				if(word[0].pos=="p"):
					possibleprepositions.append(word[0])
				else:
					verbfound = False
					for w in word:
						if(w.pos=="p"):
							possibleprepositions.append(w)
		return possibleprepositions
		
	def decipherSentenceDefinition(self):
		possibleprepositions = self.findPrepositions()
		verbs = self.findVerbs()
		definiteverbs = verbs[0]
		possibleverbs = verbs[1]
		#print verbs
		#for v in verbs:
		#	posswords = self.words[v]
		#	if(len(posswords)==1):
		#		definiteverbs.append(posswords)
		if(len(definiteverbs)==1):
			pass #Found a verb
		possibilities = self.recursivelyGetPossibilities(0,[])
		print len(possibilities)
		for possibility in possibilities:
			verb = False
			for word in possibility:
				if(word.isVerb()):
					verb = True
			if(not(verb)):
				del possibilities[possibilities.index(possibility)]
		print len(possibilities)
		return possibilities
	
	def recursivelyGetPossibilities(self, level, sofar):
		returning = []
		#print level
		#print sofar
		#print ""
		for word in self.words[level]:
			if(level==(len(self.words)-1)):
				newar = sofar[:]
				newar.append(word)
				returning.append(newar)
			else:
				newar = sofar[:]
				newar.append(word)
				returning.extend(self.recursivelyGetPossibilities(level+1,newar))
		return returning
			
class NounPhrase:
	pass

class VerbPhrase:
	pass
	
class PrepositionalPhrase:
	pass