import spacy

def remerge_sent(sent):
    # merges tokens which are not separated by white-space
    # does this recursively until no further changes
    # this ensures spacy tokenization does not
    changed = True
    while changed:
        changed = False
        i = 0
        while i < sent.__len__() - 1:
            tok = sent[i]
            if not tok.whitespace_:
                ntok = sent[i + 1]
                # in-place operation.
                with sent.retokenize() as retokenizer:
                    retokenizer.merge(sent[i: i + 2])
                changed = True
            i += 1
    return sent


nlp = spacy.load("en_core_web_sm")
spacy_sentence = nlp("simon is quoted as saying `` if you 'd ever seen widnes , then you 'd know why i was keen to get back to london as quickly as possible '' .")
print(len(spacy_sentence))
spacy_sentence = remerge_sent(spacy_sentence)
print(len(spacy_sentence))
