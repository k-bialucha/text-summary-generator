import morfeusz2

morfeusz = morfeusz2.Morfeusz()


def partition_to_sentences(input):
    analysis = morfeusz.analyse(input)

    for i, j, interpretation in analysis:
        symbol = interpretation[0]

        if symbol == '.':
            print('dot', i, j)
