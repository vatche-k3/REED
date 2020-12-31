import spacy
from spacy.matcher import Matcher
from spacy.tokens import Span
from spacy.util import filter_spans 

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)
doc =  open('lorem.txt')
data = doc.read()

matcher = Matcher(nlp.vocab)
#pattern = [{"LEMMA": "collect", "POS": "VERB"}, {"POS": "DET", "OP": "?"}, {"POS": "NOUN"}]
#pattern = [{"LEMMA": "collect", "POS": "VERB"}, {"POS": "NOUN" , "OP": "*"}, {"POS": "DET", "OP": "?"}, {"POS": "NOUN", "OP": "+"}]
pattern = [{"LEMMA": "collect", "POS": "VERB"}, {"OP": "*"}, {"TEXT": "."}]
matcher.add("Collect", None, pattern)
text = nlp(data)
matches = matcher(text)

for match_id, start, end in matches:
    matched_span = text[start:end]
    print(matched_span.text)