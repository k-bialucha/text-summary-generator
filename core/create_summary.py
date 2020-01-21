def sortByRanking(val):
    return val[1]


def sortByOriginalOrder(val):
    return val[2]


def create_summary(original_sentences_ranked, summary_percent, debug):
    original_sentences_ranked.sort(key=sortByRanking, reverse=True)

    top_sentences_count = round(
        len(original_sentences_ranked) * summary_percent / 100)

    top_sentences = original_sentences_ranked[0:top_sentences_count]

    top_sentences.sort(key=sortByOriginalOrder)

    summary_sentences = []

    for enhanced_sentence in top_sentences:
        sentence = enhanced_sentence[0]

        if debug:
            original_index = str(enhanced_sentence[2] + 1)
            ranking = ' [' + str(round(enhanced_sentence[1], 2)) + ']\n'

            line = sentence.split('\n')[0]
            summary_sentences.append(original_index + ' ' + line + ranking)
        else:
            summary_sentences.append(sentence)

    return summary_sentences
