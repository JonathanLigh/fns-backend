import os
import spacy


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
spacy_nlp_model = spacy.load("en")
