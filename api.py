from flask import Flask, jsonify

from core.summarize import summarize
from read_sentences import read_sentences


app = Flask(__name__)


@app.route('/')
def output_sentences():
    sentences = read_sentences("input.txt")

    summary_sentences = summarize(sentences)
    return jsonify(summary_sentences)
