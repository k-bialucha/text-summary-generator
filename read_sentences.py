def read_sentences(file_path):
    input = open(file_path, "r")

    lines = input.readlines()
    sentences = []

    for sentence in lines:
        sentences.append(sentence)

    input.close()

    return sentences
