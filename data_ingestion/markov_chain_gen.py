import markovify
import spacy
import re

#   natural language processing object for picking parts of speech
nlp = spacy.load("en")


#   markovify's github page recommended we use spacy to override functions for much better performance on large entries


class POSifiedText(markovify.Text):

    def word_split(self, sentence):
        return ["::".join((word.orth_, word.pos)) for word in nlp(sentence)]

    def word_join(self, words):
        sentence = " ".join(word.split("::")[0] for word in words)
        return sentence


"""
takes:
    data - array of text, could be either array of article titles, or array of article descriptions
    model_json - JSON object of pre-existing model (if none is provided, it will create and return a new one)
returns:
    updated markov model in JSON format
"""


def update_markov_model_json(data, model_json):

    #   reconstitutes markov model from json
    if model_json:
        model = markovify.Text.from_json(model_json)
    else:
        model = None

    for phrase in data:
        new_model = markovify.Text(phrase, retain_original=False)
        if model:
            model = markovify.combine(models=[new_model, model])
        else:
            model = new_model

    return model.to_json()

"""
    model_json - JSON object of markov model
"""


def gen_title_from_model_json(model_json):
    #   got optimal article character length from here: https://coschedule.com/blog/best-headline-length/
    return markovify.Text.from_json(model_json).make_short_sentence(max_chars=120, min_chars=60)