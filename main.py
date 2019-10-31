import morfeusz2

sentence = 'Sercem realme X2 jest jeden z najwydajniejszych procesorów na rynku, tj. ośmiordzeniowy (8x Kryo 470; 8 nm). Telefon posiada aż 256 GB na pliki użytkownika.'

morfeusz = morfeusz2.Morfeusz()

analysis = morfeusz.analyse(sentence)

for i, j, interpretation in analysis:
  print(i, j, interpretation)

