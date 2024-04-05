from unicodedata import bidirectional
from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# A is ether knave or knight 
AKnaveOrKnight = Or(And(AKnave,Not(AKnight)) , And(Not(AKnave),AKnight))
# B is ether knave or knight 
BKnaveOrKnight = Or(And(BKnave,Not(BKnight)) , And(Not(BKnave),BKnight))
# C is ether knave or knight 
CKnaveOrKnight = Or(And(CKnave,Not(CKnight)) , And(Not(CKnave),CKnight))

# Puzzle 0
# A says "I am both a knight and a knave."
ASpeech = And(AKnight,AKnave)

knowledge0 = And( Biconditional(AKnight,ASpeech) , Biconditional(AKnave,Not(ASpeech)) ,AKnaveOrKnight
)

# Puzzle 1
# A says "We are both knaves."
# B says nothing.
ASpeech = And(AKnave,BKnave)

knowledge1 = And(Biconditional(AKnight,ASpeech) , Biconditional(AKnave,Not(ASpeech)),
            AKnaveOrKnight , BKnaveOrKnight            
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
ASpeech = Or(And(AKnave,BKnave),And(AKnight,BKnight))
BSpeech = Or(And(AKnave,BKnight),And(AKnight,BKnave))

knowledge2 = And(Biconditional(AKnight,ASpeech) , Biconditional(AKnave,Not(ASpeech)),
                Biconditional(BKnight,BSpeech) , Biconditional(BKnave,Not(BSpeech)),
                AKnaveOrKnight , BKnaveOrKnight 
)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
ASpeech = Or(AKnave,AKnight)
# A said im a knave : A is a knight and he said im a knave OR A is a knave and he said im a knave
BFirstSpeech = Or(And(AKnight,AKnave),And(AKnave,AKnave))
BSecondSpeech = CKnave
CSpeech = AKnight
knowledge3 = And(Biconditional(AKnight,ASpeech) , Biconditional(AKnave,Not(ASpeech)),
                Biconditional(BKnight,BFirstSpeech) , Biconditional(BKnave,Not(BFirstSpeech)),
                Biconditional(BKnight,BSecondSpeech) , Biconditional(BKnave,Not(BSecondSpeech)),
                Biconditional(CKnight,CSpeech) , Biconditional(CKnave,Not(CSpeech)),
                AKnaveOrKnight, BKnaveOrKnight , CKnaveOrKnight
)
def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
