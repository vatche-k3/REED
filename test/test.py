import spacy
from spacy import displacy
from spacy.matcher import Matcher
from rake_nltk import Rake
from hashMap import MyHashMap

r = Rake()

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

doc =  open('lorem.txt')

data = doc.read()
t = nlp(data)
hm = MyHashMap()
#r.extract_keywords_from_text(data)
#print(r.get_ranked_phrases())
#displacy.serve(i, style="ent")

collect = []
verb = []
check = 0
string = ""
i = 0


for token in t:
    
    lemma = token.lemma_
    if(lemma == "collect" or check == 1):
        check = 1
        if(token.pos_ )
        string += " "
        string += token.text

    if(token.text == "." and check == 1):
        check = 0
        hm.put(i, string)
        i += 1
        string = ""

for j in range(i):
    print(hm.get(j))
        
    

    # print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            # token.shape_, token.is_alpha, token.is_stop)

