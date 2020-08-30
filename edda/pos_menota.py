"""

"""


from collections import defaultdict
from pos_utils import *


__author__ = ["Clément Besnier <clemsciences@aol.com>", ]


class WordClass:
    identifier = "x"
    noun = "N"
    common_noun = "NC"
    proper_noun = "NP"
    adjective = "AJ"
    pronoun = "P"
    personal_pronoun = "PE"
    interrogative_pronoun = "PQ"
    indefinite_pronouns = "PI"
    possessive = "DP"
    demonstrative = "DD"
    quantifier = "DQ"
    pronoun = "PD"
    number = "N"
    cardinal = "NA"
    ordinal = "NO"
    numeral_undetermined = "NU"
    article = "AT"
    verb = "VB"
    adverb = "AV"
    preposition = "VP"
    adposition = "AP"
    conjunction = "CC"
    subjunction = "CS"
    conjunction_subjunction = "CU"
    interjection = "IT"
    infinitive_marker = "IM"
    relative_particle = "RP"
    expletive_particle = "EX"
    unassigned = "UA"


class Gender(POSElement):
    identifier = "g"
    masculine = "M"
    feminine = "F"
    neuter = "N"
    unspecified = "U"

    verbose = defaultdict(str)
    verbose[masculine] = "masculine"
    verbose[feminine] = "feminine"
    verbose[neuter] = "neuter"
    verbose[unspecified] = "unspecified"

    @staticmethod
    def parse(tag, value):
        return value + " " + Gender.verbose[tag]

    @staticmethod
    def can_apply(tag):
        return tag in Gender.verbose

    @staticmethod
    def binarize(tag, value):
        value.masculine = tag == Gender.masculine
        value.feminine = tag == Gender.feminine
        value.neuter = tag == Gender.neuter
        return value


class Number(POSElement):
    identifier = "n"
    singular = "S"
    dual = "D"
    plural = "P"
    unspecified = "U"

    verbose = defaultdict(str)
    verbose[singular] = "singular"
    verbose[plural] = "plural"
    verbose[dual] = "dual"
    verbose[unspecified] = "unspecified"

    @staticmethod
    def parse(tag, value):
        return value + " " + Number.verbose[tag]

    @staticmethod
    def can_apply(tag):
        return tag in Number.verbose

    @staticmethod
    def binarize(tag, value):
        value.singular = tag == Number.singular
        value.plural = tag == Number.plural
        value.plural = tag == Number.dual
        return value


class Case(POSElement):
    identifier = "c"
    nominative = "N"
    genitive = "G"
    dative = "D"
    accusative = "A"
    oblique = "O"
    unspecified = "U"

    verbose = defaultdict(str)
    verbose[nominative] = "nominative"
    verbose[accusative] = "feminine"
    verbose[genitive] = "genitive"
    verbose[dative] = "dative"
    verbose[oblique] = "oblique"
    verbose[unspecified] = "unspecified"

    @staticmethod
    def parse(tag, value):
        return value + " " + Case.verbose[tag]

    @staticmethod
    def can_apply(tag):
        return tag in Case.verbose

    @staticmethod
    def binarize(tag, value):
        value.nominative = tag == Case.nominative
        value.accusative = tag == Case.accusative
        value.dative = tag == Case.dative
        value.genitive = tag == Case.genitive
        return value


class Species(POSElement):
    identifier = "s"
    indefinite = "I"
    definite = "D"
    unspecified = "U"

    verbose = defaultdict(str)
    verbose[indefinite] = "indefinite"
    verbose[definite] = "definite"
    verbose[unspecified] = "unspecified"

    @staticmethod
    def parse(tag, value):
        return value + " " + Species.verbose[tag]

    @staticmethod
    def can_apply(tag):
        return tag in Species.verbose

    @staticmethod
    def binarize(tag, value):
        value.definite = tag == Species.definite
        value.indefinite = tag == Species.indefinite
        return value


class Grade(POSElement):
    identifier = "r"
    positive = "P"
    comparative = "C"
    superlative = "S"
    unspecified = "U"

    verbose = defaultdict(str)
    verbose[positive] = "positive"
    verbose[comparative] = "comparative"
    verbose[superlative] = "superlative"
    verbose[unspecified] = "unspecified"

    @staticmethod
    def parse(tag, value):
        return value + " " + Grade.verbose[tag]

    @staticmethod
    def can_apply(tag):
        return tag in Grade.verbose

    @staticmethod
    def binarize(tag, value):
        value.positive = tag == Grade.positive
        value.comparative = tag == Grade.comparative
        value.superlative = tag == Grade.superlative
        return value


class Person(POSElement):
    identifier = "p"
    first = "1"
    second = "2"
    third = "3"
    unspecified = "U"

    verbose = defaultdict(str)
    verbose[first] = "first"
    verbose[second] = "second"
    verbose[third] = "third"
    verbose[unspecified] = "unspecified"

    @staticmethod
    def parse(tag, value):
        return value + " " + Person.verbose[tag]

    @staticmethod
    def can_apply(tag):
        return tag in Person.verbose

    @staticmethod
    def binarize(tag, value):
        value.first = tag == Person.first
        value.second = tag == Person.second
        value.third = tag == Person.third
        return value


class Tense(POSElement):
    identifier = "t"
    present = "PS"
    preterite = "PT"
    unspecified = "U"

    verbose = defaultdict(str)
    verbose[present] = "present"
    verbose[preterite] = "preterite"
    verbose[unspecified] = "unspecified"

    @staticmethod
    def parse(tag, value):
        return value + " " + Tense.verbose[tag]

    @staticmethod
    def can_apply(tag):
        return tag in Tense.verbose

    @staticmethod
    def binarize(tag, value):
        value.present = tag == Tense.present
        value.preterite = tag == Tense.preterite
        return value


class Mood(POSElement):
    identifier = "m"
    indicative = "IN"
    subjunctive = "SU"
    imperative = "IP"
    unspecified = "U"

    verbose = defaultdict(str)
    verbose[indicative] = "indicative"
    verbose[subjunctive] = "subjunctive"
    verbose[imperative] = "imperative"
    verbose[unspecified] = "unspecified"

    @staticmethod
    def parse(tag, value):
        return value + " " + Mood.verbose[tag]

    @staticmethod
    def can_apply(tag):
        return tag in Mood.verbose

    @staticmethod
    def binarize(tag, value):
        value.indicative = tag == Mood.indicative
        value.subjunctive = tag == Mood.subjunctive
        value.imperative = tag == Mood.imperative
        return value


class Voice(POSElement):
    identifier = "v"
    active = "A"
    reflexive = "R"
    unspecified = "U"

    verbose = defaultdict(str)
    verbose[active] = "active"
    verbose[reflexive] = "reflexive"
    verbose[unspecified] = "unspecified"

    @staticmethod
    def parse(tag, value):
        return value + " " + Voice.verbose[tag]

    @staticmethod
    def can_apply(tag):
        return tag in Voice.verbose

    @staticmethod
    def binarize(tag, value):
        value.active = tag == Voice.active
        value.reflexive = tag == Voice.reflexive
        return value


class Finitness(POSElement):
    identifier = "f"
    finite = "F"
    infinite = "I"
    participle = "P"
    unspecified = "U"

    verbose = defaultdict(str)
    verbose[finite] = "finite"
    verbose[infinite] = "infinite"
    verbose[participle] = "participle"
    verbose[unspecified] = "unspecified"

    @staticmethod
    def parse(tag, value):
        return value + " " + Finitness.verbose[tag]

    @staticmethod
    def can_apply(tag):
        return tag in Finitness.verbose

    @staticmethod
    def binarize(tag, value):
        value.finite = tag == Finitness.finite
        value.infinite = tag == Finitness.infinite
        value.participle = tag == Finitness.participle
        return value


class InflectionalClass(POSElement):
    identifier = "i"
    strong = "ST"
    weak = "WK"
    reduplicating = "RD"
    preterito_present = "PP"

    verbose = defaultdict(str)
    verbose[strong] = "strong"
    verbose[weak] = "weak"
    verbose[reduplicating] = "reduplicating"
    verbose[preterito_present] = "preterito-present"

    @staticmethod
    def parse(tag, value):
        return value + " " + InflectionalClass.verbose[tag]

    @staticmethod
    def can_apply(tag):
        return tag in InflectionalClass.verbose

    @staticmethod
    def binarize(tag, value):
        value.strong = tag == InflectionalClass.strong
        value.weak = tag == InflectionalClass.weak
        value.reduplicating = tag == InflectionalClass.reduplicating
        value.preterito_present = tag == InflectionalClass.preterito_present
        return value


class Enclitic(POSElement):
    identifier = "e"
    pronoun = "P"
    negative_particle = "N"

    verbose = defaultdict(str)
    verbose[pronoun] = "pronoun"
    verbose[negative_particle] = "negative particle"

    @staticmethod
    def parse(tag, value):
        return value + " " + Enclitic.verbose[tag]

    @staticmethod
    def can_apply(tag):
        return tag in Enclitic.verbose

    @staticmethod
    def binarize(tag, value):
        value.pronoun = tag == Enclitic.pronoun
        value.negative_particle = tag == Enclitic.negative_particle
        return value


class Government(POSElement):
    identifier = "y"
    genitive = "G"
    dative = "D"
    accusative = "A"
    unspecified = "U"
    indicative = "UN"
    subjunctive = "SU"

    verbose = defaultdict(str)
    verbose[genitive] = "genitive"
    verbose[dative] = "dative"
    verbose[accusative] = "accusative"
    verbose[indicative] = "indicative"
    verbose[subjunctive] = "subjunctive"
    verbose[unspecified] = "unspecified gender"

    @staticmethod
    def parse(tag, value):
        return value + " " + Government.verbose[tag]

    @staticmethod
    def can_apply(tag):
        return tag in Government.verbose

    @staticmethod
    def binarize(tag, value):
        value.genitive = tag == Government.genitive
        value.dative = tag == Government.dative
        value.accusative = tag == Government.accusative
        value.indicative = tag == Government.indicative
        value.subjunctive = tag == Government.subjunctive
        return value


DELIMITER = "|"


class POSMenota(POSAbstract):
    noun = "n"
    adjective = "l"
    pronoun = "f"
    article = "g"
    numeral = "t"
    verb = "s"
    adverb = "a"
    conjunction = "c"
    foreign = "e"
    unanalysed = "x"
    punctuation = "p"

    verbose = defaultdict(str)
    verbose[WordClass.common_noun] = "common noun"
    verbose[WordClass.proper_noun] = "proper noun"
    verbose[WordClass.adjective] = "adjective"
    verbose[WordClass.pronoun] = "pronoun"
    verbose[WordClass.article] = "article"
    verbose[WordClass.ordinal] = "ordinal"
    verbose[WordClass.cardinal] = "cardinal"
    verbose[WordClass.numeral_undetermined] = "numeral undetermined"
    verbose[WordClass.verb] = "verb"
    verbose[WordClass.adverb] = "adverb"
    verbose[WordClass.conjunction] = "conjunction"
    verbose[WordClass.subjunction] = "subjunction"
    verbose[WordClass.conjunction_subjunction] = "conjunction or subjunction"
    verbose[WordClass.unassigned] = "unanalysed"
    verbose[WordClass.unassigned] = "unanalysed"
    #     verbose[WordClass.punctuation] = "punctuation"
    #     verbose[WordClass.foreign] = "foreign"

    #     icepac = defaultdict(str)
    #     icepac[WordClass.comm]

    # A universal part-of-speech tagset by Petrov S., Das D., McDonald R.

    universal = defaultdict(str)
    universal[noun] = "NOUN"
    universal[adjective] = "ADJ"
    universal[pronoun] = "PRON"
    universal[article] = "DET"
    universal[numeral] = "NUM"
    universal[verb] = "VERB"
    universal[adverb] = "ADV"  # in this category, belong ADV, ADP and PRT
    universal[conjunction] = "CONJ"
    universal[unanalysed] = "X"
    universal[foreign] = "X"
    universal[punctuation] = "PUNC"

    @staticmethod
    def apply(tag: list, l_pos: list, value: str):
        #         print(tag)
        i = 0
        for pos in l_pos:
            #             print(pos)
            new_value = ""
            if isinstance(pos, list):
                for j in pos:
                    if j.can_apply(tag[i][1:]):
                        new_value = j.parse(tag[i], value)
            elif i < len(tag):
                #                 print(tag[i])
                new_value = pos.parse(tag[i][1:], value)
            #                 print(repr(value))
            if new_value != "" and value + " " != new_value:
                value = new_value
                i += 1
        return value

    @staticmethod
    def binarize(tag: list, l_pos: list, value: POSFeatures) -> POSFeatures:
        #         print(tag)
        i = 0
        new_value = value
        for pos in l_pos:
            # print(pos)
            if isinstance(pos, list):
                for j in pos:
                    if j.can_apply(tag[i][1:]):
                        new_value = j.binarize(tag[i], value)

            elif i < len(tag):
                #                 print(tag[i])
                new_value = pos.binarize(tag[i][1:], value)
            #                 print(repr(value))
            value = new_value
            i += 1
        return value

    @staticmethod
    def parse(full_tag, vector=False):
        """
        >>> POSMenota.parse('xPE p1 nD cN')

        :param full_tag:
        :param vector:
        :return:
        """
        features = POSFeatures()
        tags = full_tag.split(" ")

        first_tag = tags[0][0]
        if WordClass.identifier == first_tag:
            word_class = tags[0][1:]
            #             print(word_class)
            value = ""
            tag = tags[1:]
            if word_class == WordClass.noun:
                features.noun = True
                value = POSMenota.verbose[word_class]
                parsers = [Gender, Number, Case, Species]
                value = POSMenota.apply(tag, parsers, value)
                features = POSMenota.binarize(tag, parsers, features)

            elif word_class == WordClass.proper_noun:
                features.proper_noun = True
                value = POSMenota.verbose[word_class]
                parsers = [Gender, Number, Case, Species]
                value = POSMenota.apply(tag, parsers, value)
                features = POSMenota.binarize(tag, parsers, features)

            elif word_class == WordClass.common_noun:
                features.common_noun = True
                value = POSMenota.verbose[word_class]
                parsers = [Gender, Number, Case, Species]
                value = POSMenota.apply(tag, parsers, value)
                features = POSMenota.binarize(tag, parsers, features)

            elif word_class == WordClass.adjective:
                features.adjective = True
                value = POSMenota.verbose[word_class]
                parsers = [Grade, Gender, Number, Case, Species, Grade]
                value = POSMenota.apply(tag, parsers, value)
                features = POSMenota.binarize(tag, parsers, features)

            elif word_class == WordClass.personal_pronoun:
                features.personal_pronoun = True
                value = POSMenota.verbose[word_class]
                parsers = [Person, Gender, Number, Case]
                value = POSMenota.apply(tag, parsers, value)
                features = POSMenota.binarize(tag, parsers, features)

            elif word_class == WordClass.interrogative_pronoun:
                features.interrogative_pronoun = True
                value = POSMenota.verbose[word_class]
                parsers = [Gender, Number, Case]
                value = POSMenota.apply(tag, parsers, value)
                features = POSMenota.binarize(tag, parsers, features)

            elif word_class == WordClass.indefinite_pronouns:
                features.indefinite_pronouns = True
                value = POSMenota.verbose[word_class]
                parsers = [Gender, Number, Case]
                value = POSMenota.apply(tag, parsers, value)
                features = POSMenota.binarize(tag, parsers, features)

            elif word_class == WordClass.possessive:
                features.possessive = True
                value = POSMenota.verbose[word_class]
                parsers = [Gender, Number, Case]
                value = POSMenota.apply(tag, parsers, value)
                features = POSMenota.binarize(tag, parsers, features)

            elif word_class == WordClass.demonstrative:
                features.demonstrative = True
                value = POSMenota.verbose[word_class]
                parsers = [Gender, Number, Case]
                value = POSMenota.apply(tag, parsers, value)
                features = POSMenota.binarize(tag, parsers, features)

            elif word_class == WordClass.quantifier:
                features.quantifier = True
                value = POSMenota.verbose[word_class]
                parsers = [Gender, Number, Case]
                value = POSMenota.apply(tag, parsers, value)
                features = POSMenota.binarize(tag, parsers, features)

            elif word_class == WordClass.article:
                features.article = True
                value = POSMenota.verbose[word_class]
                parsers = [Gender, Number, Case]
                value = POSMenota.apply(tag, parsers, value)
                features = POSMenota.binarize(tag, parsers, features)

            elif word_class == WordClass.pronoun:
                features.pronoun = True
                value = POSMenota.verbose[word_class]
                parsers = [Person, Gender, Number, Case]
                value = POSMenota.apply(tag, parsers, value)
                features = POSMenota.binarize(tag, parsers, features)

            elif word_class == WordClass.ordinal:
                features.ordinal = True
                value = POSMenota.verbose[word_class]
                parsers = [Gender, Number, Case, Species]
                value = POSMenota.apply(tag, parsers, value)
                features = POSMenota.binarize(tag, parsers, features)

            elif word_class == WordClass.cardinal:
                features.cardinal = True
                value = POSMenota.verbose[word_class]
                parsers = [Gender, Number, Case, Species]
                value = POSMenota.apply(tag, parsers, value)
                features = POSMenota.binarize(tag, parsers, features)

            elif word_class == WordClass.numeral_undetermined:
                features.numeral = True
                value = POSMenota.verbose[word_class]
                parsers = [Gender, Number, Case, Species]
                value = POSMenota.apply(tag, parsers, value)
                features = POSMenota.binarize(tag, parsers, features)

            elif word_class == WordClass.article:
                features.article = True
                value = POSMenota.verbose[word_class]
                parsers = [Gender, Number, Case, Species]
                value = POSMenota.apply(tag, parsers, value)
                features = POSMenota.binarize(tag, parsers, features)

            elif word_class == WordClass.verb:
                features.verb = True
                value = POSMenota.verbose[word_class]
                verb_class = tags[1][1]
                if verb_class == "F":
                    parsers = [Finitness, Tense, Mood, Person, Number, Voice, InflectionalClass]
                    value = POSMenota.apply(tag, parsers, value)
                    features = POSMenota.binarize(tag, parsers, features)
                elif verb_class == "P":
                    parsers = [Finitness, Tense, Voice, Gender, Number, Case, Species, InflectionalClass]
                    value = POSMenota.apply(tag, parsers, value)
                    features = POSMenota.binarize(tag, parsers, features)
                elif verb_class == "I":
                    parsers = [Finitness, Tense, Voice, InflectionalClass]
                    value = POSMenota.apply(tag, parsers, value)
                    features = POSMenota.binarize(tag, parsers, features)

            elif word_class == WordClass.adverb:
                features.adverb = True
                value = POSMenota.verbose[word_class]
                parsers = [Grade]
                value = POSMenota.apply(tag, parsers, value)
                features = POSMenota.binarize(tag, parsers, features)

            elif word_class == WordClass.preposition:
                features.preposition = True
                value = POSMenota.verbose[word_class]
                parsers = [Government]
                value = POSMenota.apply(tag, parsers, value)
                features = POSMenota.binarize(tag, parsers, features)

            elif word_class == WordClass.adposition:
                value = POSMenota.verbose[word_class]
                features.preposition = True

            elif word_class == WordClass.conjunction:
                value = POSMenota.verbose[word_class]
                features.conjunction = True

            elif word_class == WordClass.conjunction_subjunction:
                value = POSMenota.verbose[word_class]
                features.conjunction = True

            elif word_class == WordClass.subjunction:
                value = POSMenota.verbose[word_class]
                features.conjunction = True

            if vector:
                return features
            else:
                return value


def parse(tag, vector=False):
    #     print(tag)
    if tag is None:
        return POSFeatures
    if len(tag) > 0:
        value = POSMenota.parse(tag.lower(), vector)
    else:
        if vector:
            value = POSFeatures()
        else:
            value = ""
    return value
