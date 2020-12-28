import spacy
nlp = spacy.load("en_core_web_sm")
doc =  open('lorem.txt')

data = doc.read()

i = nlp(data)

for token in i:
    print(token.text, token.dep_, token.head.text, token.head.pos_,
            [child for child in token.children])
