from flask import Flask, jsonify
from convert_to_base_words import convert_to_base_words
from read_sentences import read_sentences
from core.generator import SummaryGenerator

generator = SummaryGenerator()


app = Flask(__name__)


@app.route('/')
def output_sentences():
    sentences = read_sentences("input.txt")

    summary_sentences = generator.summarize(sentences)
    return jsonify(summary_sentences)
