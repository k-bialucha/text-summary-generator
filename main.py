import morfeusz2
from partition_to_sentences import partition_to_sentences

input = open("input.txt", "r")

sentence = input.read()

input.close()

morfeusz = morfeusz2.Morfeusz()

analysis = morfeusz.analyse(sentence)

sentenceWords = []

prev_i = None

for i, j, interpretation in analysis:
    print(i, j, interpretation)
    word = interpretation[1].split(':')[0]

    if i != prev_i:
        sentenceWords.append(word)
    prev_i = i

print(sentenceWords)

partition_to_sentences(sentence)
