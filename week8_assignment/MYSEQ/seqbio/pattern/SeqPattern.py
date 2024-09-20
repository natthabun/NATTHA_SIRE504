# # SeqPattern module
import re
def cpgSearch(seq):
    cpgs = []
    for m in re.finditer(r'CG', seq.upper(), re.I):
        cpgs.append((m.group(), m.start(), m.end()))
    return cpgs

def enzTargetsScan(seq, enz): 
    out = []
    resEnzyme = dict(EcoRI='GAATTC', BamHI='GGATCC', 
                 HindIII='AAGCTT',AccB2I='[AG]GCGC[CT]',
                 AasI='GAC[ATCG][ATCG][ATCG][ATCG][ATCG][ATCG]GTC',
                 AceI='GC[AT]GC')
    
    if enz in resEnzyme:
        for m in re.finditer(resEnzyme['EcoRI'], seq.upper()):
            out.append((m.group(), m.start(), m.end()))
        return out
    else:
        return []
