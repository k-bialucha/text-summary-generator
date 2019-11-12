import morfeusz2
from read_sentences import read_sentences
from convert_to_base_words import convert_to_base_words
from create_word_ranking import create_word_ranking

sentences = read_sentences("input.txt")

base_form_sentences = []

for sentence in sentences:
    base_words = convert_to_base_words(sentence)
    base_form_sentences.append(base_words)

word_ranking = create_word_ranking(base_form_sentences)
# sentences_ranked = rank_sentences()

print(base_form_sentences)
print(word_ranking)
