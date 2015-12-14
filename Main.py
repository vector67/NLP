# coding=utf-8
import Sentence
import Word

# Now to figure out which part of speech something is
sentence = raw_input("Please put in the sentence:\n")
sentence = Sentence.Sentence(sentence.lower().split(" "))
print sentence.findVerbs()
print sentence	