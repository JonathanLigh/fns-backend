import os
import spacy
import en_core_web_sm


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
spacy_nlp_model = en_core_web_sm.load()
