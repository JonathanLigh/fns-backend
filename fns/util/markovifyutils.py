import markovify
import random

from definitions import spacy_nlp_model
from fns.structure.text import NLPText, NLPSentence


def gen_sentence(model: NLPText, subject: str) -> str:
    sentence: str = None
    i = 0
    limit = 100
    while sentence is None:
        sentence = model.make_sentence_with_start(beginning=subject) + ' '
        if i is limit:
            sentence = ''
            break
        else:
            i += 1
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
        model = NLPText.from_json(model_json)
    else:
        model = None

    for phrase in data:
        new_model = NLPText(phrase, retain_original=False)
        if model:
            model = markovify.combine(models=[new_model, model])
        else:
            model = new_model

    return model.to_json()


"""
takes:
    model_json - JSON object of title markov model
returns:
    generated title of an article
"""


def gen_title_from_model_json(model_json):
    model = NLPText.from_json(model_json)
    title: str = None
    i = 0
    limit = 100
    while title is None:
        title = model.make_short_sentence(max_chars=120, min_chars=60)
    #   got optimal article character length from here: https://coschedule.com/blog/best-headline-length/
    return title


"""
takes:
    model_json - JSON object of article markov model
    article_title - string of article title
returns:
    generated paragraph of an article
"""


def gen_article_from_model_json(model_json, article_title):
    parsed_tokens = spacy_nlp_model(article_title)
    parsed_sentence = NLPSentence(parsed_tokens)

    subject = parsed_sentence.subj_tokens
    model = NLPText.from_json(model_json)

    article = ""

    for i in range(random.randint(5, 10)):
        article = article + gen_sentence(model=model, subject=subject)

        #   now we choose the subject of the next sentence
        if parsed_sentence.dobj_tokens is not None:
            subject = parsed_sentence.dobj_tokens
        elif parsed_sentence.iobj_tokens is not None:
            subject = parsed_sentence.iobj_tokens
        elif parsed_sentence.subj_tokens is not None:
            subject = parsed_sentence.subj_tokens
        #   if the previous sentence does not contain a direct object, indirect object, or subject,
        #   we continue with the same subject

    return article
