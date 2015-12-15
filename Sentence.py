# coding=utf-8
import Word
from xml.dom.minidom import parse
import xml.dom.minidom

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
				self.words.append(Word.findWords(word))
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
			#pos = word.getPOS()
			if(len(word)==1):
				if(word[0].pos=="V"):
					definiteverbs.append(word[0])
					print word
				else:
					verbfound = False
					for w in word:
						if(w.pos=="V"):
							possibleverbs.append(w)
		if(len(definiteverbs)==0 and len(possibleverbs)==0):
			return("No verbs, this phrase must be a fragment")
		if(len(possibleverbs)==0):
			return definiteverbs
		if(len(definiteverbs)==0 and len(possibleverbs)==1):
			return possibleverbs
		phrasestructure = Phrase.split(" ")
		for part in phrasestructure:
			pass
		#print possibleverbs
		#print definiteverbs
	def decipherSentenceDefinition():
		pass
		# Open XML document using minidom parser
		#DOMTree = xml.dom.minidom.parse("sentence.xml")
		#collection = DOMTree.documentElement
		#if collection.hasAttribute("shelf"):
		#   print "Root element : %s" % collection.getAttribute("shelf")
		#
		# Get all the movies in the collection
		#movies = collection.getElementsByTagName("movie")
		
		# Print detail of each movie.
		#for movie in movies:
		#   print "*****Movie*****"
		#   if movie.hasAttribute("title"):
		#	  print "Title: %s" % movie.getAttribute("title")
		#
		#   type = movie.getElementsByTagName('type')[0]
		#   print "Type: %s" % type.childNodes[0].data
		#   format = movie.getElementsByTagName('format')[0]
		#   print "Format: %s" % format.childNodes[0].data
		#   rating = movie.getElementsByTagName('rating')[0]
		#   print "Rating: %s" % rating.childNodes[0].data
		#   description = movie.getElementsByTagName('description')[0]
		#   print "Description: %s" % description.childNodes[0].data
class NounPhrase:
	pass

class VerbPhrase:
	pass
	
class PrepositionalPhrase:
	pass