from read_sentences import read_sentences
from process_sentences import process_sentences
from write_sentences import write_sentences

sentences = read_sentences("input.txt")

summary_sentences = process_sentences(sentences)

write_sentences("output.txt", summary_sentences)

print('SUMMARY')
print(summary_sentences)
