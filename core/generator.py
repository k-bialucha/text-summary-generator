from core.convert_to_base_words import convert_to_base_words
from core.create_word_ranking import create_word_ranking
from core.rank_sentences import rank_sentences
from core.enhance_original_sentences import enhance_original_sentences
from core.create_summary import create_summary


class SummaryGenerator:
    config = {
        "summary_percent": 40,
        "ranking_aging": 0,
    }

    def summarize(self, input_sentences):
        base_form_sentences = []

        for sentence in input_sentences:
            base_words = convert_to_base_words(sentence)
            base_form_sentences.append(base_words)

        word_ranking = create_word_ranking(base_form_sentences)

        sentences_ranked = rank_sentences(
            base_form_sentences, word_ranking, self.config["ranking_aging"])

        original_sentences_ranked = enhance_original_sentences(
            input_sentences, sentences_ranked)

        return create_summary(original_sentences_ranked, self.config["summary_percent"])
