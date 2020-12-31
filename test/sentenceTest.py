import spacy
from spacy import displacy
from spacy.matcher import Matcher
from rake_nltk import Rake
from hashMap import MyHashMap

display = ""

r = Rake()

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

doc =  open('lorem.txt')

data = doc.read()

hm = MyHashMap()
sentencizer = nlp.create_pipe("sentencizer")
nlp.add_pipe(sentencizer)
t = nlp(data)
i = 0
for sent in t.sents:
    for token in sent:
        if(token.lemma_ == "collect"):
            hm.put(i, sent.text)
            i+=1
            break

for j in range(i):
    display += hm.get(j)
    display += " "
displacy.serve(nlp(display), style="ent")
    
#r.extract_keywords_from_text(data)
#print(r.get_ranked_phrases())
#displacy.serve(i, style="ent")



        
    

    # print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            # token.shape_, token.is_alpha, token.is_stop)

