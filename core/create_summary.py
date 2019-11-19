def sortByRanking(val):
    return val[1]


def sortByOriginalOrder(val):
    return val[2]


def create_summary(original_sentences_ranked, summary_ratio):
    original_sentences_ranked.sort(key=sortByRanking, reverse=True)

    top_sentences_count = round(len(original_sentences_ranked) * summary_ratio)

    top_sentences = original_sentences_ranked[0:top_sentences_count]

    top_sentences.sort(key=sortByOriginalOrder)

    summary_sentences = []

    for enhanced_sentence in top_sentences:
        summary_sentences.append(enhanced_sentence[0])

    return summary_sentences
