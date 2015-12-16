# coding=utf-8
import Sentence

# Now to figure out which part of speech something is
sentence = "I am blue"#raw_input("Please put in the sentence:\n")
sentence = Sentence.Sentence(sentence.lower().split(" "))
#print sentence.findPrepositions()
#print sentence.findVerbs()
print sentence.decipherSentenceDefinition()