def write_sentences(file_path, sentences):
    output_file = open(file_path, "w+")

    for sentence in sentences:
        output_file.write(sentence)

    output_file.close()
