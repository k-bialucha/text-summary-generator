import morfeusz2
from read_sentences import read_sentences
from convert_to_base_words import convert_to_base_words

sentences = read_sentences("input.txt")

sentence = sentences[1]

morfeusz = morfeusz2.Morfeusz()

analysis = morfeusz.analyse(sentence)

sentenceWords = []

baseWords = convert_to_base_words(sentence)

print(sentence)
print(baseWords)
