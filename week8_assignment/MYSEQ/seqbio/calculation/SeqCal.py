# # SeqCal module
def countBase(seq, base): 
    base_count = seq.upper().count(base.upper())
    return base_count

def gcContent(seq): 
    c_number = countBase(seq, 'C')
    g_number = countBase(seq, 'G')
    GC_content = (c_number+g_number)/len(seq) 
    return float(GC_content)

def atContent(seq): 
    a_number = countBase(seq, 'A')
    t_number = countBase(seq, 'T')
    AT_content = (a_number+t_number)/len(seq)
    return float(AT_content)

def countBasesDict(seq): 
    basesM = {}
    for base in seq.upper():
        basesM[base] = basesM.setdefault(base, 0) +1
    return basesM
