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
			print self.words[definiteverbs[0]]
			print "found verb"
		
		for (w in self.words):
			for wpos in w:
				
class NounPhrase:
	pass

class VerbPhrase:
	pass
	
class PrepositionalPhrase:
	pass