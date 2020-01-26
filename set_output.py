import tkinter as tk
from core.generator import SummaryGenerator


def set_output(output, text, percent, aging, start_range, start_weight, end_range, end_weight, debug, ignored_words, use_special_words):
    config = {
        "summary_percent": percent,
        "ranking_aging": aging,
        "segment_boost": [(0, start_range, start_weight), (100 - end_range, 100, end_weight)],
        "debug": debug,
        "ignored_words": ignored_words,
        "use_special_words": use_special_words
    }

    generator = SummaryGenerator()
    generator.config = config

    sentences = text.splitlines()

    summary_sentences = generator.summarize(sentences)
    summary = '\n'.join(summary_sentences)

    output.config(state=tk.NORMAL)
    output.delete("1.0", tk.END)
    output.insert("end-1c", summary)
    output.config(state=tk.DISABLED)
