import markovify

from definitions import spacy_nlp_model
from fns.constant.strconst import StringConstants


class NLPText(markovify.Text):
    def word_split(self, sentence):
        return [StringConstants.TAB.join((word.orth_, word.pos_)) for word in spacy_nlp_model(sentence)]

    def word_join(self, words):
        sentence = StringConstants.SPACE.join(word.split(StringConstants.TAB)[0] for word in words)
        return sentence


class NLPSentence:
    def __init__(self, tokens):
        self.tokens = tokens
        self.subj_tokens = self._get_dependency_field("nsubj")
        self.dobj_tokens = self._get_dependency_field("dobj")
        self.iobj_tokens = self._get_dependency_field("iobj")

    def _get_dependency_field(self, dep_field):
        return list(filter(lambda t: t.dep_ == dep_field, self.tokens))
