from flask import Flask, jsonify
from convert_to_base_words import convert_to_base_words
from read_sentences import read_sentences

app = Flask(__name__)


@app.route('/')
def output_sentences():
    sentences = read_sentences("input.txt")

    return jsonify([convert_to_base_words(sentence) for sentence in sentences])
