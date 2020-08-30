"""
POS tags reader for Old Norse texts.
The tagset is available at http://nlp.cs.ru.is/pdf/Tagset.pdf.
Some changes were made:
cc for coordinating conjunctions
ct for


"""
from typing import Union

__author__ = ["Clément Besnier <clemsciences@aol.com>", ]
__license__ = "MIT License"

from collections import defaultdict
from pos_utils import POSFeatures, POSAbstract, POSElement


class Gender(POSElement):
    masculine = "k"
    feminine = "v"
    neuter = "h"

    verbose = defaultdict(str)
    verbose[masculine] = "masculine"
    verbose[feminine] = "feminine"
    verbose[neuter] = "neuter"

    @staticmethod
    def parse(tag, value):
        """
        >>> Gender.parse("k", "")
        ' masculine'
        >>> Gender.parse("v", "")
        ' feminine'
        >>> Gender.parse("h", "")
        ' neuter'

        :param tag:
        :param value:
        :return:
        """
        return value + " " + Gender.verbose[tag]

    @staticmethod
    def can_apply(tag):
        return tag in Gender.verbose

    @staticmethod
    def binarize(tag, features: POSFeatures):
        features.masculine = tag == Gender.masculine
        features.feminine = tag == Gender.feminine
        features.neuter = tag == Gender.neuter
        return features


class Number(POSElement):

    singular = "e"
    plural = "f"

    verbose = defaultdict(str)
    verbose[singular] = "singular"
    verbose[plural] = "plural"

    @staticmethod
    def parse(tag, value):
        """
        >>> Number.parse("e", "")
        ' singular'
        >>> Number.parse("f", "")
        ' plural'

        :param tag:
        :param value:
        :return:
        """
        return value + " " + Number.verbose[tag]

    @staticmethod
    def can_apply(tag):
        return tag in Number.verbose

    @staticmethod
    def binarize(tag, features: POSFeatures):
        features.singular = tag == Number.singular
        features.plural = tag == Number.plural
        return features


class Case(POSElement):
    nominative = "n"
    accusative = "o"
    dative = "þ"
    genitive = "e"

    verbose = defaultdict(str)
    verbose[nominative] = "nominative"
    verbose[accusative] = "accusative"
    verbose[dative] = "dative"
    verbose[genitive] = "genitive"

    @staticmethod
    def parse(tag, value):
        """
        >>> Case.parse("n", "")
        ' nominative'
        >>> Case.parse("o", "")
        ' accusative'
        >>> Case.parse("þ", "")
        ' dative'
        >>> Case.parse("e", "")
        ' genitive'

        :param tag:
        :param value:
        :return:
        """
        return value + " " + Case.verbose[tag]

    @staticmethod
    def can_apply(tag):
        return tag in Case.verbose

    @staticmethod
    def binarize(tag, features: POSFeatures):
        features.nominative = tag == Case.nominative
        features.accusative = tag == Case.accusative
        features.dative = tag == Case.dative
        features.genitive = tag == Case.genitive
        return features


class Declension(POSElement):
    strong = "s"
    weak = "v"
    indeclinable = "o"

    verbose = defaultdict(str)
    verbose[strong] = "strong"
    verbose[weak] = "weak"
    verbose[indeclinable] = "indeclinable"

    @staticmethod
    def parse(tag, value):
        """
        >>> Declension.parse("s", "")
        ' strong'
        >>> Declension.parse("v", "")
        ' weak'
        >>> Declension.parse("o", "")
        ' indeclinable'

        :param tag:
        :param value:
        :return:
        """
        return value + " " + Declension.verbose[tag]

    @staticmethod
    def can_apply(tag):
        return tag in Declension.verbose

    @staticmethod
    def binarize(tag, features: POSFeatures):
        features.strong = tag == Declension.strong
        features.weak = tag == Declension.weak
        return features


class Degree(POSElement):
    positive = "f"
    comparative = "m"
    superlative = "e"

    verbose = defaultdict(str)
    verbose[positive] = "positive"
    verbose[comparative] = "comparative"
    verbose[superlative] = "superlative"

    @staticmethod
    def parse(tag, value):
        """
        >>> Degree.parse("f", "")
        ' positive'
        >>> Degree.parse("m", "")
        ' comparative'
        >>> Degree.parse("e", "")
        ' superlative'

        :param tag:
        :param value:
        :return:
        """
        return value + " " + Degree.verbose[tag]

    @staticmethod
    def can_apply(tag):
        return tag in Degree.verbose

    @staticmethod
    def binarize(tag, features: POSFeatures):
        features.positive = tag == Degree.positive
        features.comparative = tag == Degree.comparative
        features.superlative = tag == Degree.superlative
        return features


class ProperNoun(POSElement):
    person = "m"
    place = "ö"
    other = "s"

    verbose = defaultdict(str)
    verbose[person] = "person"
    verbose[place] = "place"
    verbose[other] = "other"

    @staticmethod
    def parse(tag, value):
        """
        >>> ProperNoun.parse("m", "")
        ' person'
        >>> ProperNoun.parse("ö", "")
        " place'
        >>> ProperNoun.parse("s", "")
        ' other'

        :param tag:
        :param value:
        :return:
        """
        return value + " " + ProperNoun.verbose[tag]

    @staticmethod
    def can_apply(tag):
        return tag in ProperNoun.verbose

    @staticmethod
    def binarize(tag, features: POSFeatures):
        features.proper_noun = True
        return features


class Pronoun(POSElement):

    demonstrative = "a"
    indefinite_demonstrative = "b"
    possessive = "e"
    indefinite = "o"
    personal = "p"
    interrogative = "s"
    relative = "t"

    verbose = defaultdict(str)
    verbose[demonstrative] = "demonstrative"
    verbose[indefinite_demonstrative] = "indefinite demonstrative"
    verbose[possessive] = "possessive"
    verbose[indefinite] = "indefinite"
    verbose[personal] = "personal"
    verbose[interrogative] = "interrogative"
    verbose[relative] = "relative"

    @staticmethod
    def parse(tag, value):
        """
        >>> Pronoun.parse("a", "")
        ' demonstrative'
        >>> Pronoun.parse("b", "")
        ' indefinite demonstrative'
        >>> Pronoun.parse("e", "")
        ' possessive'
        >>> Pronoun.parse("o", "")
        ' indefinite'
        >>> Pronoun.parse("p", "")
        ' personal'
        >>> Pronoun.parse("s", "")
        ' interrogative'
        >>> Pronoun.parse("t", "")
        ' relative'

        :param tag:
        :param value:
        :return:
        """
        return value + " " + Pronoun.verbose[tag]

    @staticmethod
    def can_apply(tag):
        return tag in Pronoun.verbose

    @staticmethod
    def binarize(tag, features: POSFeatures):
        features.demonstrative = tag == Pronoun.demonstrative
        features.indefinite_demonstrative = tag == Pronoun.indefinite_demonstrative
        features.possessive = tag == Pronoun.possessive
        features.indefinite = tag == Pronoun.indefinite
        features.personal = tag == Pronoun.personal
        features.interrogative = tag == Pronoun.interrogative
        features.relative = tag == Pronoun.relative
        return features


class Person(POSElement):
    first = "1"
    second = "2"
    third = "3"

    verbose = defaultdict(str)
    verbose[first] = "first"
    verbose[second] = "second"
    verbose[third] = "third"

    @staticmethod
    def parse(tag, value):
        """
        >>> Person.parse("1", "")
        ' first'
        >>> Person.parse("2", "")
        ' second'
        >>> Person.parse("3", "")
        ' third'

        :param tag:
        :param value:
        :return:
        """
        return value + " " + Person.verbose[tag]

    @staticmethod
    def can_apply(tag):
        return tag in Person.verbose

    @staticmethod
    def binarize(tag, features: POSFeatures):
        features.first = tag == Person.first
        features.second = tag == Person.second
        features.third = tag == Person.third
        return features


class NumberCategory(POSElement):
    cardinal = "f"
    ordinal = "o"

    verbose = defaultdict(str)
    verbose[cardinal] = "cardinal"
    verbose[ordinal] = "ordinal"

    @staticmethod
    def parse(tag, value):
        """
        >>> NumberCategory.parse("f", "")
        ' cardinal'
        >>> NumberCategory.parse("o", "")
        ' ordinal'

        :param tag:
        :param value:
        :return:
        """
        return value + " " + NumberCategory.verbose[tag]

    @staticmethod
    def can_apply(tag):
        return tag in NumberCategory.verbose

    @staticmethod
    def binarize(tag, features: POSFeatures):
        features.numeral = True
        return features


class Mood(POSElement):
    infinitive = "n"
    imperative = "b"
    indicative = "f"
    subjunctive = "v"
    supine = "s"
    present_participle = "l"
    past_participle = "þ"

    verbose = defaultdict(str)
    verbose[infinitive] = "infinitive"
    verbose[imperative] = "imperative"
    verbose[indicative] = "indicative"
    verbose[subjunctive] = "subjunctive"
    verbose[supine] = "supine"
    verbose[present_participle] = "present participle"
    verbose[past_participle] = "past participle"

    @staticmethod
    def parse(tag, value):
        """
        >>> Mood.parse("n", "")
        ' infinitive'
        >>> Mood.parse("b", "")
        ' imperative'
        >>> Mood.parse("f", "")
        ' indicative'
        >>> Mood.parse("v", "")
        ' subjunctive'
        >>> Mood.parse("s", "")
        ' supine'
        >>> Mood.parse("l", "")
        ' present participle'
        >>> Mood.parse("þ", "")
        ' past participle'

        :param tag:
        :param value:
        :return:
        """
        return value + " " + Mood.verbose[tag]

    @staticmethod
    def can_apply(tag):
        return tag in Mood.verbose

    @staticmethod
    def binarize(tag, features: POSFeatures):
        features.indicative = tag == Mood.indicative
        features.subjunctive = tag == Mood.subjunctive
        features.infinitive = tag == Mood.infinitive
        features.imperative = tag == Mood.imperative
        features.participle = tag in [Mood.present_participle, Mood.past_participle, Mood.supine]
        return features


class Voice(POSElement):
    active = "g"
    middle = "m"

    verbose = defaultdict(str)
    verbose[active] = "active"
    verbose[middle] = "middle"

    @staticmethod
    def parse(tag, value):
        """
        >>> Voice.parse("g", "")
        ' active'
        >>> Voice.parse("m", "")
        ' middle'

        :param tag:
        :param value:
        :return:
        """
        return value + " " + Voice.verbose[tag]

    @staticmethod
    def can_apply(tag):
        return tag in Voice.verbose

    @staticmethod
    def binarize(tag, features: POSFeatures):
        features.active = tag == Voice.active
        features.reflexive = tag == Voice.middle
        return features


class Tense(POSElement):
    present = "n"
    past = "þ"

    verbose = defaultdict(str)
    verbose[present] = "present"
    verbose[past] = "past"

    @staticmethod
    def parse(tag, value):
        """
        >>> Tense.parse("n", "")
        'present"
        >>> Tense.parse("þ", "")
        'past'

        :param tag:
        :param value:
        :return:
        """
        return value + " " + Tense.verbose[tag]

    @staticmethod
    def can_apply(tag):
        return tag in Tense.verbose

    @staticmethod
    def binarize(tag, features: POSFeatures):
        features.preterite = tag == Tense.past
        features.present = tag == Tense.present
        return features


class POSIcePaHC(POSAbstract):
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
    verbose[noun] = "noun"
    verbose[adjective] = "adjective"
    verbose[pronoun] = "pronoun"
    verbose[article] = "article"
    verbose[numeral] = "numeral"
    verbose[verb] = "verb"
    verbose[adverb] = "adverb"
    verbose[conjunction] = "conjunction"
    verbose[unanalysed] = "unanalysed"
    verbose[punctuation] = "punctuation"
    verbose[foreign] = "foreign"

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
    def apply(tag: str, l_pos: list, value: str) -> str:
        i = 1
        for pos in l_pos:
            if isinstance(pos, list):
                for j in pos:
                    if j.can_apply(tag[i]):
                        value = j.parse(tag[i], value)
            else:
                value = pos.parse(tag[i], value)
            i += 1
        return value

    @staticmethod
    def parse(tag, vector=False) -> Union[str, POSFeatures]:
        """
        >>> POSIcePaHC.parse('fakeþ')
        'pronoun demonstrative masculine singular dative'
        >>> POSIcePaHC.parse('sfg3eþ')
        'verb indicative active third singular past'
        >>> POSIcePaHC.parse('lvensf')
        'adjective feminine singular nominative strong positive'
        >>> POSIcePaHC.parse('fp1en')
        'pronoun personal first singular nominative'
        >>> POSIcePaHC.parse('nkee')
        'noun masculine singular genitive'
        >>> POSIcePaHC.parse('sþgken')
        'verb past participle active masculine singular nominative'
        >>> POSIcePaHC.parse('nhfn')
        'noun neuter plural nominative'
        >>> POSIcePaHC.parse('nveo')
        'noun feminine singular accusative'

        :param tag:
        :param vector:
        :return:
        """
        value = ""
        features = POSFeatures
        if tag[0] == POSIcePaHC.noun:
            features.noun = True
            if len(tag) >= 4:
                parsers = [Gender, Number, Case]
                value = POSIcePaHC.verbose[tag[0]]
                value = POSIcePaHC.apply(tag, parsers, value)
                features = POSIcePaHC.binarize(tag, parsers, features)
                if len(tag) == 5:
                    value = ProperNoun.parse(tag[4], value)
                    features = ProperNoun.binarize(tag[4], features)

        elif tag[0] == POSIcePaHC.adjective:
            if len(tag) == 6:
                parsers = [Gender, Number, Case, Declension, Degree]
                value = POSIcePaHC.verbose[tag[0]]
                value = POSIcePaHC.apply(tag, parsers, value)
                features = POSIcePaHC.binarize(tag, parsers, features)

        elif tag[0] == POSIcePaHC.pronoun:
            if len(tag) == 5:
                parsers = [Pronoun, [Person, Gender], Number, Case]
                value = POSIcePaHC.verbose[tag[0]]
                value = POSIcePaHC.apply(tag, parsers, value)
                features = POSIcePaHC.binarize(tag, parsers, features)

        elif tag[0] == POSIcePaHC.article:
            if len(tag) == 4:
                parsers = [Gender, Number, Case]
                value = POSIcePaHC.verbose[tag[0]]
                value = POSIcePaHC.apply(tag, parsers, value)
                features = POSIcePaHC.binarize(tag, parsers, features)

        elif tag[0] == POSIcePaHC.numeral:
            if len(tag) == 5:
                parsers = [NumberCategory, Gender, Number, Case]
                value = POSIcePaHC.verbose[tag[0]]
                value = POSIcePaHC.apply(tag, parsers, value)
                features = POSIcePaHC.binarize(tag, parsers, features)

        elif tag[0] == POSIcePaHC.verb:
            features.verb = True
            if len(tag) == 3 and tag[1] == "n":
                parsers = [Mood, Voice]
                value = POSIcePaHC.verbose[tag[0]]
                value = POSIcePaHC.apply(tag, parsers, value)
                value = Mood.parse(tag[1], value)
                value = Voice.parse(tag[2], value)
                features = POSIcePaHC.binarize(tag, parsers, features)
                features = Mood.binarize(tag[1], features)
                features = Voice.binarize(tag[2], features)

            elif len(tag) == 6 and tag[1] == "þ":
                parsers = [Mood, Voice, Gender, Number, Case]
                value = POSIcePaHC.verbose[tag[0]]
                value = POSIcePaHC.apply(tag, parsers, value)
                features = POSIcePaHC.binarize(tag, parsers, features)

            elif len(tag) == 6:
                parsers = [Mood, Voice, Person, Number, Tense]
                value = POSIcePaHC.verbose[tag[0]]
                value = POSIcePaHC.apply(tag, parsers, value)
                features = POSIcePaHC.binarize(tag, parsers, features)

        elif tag[0] == POSIcePaHC.adverb:
            if len(tag) == 2:
                features.adverb = True
                value = POSIcePaHC.verbose[tag[0]]
                features.adverb = True
                if tag[1] == "a":
                    value += " no case "
                elif tag[1] == "u":
                    value += " exclamation"
                elif tag[1] == "o":
                    value += " accusative"
                elif tag[1] == "þ":
                    value += " dative"
                elif tag[1] == "e":
                    value += " genitive"

        elif tag[0] == POSIcePaHC.conjunction:
            if len(tag) == 2:
                value = POSIcePaHC.verbose[tag[0]]
                features.conjunction = True
                if tag[1] == "n":
                    value += ""
                elif tag[1] == "t":
                    value += ""

        elif tag[0] == POSIcePaHC.foreign:
            value = POSIcePaHC.verbose[tag[0]]
            features.foreign = True

        elif tag[0] == POSIcePaHC.unanalysed:
            value = POSIcePaHC.verbose[tag[0]]
            features.unanalysed = True

        elif tag[0] == POSIcePaHC.punctuation:
            value = POSIcePaHC.verbose[tag[0]]
            features.punctuation = True

        if vector:
            return features
        else:
            return value

    @staticmethod
    def parse_universal(tag):
        """
        >>> POSIcePaHC.parse_universal('fakeþ')
        'PRON'
        >>> POSIcePaHC.parse_universal('sfg3eþ')
        'VERB'
        >>> POSIcePaHC.parse_universal('lvensf')
        'ADJ'
        >>> POSIcePaHC.parse_universal('fp1en')
        'PRON'
        >>> POSIcePaHC.parse_universal('nkee')
        'NOUN'
        >>> POSIcePaHC.parse_universal('sþgken')
        'VERB'
        >>> POSIcePaHC.parse_universal('nhfn')
        'NOUN'
        >>> POSIcePaHC.parse_universal('nveo')
        'NOUN'

        :param tag:
        :return:
        """

        if tag[0] == POSIcePaHC.noun or tag[0] == POSIcePaHC.adjective or\
                tag[0] == POSIcePaHC.article or tag[0] == POSIcePaHC.pronoun or \
                tag[0] == POSIcePaHC.numeral or tag[0] == POSIcePaHC.verb or \
                tag[0] == POSIcePaHC.conjunction or tag[0] == POSIcePaHC.foreign or \
                tag[0] == POSIcePaHC.unanalysed or tag[0] == POSIcePaHC.punctuation:
            return POSIcePaHC.universal[tag[0]]

        elif tag[0] == POSIcePaHC.adverb:
            if len(tag) == 2:
                if tag[1] == "a":
                    return "ADV"
                elif tag[1] == "u":
                    return "ADV"
                elif tag[1] == "o" or tag[1] == "þ" or tag[1] == "e":
                    return "ADP"
        return ""

    @staticmethod
    def generate_all_possible_tags():
        """
        TODO correct it because this should not return a list whose length is equal to 1249!

        >>> len(POSIcePaHC.generate_all_possible_tags())
        1249

        :return: All the possible tags
        """
        tags = []

        noun_tags = [POSIcePaHC.noun + gender + number + case for gender in Gender.verbose for number in Number.verbose
                     for case in Case.verbose]

        noun_tags.extend([tag + pn_tag for tag in noun_tags for pn_tag in ProperNoun.verbose])
        tags.extend(noun_tags)

        adj_tags = [POSIcePaHC.adjective + gender + number + case + declension + degree for gender in Gender.verbose
                    for number in Number.verbose for case in Case.verbose for declension in Declension.verbose
                    for degree in Degree.verbose]

        tags.extend(adj_tags)

        pron_tags = [POSIcePaHC.pronoun + pronoun + person + number + case for pronoun in Pronoun.verbose
                     for person in Person.verbose for number in Number.verbose for case in Case.verbose]
        pron_tags.extend([POSIcePaHC.pronoun + pronoun + gender + number + case for pronoun in Pronoun.verbose
                          for gender in Gender.verbose for number in Number.verbose for case in Case.verbose])

        tags.extend(pron_tags)

        tags.extend([POSIcePaHC.article + gender + number + case for gender in Gender.verbose for number in Number.verbose
                     for case in Case.verbose])

        tags.extend(
            [POSIcePaHC.numeral + number_category + gender + number + case for number_category in NumberCategory.verbose
             for gender in Gender.verbose for number in Number.verbose for case in Case.verbose])

        verb_tags = [POSIcePaHC.verb + mood + voice for mood in Mood.verbose for voice in Voice.verbose]
        verb_tags.extend([POSIcePaHC.verb + mood + voice + gender + number + case for mood in Mood.verbose
                          for voice in Voice.verbose for gender in Gender.verbose for number in Number.verbose
                          for case in Case.verbose])
        verb_tags.extend(
            [POSIcePaHC.verb + mood + voice + person + number + tense for mood in Mood.verbose for voice in Voice.verbose
             for person in Person.verbose for number in Number.verbose for tense in Tense.verbose])

        tags.extend(verb_tags)

        tags.extend(["aa", "au", "ao", "aþ", "ae"])
        tags.extend(["cn", "ct", "cc"])
        tags.append(POSIcePaHC.foreign)
        tags.append(POSIcePaHC.unanalysed)
        tags.append(POSIcePaHC.punctuation)
        return tags

    @staticmethod
    def binarize(tag: str, l_pos: list, value: POSFeatures) -> POSFeatures:
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


def parse_icepahc(tag: str, vector=False):
    if vector:
        return POSFeatures()
    if len(tag) > 0:
        value = POSIcePaHC.parse(tag.lower(), vector)
    else:
        if vector:
            value = POSFeatures()
        else:
            value = ""
    return value


if __name__ == "__main__":
    print(parse("sfg3en"))
    print(parse("p"))
    print(len(POSIcePaHC.generate_all_possible_tags()))
    print(POSIcePaHC.generate_all_possible_tags())
