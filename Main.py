# coding=utf-8
import Sentence

# Now to figure out which part of speech something is
sentence = "We have gotten this type of signal from a successful input."#raw_input("Please put in the sentence:\n")
#we P, have v, gotten V, this A, type N, of p, signal N, from p, a A, successful A, input N
sentence = Sentence.Sentence(sentence.lower().split(" "))
#print sentence.findPrepositions()
#print sentence.findVerbs()
#print sentence
dsd = sentence.decipherSentenceDefinition()
for i in dsd:
	if(i[1].pos=="v"):
		print i
		print ""