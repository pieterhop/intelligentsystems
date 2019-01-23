import sys
from kb import KB, Boolean, Integer, Constant

# Define our propositional symbols
# a1 is true if the card with index 1 is an ace, etc
# You need to initialise all variables that you need for you strategies and game knowledge.
# Add those variables here.. The following list is complete for the Play ace strategy.
a0 = Boolean('a0')
a1 = Boolean('a1')
a2 = Boolean('a2')
a3 = Boolean('a3')
a4 = Boolean('a4')
a5 = Boolean('a5')
a6 = Boolean('a6')
a7 = Boolean('a7')
a8 = Boolean('a8')
a9 = Boolean('a9')
a10 = Boolean('a10')
a11 = Boolean('a11')
a12 = Boolean('a12')
a13 = Boolean('a13')
a14 = Boolean('a14')
a15 = Boolean('a15')
a16 = Boolean('a16')
a17 = Boolean('a17')
a18 = Boolean('a18')
a19 = Boolean('a19')
Pa0 = Boolean('pa0')
Pa1 = Boolean('pa1')
Pa2 = Boolean('pa2')
Pa3 = Boolean('pa3')
Pa4 = Boolean('pa4')
Pa5 = Boolean('pa5')
Pa6 = Boolean('pa6')
Pa7 = Boolean('pa7')
Pa8 = Boolean('pa8')
Pa9 = Boolean('pa9')
Pa10 = Boolean('pa10')
Pa11 = Boolean('pa11')
Pa12 = Boolean('pa12')
Pa13 = Boolean('pa13')
Pa14 = Boolean('pa14')
Pa15 = Boolean('pa15')
Pa16 = Boolean('pa16')
Pa17 = Boolean('pa17')
Pa18 = Boolean('pa18')
Pa19 = Boolean('pa19')

# Create a new knowledge base
kb = KB()

# GENERAL INFORMATION ABOUT THE CARDS
# This adds information which cards are aacks
kb.add_clause(a0)
kb.add_clause(a5)
kb.add_clause(a10)
kb.add_clause(a15)
# Add here whatever is needed for your strategy.

# DEFINITION OF THE STRATEGY
# Add clauses (This list is sufficient for this strategy)
# Pa is the strategy to play aces first, so all we need to model is all x Pa(x) <-> a(x),
# In other words that the Pa strategy should play a card when it is an ace
kb.add_clause(~a0, Pa0)
kb.add_clause(~a5, Pa5)
kb.add_clause(~a10, Pa10)
kb.add_clause(~a15, Pa15)
kb.add_clause(~Pa0, a0)
kb.add_clause(~Pa5, a5)
kb.add_clause(~Pa10, a10)
kb.add_clause(~Pa15, a15)
# Add here other strategies

kb.add_clause(~Pa0)
# print all models of the knowledge base
for model in kb.models():
    print(model)

# print out whether the KB is satisfiable (if there are no models, it is not satisfiable)
print(kb.satisfiable())
