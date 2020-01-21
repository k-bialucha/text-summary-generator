from core.summarize import summarize
import tkinter as tk


def set_output(output, text, percent, aging, start_range, start_weight, end_range, end_weight, debug, ignore, use_special_words):
    lines = text.splitlines()
    sentences = []

    for sentence in lines:
        sentences.append(sentence)

    summary_sentences = summarize(
        sentences, percent, aging, start_range, start_weight, end_range, end_weight, debug == 1, ignore, use_special_words == 1)
    summary = '\n'.join(summary_sentences)

    output.config(state=tk.NORMAL)
    output.delete("1.0", tk.END)
    output.insert("end-1c", summary)
    output.config(state=tk.DISABLED)
