def create_word_ranking(base_form_sentences):
    word_rank = dict()

    for sentence_base_words in base_form_sentences:
        for base_word in sentence_base_words:
            current_word_count = word_rank.get(base_word)

            if current_word_count:
                word_rank[base_word] = current_word_count + 1
            else:
                word_rank[base_word] = 1

    return word_rank
