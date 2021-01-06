import spacy
from spacy import displacy
from spacy.matcher import Matcher
from rake_nltk import Rake
from hashMap import MyHashMap
import json

def add_values_in_dict(dictionary, key, list_of_values):
    """Append multiple values to a key in the given dictionary"""
    if key not in dictionary:
        dictionary[key] = list()
    dictionary[key].extend(list_of_values)
    return dictionary

display = ""

r = Rake()

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

doc =  open('lorem.txt')
lemma = open('lemma.txt')

data = doc.read()
data2 = lemma.read()

hm = MyHashMap()
sentencizer = nlp.create_pipe("sentencizer")
nlp.add_pipe(sentencizer)
t = nlp(data)
t2 = nlp(data2)
i = 0
dictionary = {}

for word in t2:
    dictionary.setdefault(word.text, [])



#for sent in t.sents:
    #for word in t2:
        #for token in sent:
            #if(token.lemma_ == word.text):
                #hm.put(i, sent.text)
                #i+=1
                #break

for sent in t.sents:
    #for word in dictionary.keys():
        for token in sent:
            if token.lemma_ in dictionary.keys():
                dictionary = add_values_in_dict(dictionary, token.lemma_, [sent.text])
                #dictionary[token.lemma_] = sent.text
                i+=1
                

#for j in range(i):
    #display += hm.get(j)
    #display += " "
#displacy.serve(nlp(display), style="ent")

#for j in range(i):
    #print(hm.get(j))
    #print("------------")

json_object = json.dumps(dictionary, indent = 4)   
print(json_object) 
    
#r.extract_keywords_from_text(data)
#print(r.get_ranked_phrases())
#displacy.serve(i, style="ent")



        
    

    # print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
            # token.shape_, token.is_alpha, token.is_stop)

