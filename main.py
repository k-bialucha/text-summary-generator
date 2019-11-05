import morfeusz2
from partition_to_sentences import partition_to_sentences

sentence = 'Sercem realme X2 jest jeden z najwydajniejszych procesorów na rynku, tj. ośmiordzeniowy (8x Kryo 470; 8 nm). Telefon posiada aż 256 GB na pliki użytkownika.'

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
