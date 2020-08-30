"""

"""
import abc

__author__ = ["Clément Besnier <clemsciences@aol.com>", ]


class POSFeatures:

    def __init__(self):
        self.masculine = False
        self.feminine = False
        self.neuter = False
        self.singular = False
        self.plural = False
        self.dual = False
        self.nominative = False
        self.accusative = False
        self.dative = False
        self.genitive = False
        self.definite = False
        self.indefinite = False
        self.positive = False
        self.comparative = False
        self.superlative = False
        self.first = False
        self.second = False
        self.third = False
        self.indicative = False
        self.subjunctive = False
        self.imperative = False
        self.present = False
        self.preterite = False
        self.active = False
        self.reflexive = False
        self.infinitive = False
        self.participle = False
        self.strong = False
        self.weak = False
        self.reduplicating = False
        self.preterito_present = False
        self.noun = False
        self.proper_noun = False
        self.adjective = False
        self.article = False
        self.demonstrative = False
        self.indefinite_demonstrative = False
        self.possessive = False
        self.personal = False
        self.interrogative = False
        self.relative = False
        self.numeral = False
        self.verb = False
        self.adverb = False
        self.conjunction = False
        self.foreign = False
        self.punctuation = False
        self.unanalysed = False

    def __eq__(self, other):
        for i in range(len(self.vectorize())):
            if self.vectorize()[i] != other.vectorize()[i]:
                return False
        return True

    def vectorize(self):
        return [
            self.masculine,
            self.feminine,
            self.neuter,
            self.singular,
            self.plural,
            self.dual,
            self.nominative,
            self.accusative,
            self.dative,
            self.genitive,
            self.definite,
            self.indefinite,
            self.positive,
            self.comparative,
            self.superlative,
            self.first,
            self.second,
            self.third,
            self.indicative,
            self.subjunctive,
            self.imperative,
            self.present,
            self.preterite,
            self.active,
            self.reflexive,
            self.infinitive,
            self.participle,
            self.strong,
            self.weak,
            self.reduplicating,
            self.preterito_present,
            self.noun,
            self.proper_noun,
            self.adjective,
            self.article,
            self.demonstrative,
            self.indefinite_demonstrative,
            self.possessive,
            self.personal,
            self.interrogative,
            self.relative,
            self.numeral,
            self.verb,
            self.adverb,
            self.foreign,
            self.punctuation,
            self.unanalysed
        ]


class POSElement:

    @staticmethod
    @abc.abstractmethod
    def parse(tag, value):
        return value

    @staticmethod
    @abc.abstractmethod
    def binarize(tag, features):
        pass


class POSAbstract:
    """

    """

    @staticmethod
    @abc.abstractmethod
    def apply(tag, l_pos, value):
        """

        :param tag:
        :param l_pos:
        :param value:
        :return:
        """
        pass

    @staticmethod
    @abc.abstractmethod
    def binarize(tag, l_pos, value):
        """

        :param tag: POS tag
        :param l_pos:
        :param value:
        :return:
        """
        pass

    @staticmethod
    @abc.abstractmethod
    def parse(full_tag, vector=False):
        """

        :param full_tag: Pars oratori in annotated documents
        :param vector:
        :return: readable form of the POS tag
        """
        pass
