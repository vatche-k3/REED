import spacy

doc =  textacy.io.spacy.read_spacy_docs('lorem.txt', lang='en')

print(doc)

for token in doc:
    print(token.text, token.dep_, token.head.text, token.head.pos_,
            [child for child in token.children])
