from core.convert_to_base_words import convert_to_base_words
from core.create_word_ranking import create_word_ranking
from core.rank_sentences import rank_sentences
from core.enhance_original_sentences import enhance_original_sentences
from core.create_summary import create_summary
from core.remove_blocked_words import remove_blocked_words


class SummaryGenerator:
    config = {
        "summary_percent": 40,
        "ranking_aging": 5,
        "segment_boost": [(0, 15, 20), (85, 100, 15)],
        "debug": False,
        "ignored_words": "",
        "use_special_words": True
    }

    def summarize(self, sentences):
        base_form_sentences = []

        for sentence in sentences:
            base_words = convert_to_base_words(sentence)
            base_words = remove_blocked_words(
                base_words, self.config["ignored_words"])
            base_form_sentences.append(base_words)

        word_ranking = create_word_ranking(
            base_form_sentences, self.config["use_special_words"])

        sentences_ranked = rank_sentences(
            base_form_sentences, word_ranking, self.config["ranking_aging"])

        original_sentences_ranked = enhance_original_sentences(
            sentences, sentences_ranked, self.config["segment_boost"])

        return create_summary(original_sentences_ranked, self.config["summary_percent"], self.config["debug"])
