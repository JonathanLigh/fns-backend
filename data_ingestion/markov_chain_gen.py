import markovify
import spacy
import random

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
takes:
    model_json - JSON object of title markov model
returns:
    generated title of an article
"""


def gen_title_from_model_json(model_json):
    model = markovify.Text.from_json(model_json)
    title = None
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
    parsed_sentence = ParsedSentence(article_title)
    subject: str = parsed_sentence.subject
    model = markovify.Text.from_json(model_json)
    article: str = ""
    for i in range(random.randint(5, 10)):
        sentence: None = None
        while sentence is None:
                sentence: str = model.make_sentence_with_start(beginning=subject)
        parsed_sentence = ParsedSentence(sentence)

        article: str = article + ' ' + sentence

        #   now we choose the subject of the next sentence
        if parsed_sentence.direct_object is not None:
            subject = parsed_sentence.direct_object
        elif parsed_sentence.indirect_object is not None:
            subject = parsed_sentence.indirect_object
        elif parsed_sentence.subject is not None:
            subject = parsed_sentence.subject
        #   if the previous sentence does not contain a direct object, indirect object, or subject,
        #   we continue with the same subject

    return article


"""
Class purpose:
    defining an interpreted sentence's logical structural components. 
    I.E. it's subject, direct objcet, and indirect object
    
"""


class ParsedSentence:
    subject = ""
    direct_object = ""
    indirect_object = ""

    """
    takes:
        sentence - string that represents a sentence
    returns:
        ParsedSentence containing the subject, indirect object, and direct object of that sentence
    """


    def __init__(self, sentence):
        text = nlp(sentence)
        for word in text:
            if word.dep_ == "nsubj":
                self.subject = word.orth_
            if word.dep_ == "iobj":
                self.indirect_object = word.orth_
            if word.dep_ == "dobj":
                self.direct_object = word.orth_




