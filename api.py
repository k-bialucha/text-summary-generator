from flask import Flask, jsonify

from core.generator import SummaryGenerator
from read_sentences import read_sentences


app = Flask(__name__)

generator = SummaryGenerator()


@app.route('/')
def output_sentences():
    sentences = read_sentences("input.txt")

    # TODO: add SummaryGenerator config support
    summary_sentences = generator.summarize(sentences)

    return jsonify(summary_sentences)
