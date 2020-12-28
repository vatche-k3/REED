import spacy
nlp = spacy.load("en_core_web_sm")
doc =  open('lorem.txt')

data = doc.read()
i = nlp(data)

noun = []
verb = []

for token in i:
    pos = token.pos_
    if(pos == "NOUN"):
        noun.append(token.text)
    elif(pos == "VERB"):
        verb.append(token.text)

    # print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            # token.shape_, token.is_alpha, token.is_stop)

for n in noun:
    print(n)

for v in verb:
    print(v)