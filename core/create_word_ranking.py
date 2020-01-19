special_words = {
    "aparat": 2,
    "pamięć": 2,
    "premiera": 2,
    "procesor": 2,
    "świetny": 2,
    "RAM": 2,
    "wspaniały": 2,
    "wymiary": 2,
    "ekran": 1.8,
    "wyświetlacz": 1.8,
    "aktualizacja": 1.7,
    "akumulator": 1.7,
    "bateria": 1.7,
    "cena": 1.7,
    "drogi": 1.7,
    "tani": 1.7,
    "wersja": 1.7,
    "android": 1.5,
    "iOS": 1.5,
    "producent": 1.3,
    "interfejs": 1.3,
}


def create_word_ranking(base_form_sentences):
    word_rank = dict()

    for sentence_base_words in base_form_sentences:
        for base_word in sentence_base_words:
            current_word_ranking = word_rank.get(base_word)

            importance = 1
            if special_words.get(base_word) != None:
                importance = special_words.get(base_word)

            if current_word_ranking:
                word_rank[base_word] = current_word_ranking + importance
            else:
                word_rank[base_word] = importance

    return word_rank
