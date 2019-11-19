from read_sentences import read_sentences
from core.generator import SummaryGenerator
from write_sentences import write_sentences

sentences = read_sentences("input.txt")

generator = SummaryGenerator()

summary_sentences = generator.summarize(sentences)

write_sentences("output.txt", summary_sentences)

print('SUMMARY')
print(summary_sentences)
