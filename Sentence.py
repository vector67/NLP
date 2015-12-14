# coding=utf-8
import Word
class Sentence:
	punctuation = ""
	def __init__(self, words):
		if(len(words)>0 and isinstance(words[0],Word.Word)):
			self.words = words
			print "got a word list"
		elif(isinstance(words,list)):
			print "got a string list"
			self.words = []
			if(not(97<=ord(words[-1][-1].lower())<=122)):
				self.punctuation = words[-1][-1]
				words[-1] = words[-1][:-1]
			for word in words:
				self.words.append(Word.Word(word))
		elif(isinstance(words,str)):
			self.words = []
			print ord(words[-1].lower())
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