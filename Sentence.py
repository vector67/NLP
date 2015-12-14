# coding=utf-8
import Word
class Sentence:
	punctuation = ""
	def __init__(self, words):
		if(len(words)>0 and isinstance(words[0],Word.Word)):
			self.words = words
		elif(isinstance(words,list)):
			self.words = []
			if(not(97<=ord(words[-1][-1].lower())<=122)):
				self.punctuation = words[-1][-1]
				words[-1] = words[-1][:-1]
			for word in words:
				self.words.append(Word.Word(word))
		elif(isinstance(words,str)):
			self.words = []
			if(not(97<=ord(words[-1].lower())<=122)):
				self.punctuation = words[-1]
				words = words[:-1]
			wordarray = words.split(" ")
			for word in wordarray:
				self.words.append(Word.Word(word))
		else:
			raise TypeError("Problems")
	def __repr__(self):
		return self.words.__repr__()
	def findVerbs(self):
		possibleverbs = []
		definiteverbs = []
		for word in self.words:
			pos = word.getPOS()
			if(pos=="V" or pos=="t" or pos=="i"):
				definiteverbs.append(word)
				print word
			elif("V" in pos or "t" in pos or "i" in pos):
				possibleverbs.append(word)
		if(len(definiteverbs)==0 and len(possibleverbs)==0):
			return("No verbs, this phrase must be a fragment")
		if(len(possibleverbs)==0):
			return definiteverbs
		if(len(definiteverbs)==0 and len(possibleverbs)==1):
			return possibleverbs
		#print possibleverbs
		#print definiteverbs

Phrase = "{NounPhrase VerbPhrase(includes adverbs) Directobject[nounphrase] Indirectobject[nounphrase] Prepositional"
class NounPhrase:
	pass

class VerbPhrase:
	pass
	
class PrepositionalPhrase:
	pass