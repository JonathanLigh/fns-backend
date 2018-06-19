import markovify
import spacy

from fns.constant.strconst import StringConstants

nlp = spacy.load("en")


class POSifiedText(markovify.Text):
    def word_split(self, sentence):
        return [StringConstants.TAB.join((word.orth_, word.pos_)) for word in nlp(sentence)]

    def word_join(self, words):
        sentence = StringConstants.SPACE.join(word.split(StringConstants.TAB)[0] for word in words)
        return sentence
