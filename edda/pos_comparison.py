"""

"""
import codecs

from eddas import reader


import pos_icepahc
import pos_menota

__author__ = ["Clément Besnier <clemsciences@aol.com>", ]


# region menota

import os
from lxml import etree

namespaces = {'n': 'http://www.tei-c.org/ns/1.0',
              'me': 'http://www.menota.org/ns/1.0'}

directory_results = "comparison_results"

if not os.path.exists(directory_results):
    os.mkdir(directory_results)


def get_menota_stanzas():
    konungsbok_filename = "GKS-2365-4to-Vsp.xml"
    # hausbok_filename = "AM-544-4to-Vsp.xml"
    menota_directory = "../menota"

    parser = etree.XMLParser(load_dtd=True, no_network=False)
    tree = etree.parse(os.path.join(menota_directory, konungsbok_filename), parser=parser)
    root = tree.getroot()

    header, text = root.getchildren()
    poem = text.getchildren()[0].getchildren()[3]
    stanzas = [child for child in poem.xpath("n:lg", namespaces=namespaces)]
    return stanzas


def extract_words_for_comparison_menota():
    stringify = etree.XPath("string()")
    stanzas = get_menota_stanzas()

    normalized_stanzas = [stanza.findall(".//n:l", namespaces=namespaces) for stanza in stanzas]
    normalized_lines = [[line.findall(".//me:norm", namespaces=namespaces) for line in stanza]
                        for stanza in normalized_stanzas]
    normalized_text = [[[stringify(word) for word in line] for line in stanza] for stanza in normalized_lines]

    lemmata_stanzas = [stanza.findall(".//n:l", namespaces=namespaces) for stanza in stanzas]
    lemmata_lines = [[line.findall(".//n:w", namespaces=namespaces) for line in stanza] for stanza in lemmata_stanzas]
    lemmata_text = [[[word.get("lemma") for word in line] for line in stanza] for stanza in lemmata_lines]

    pos_stanzas = [stanza.findall(".//n:l", namespaces=namespaces) for stanza in stanzas]
    pos_lines = [[line.findall(".//n:w", namespaces=namespaces) for line in stanza] for stanza in pos_stanzas]
    pos_text = [[[word.get('{http://www.menota.org/ns/1.0}msa') for word in line] for line in stanza]
                for stanza in pos_lines]
    #
    menota_tags = []
    text1 = []
    # for i, stanza in enumerate([pos_text[0]]):
    for i, stanza in enumerate(pos_text):
        for j, line in enumerate(stanza):
            for k, pos in enumerate(line):
                try:
                    menota_tags.append((normalized_text[i][j][k], pos_menota.parse(pos, True)))
                    text1.append(normalized_text[i][j][k])
                except IndexError:
                    print(i, j, k, pos_text[i][j], normalized_text[i][j])
                # print(normalized_text[i][j][k]+" ["+lemmata_text[i][j][k]+"]"+" : "+pos)

    print(len(menota_tags))
    with codecs.open(os.path.join(directory_results, "text_menota.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(text1))


extract_words_for_comparison_menota()
# endregion


# region icepahc

def extract_words_for_comparison_icepahc():
    # print(reader.poetic_edda_titles)
    pos_reader_clkt = reader.PoeticEddaPOSTaggedReader("Völuspá")
    # print(pos_reader_clkt.tagged_paras()[0])

    icepahc_tags = []
    icepahc_text = []
    for sents in pos_reader_clkt.tagged_paras():
        # print(sents)
        for sent in sents:
            for word, tag in sent:
                if tag.lower() not in ["ta", 'p', "", "-", "?", "-", ";", ".", ":", "!"]:
                    icepahc_tags.append((word, pos_icepahc.parse_icepahc(tag, True)))
                    icepahc_text.append(word)

    with codecs.open(os.path.join(directory_results, "text_icepahc.txt"), "w", encoding="utf-8") as f:
        f.write("\n".join(icepahc_text))

    print(icepahc_tags[:20])
    print(len(icepahc_tags))

# endregion

