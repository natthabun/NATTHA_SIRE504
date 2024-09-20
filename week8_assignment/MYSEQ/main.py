from seqbio.seqMan.dnaconvert import *
from seqbio.calculation.SeqCal import *
from seqbio.pattern.SeqPattern import *

def test_function():
    #input
    seq = 'ATGGGccGTAGAATTCTTGCaaGCCCGT'
    print("Input", seq)
    seq = seq.upper()
    print("Transcription: ", dna2rna(seq))
    print("Transcription-revcomp: ", dna2rna(reverseComplementSeq(seq)))
    print("Translation: ", dna2protein(seq))
    print("Translation-revcomp: ", dna2protein(reverseComplementSeq(seq)))
    print("GC Content:", gcContent(seq))
    print("Count Bases: ", countBasesDict(seq))
    print("Count Bases-revcomp: ", countBasesDict(reverseComplementSeq(seq)))
    print("Search EcoRI: ", enzTargetsScan(seq, 'EcoRI'))
    print("Search EcoRI-revcomp: ", enzTargetsScan(reverseComplementSeq(seq), 'EcoRI'))

      
def argparserLocal():
    from argparse import ArgumentParser
    parser = ArgumentParser(prog='myseq', description='Work with sequence', )
           
    subparsers = parser.add_subparsers(
        title='commands', description='Please choose command below:', dest='command'
    )
    subparsers.required = True

    cgc_command = subparsers.add_parser('gcContent', help='Calculate GC content')
    cgc_command.add_argument("-s", "--seq", type=str, default=None, help="Provide sequence")

    count_command = subparsers.add_parser('countBases', help='Count number of each base')
    count_command.add_argument("-s", "--seq", type=str, default=None, help="Provide sequence")
    count_command.add_argument("-r", "--revcomp", action="store_true", help="Convet DNA to reverse-complementary")
 
    transcrip_command = subparsers.add_parser('transcription', help='Convert DNA->RNA')
    transcrip_command.add_argument("-s", "--seq", type=str, default=None, help="Provide sequence")
    transcrip_command.add_argument("-r", "--revcomp", action="store_true", help="Convet DNA to reverse-complementary")

    transla_command = subparsers.add_parser('translation', help='Convert DNA->Protein')
    transla_command.add_argument("-s", "--seq", type=str, default=None, help="Provide sequence")
    transla_command.add_argument("-r", "--revcomp", action="store_true", help="Convet DNA to reverse-complementary")

    enztarg_command = subparsers.add_parser('enzTargetsScan', help='Find restriction enzyme')
    enztarg_command.add_argument("-s", "--seq", type=str, default=None, help="Provide sequence")
    enztarg_command.add_argument("-e", "--enz", type=str, default=None, help="Enzyme name")
    enztarg_command.add_argument("-r", "--revcomp", action="store_true", help="Convet DNA to reverse-complementary")

    return parser

def test_args():
    parser = argparserLocal()
    args1 = parser.parse_args(["enzTargetsScan","--seq","ATGGGccGTAGAATTCTTGCaaGCCCGT","-e","EcoRI"])
    print("Input",args1.seq,f"\n{args1.enz} sites ", enzTargetsScan(args1.seq, args1.enz))
    args2 = parser.parse_args(["enzTargetsScan", "--seq", "ATGGGccGTAGAATTCTTGCaaGCCCGT", "-e", "EcoRI", "-r"])
    print("Input",args2.seq,f"\n{args2.enz} sites ", enzTargetsScan(reverseComplementSeq(args2.seq), args2.enz))

def main():
    parser = argparserLocal()
    args = parser.parse_args()
    if args.seq == None:
        print("------\nError: You do not provide -s or --seq\n------\n")
    else:
        seq = args.seq.upper()
    
    if args.command == 'transcription':
        if args.revcomp:
            print("Input",args.seq,"\nTranscription =", dna2rna(reverseComplementSeq(args.seq)))
        else:
            print("Input",args.seq,"\nTranscription =", dna2rna(args.seq))
    elif args.command == 'translation':
        if args.revcomp:
            print("Input",args.seq,"\nTranslation =", dna2protein(reverseComplementSeq(args.seq)))
        else:
            print("Input",args.seq,"\nTranslation =", dna2protein(args.seq))
    elif args.command == 'gcContent':
        print("Input",args.seq,"\nGC content =", gcContent(args.seq))
    elif args.command == 'countBases':
        if args.revcomp:
            print("Input",args.seq,"\ncountBases =", countBasesDict(reverseComplementSeq(args.seq)))
        else:
            print("Input",args.seq,"\ncountBases =", countBasesDict(args.seq))
    elif args.command == 'enzTargetsScan':
        if args.revcomp:
            print("Input",args.seq,f"\n{args.enz} sites ", enzTargetsScan(reverseComplementSeq(args.seq), args.enz))
        else:
            print("Input",args.seq,f"\n{args.enz} sites ", enzTargetsScan(args.seq, args.enz))


if __name__ == "__main__":
    # main()
    test_function()
    # test_args()