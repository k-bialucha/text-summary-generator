from core.summarize import summarize


def set_output(output, text, percent, aging, start_range, start_weight, end_range, end_weight, debug):

    lines = text.splitlines()
    sentences = []

    for sentence in lines:
        sentences.append(sentence)

    summary_sentences = summarize(sentences, percent, aging, start_range, start_weight, end_range, end_weight, debug)
    summary = ''.join(summary_sentences)
    output.config(text=summary)

    print('SUMMARY')
    print(summary_sentences)
