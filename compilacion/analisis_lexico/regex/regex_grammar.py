"""
Definicion de la gramatica de las expresiones regulares
"""

from compilacion.analisis_lexico.regex.Ast.valueNode import ValueNode
from compilacion.grammars.grammar import Grammar
from compilacion.grammars.production import Production
from compilacion.grammars.sentence import Sentence
from compilacion.analisis_lexico.regex.Ast.unionNode import UnionNode
from compilacion.analisis_lexico.regex.Ast.concatNode import ConcatNode
from compilacion.analisis_lexico.regex.Ast.multNode import MultNode
from compilacion.analisis_lexico.regex.Ast.plusNode import PlusNode
from compilacion.analisis_lexico.regex.Ast.questNode import QuestNode
from compilacion.analisis_lexico.regex.Ast.symbolNode import SymbolNode
from compilacion.analisis_lexico.regex.Ast.rangeNode import RangeSymNode, RangeUnderSymNode, RangeSymUnderNode


regex_grammar = Grammar()

# Terminales
openBracket = regex_grammar.define_terminal('(')
closeBracket = regex_grammar.define_terminal(')')
openSquareBracket = regex_grammar.define_terminal('[')
closeSquareBracket = regex_grammar.define_terminal(']')
mult = regex_grammar.define_terminal('*')
plus = regex_grammar.define_terminal('+')
sub = regex_grammar.define_terminal('-')
union = regex_grammar.define_terminal('|')
underscore = regex_grammar.define_terminal('_')
point = regex_grammar.define_terminal('.')
quest = regex_grammar.define_terminal('?')
symbol = regex_grammar.define_terminal('symbol')


# No Terminales
SS = regex_grammar.define_noTerminal("S'")
S = regex_grammar.define_noTerminal('S')
A = regex_grammar.define_noTerminal('A')
B = regex_grammar.define_noTerminal('B')
C = regex_grammar.define_noTerminal('C')
D = regex_grammar.define_noTerminal('D')
E = regex_grammar.define_noTerminal('E')
F = regex_grammar.define_noTerminal('F')
G = regex_grammar.define_noTerminal('G')
H = regex_grammar.define_noTerminal('H')
I = regex_grammar.define_noTerminal('I')
J = regex_grammar.define_noTerminal('J')
regex_grammar.startNoTerminal = SS


# Producciones
epsilon = regex_grammar.epsilon
regex_grammar.add_production(Production(SS, Sentence(S), lambda x: ValueNode(x[0]))) # S' -> S

regex_grammar.add_production(Production(S, Sentence(A, union, S), lambda x: UnionNode(x[0], x[2]))) # S -> A | S
regex_grammar.add_production(Production(S, Sentence(A), lambda x: ValueNode(x[0])))                 # S -> A

regex_grammar.add_production(Production(A, Sentence(B, A), lambda x: ConcatNode(x[0], x[1]))) # A -> B A
regex_grammar.add_production(Production(A, Sentence(B), lambda x: ValueNode(x[0])))           # A -> B

regex_grammar.add_production(Production(B, Sentence(C, mult), lambda x: MultNode(x[0])))   # B -> C*
regex_grammar.add_production(Production(B, Sentence(C, plus), lambda x: PlusNode(x[0])))   # B -> C+
regex_grammar.add_production(Production(B, Sentence(C, quest), lambda x: QuestNode(x[0]))) # B -> C?
regex_grammar.add_production(Production(B, Sentence(C), lambda x: ValueNode(x[0])))        # B -> C

regex_grammar.add_production(Production(C, Sentence(openBracket, S, closeBracket), lambda x: ValueNode(x[1]))) # C -> (S)
regex_grammar.add_production(Production(C, Sentence(openBracket, point, S, closeBracket), lambda x: ValueNode(x[2]))) # C -> (.S)
regex_grammar.add_production(Production(C, Sentence(E), lambda x: ValueNode(x[0])))                            # C -> E

regex_grammar.add_production(Production(E, Sentence(symbol), lambda x: SymbolNode(x[0].value.text)))                       # E -> symbol
regex_grammar.add_production(Production(E, Sentence(openSquareBracket, F, closeSquareBracket), lambda x: ValueNode(x[1]))) # E -> [F]
regex_grammar.add_production(Production(E, Sentence(openSquareBracket, I, closeSquareBracket), lambda x: ValueNode(x[1]))) # E -> [I]

regex_grammar.add_production(Production(F, Sentence(G, F), lambda x: UnionNode(x[0], x[1]))) # F -> G F
regex_grammar.add_production(Production(F, Sentence(G), lambda x: ValueNode(x[0])))          # F -> G

regex_grammar.add_production(Production(G, Sentence(symbol), lambda x: SymbolNode(x[0].value.text)))                                 # G -> symbol
regex_grammar.add_production(Production(G, Sentence(symbol, sub, symbol), lambda x: RangeSymNode(x[0].value.text, x[2].value.text))) # G -> symbol - symbol
regex_grammar.add_production(Production(G, Sentence(underscore, sub, symbol), lambda x: RangeUnderSymNode(x[2].value.text)))         # G -> _ - symbol
regex_grammar.add_production(Production(G, Sentence(symbol, sub, underscore), lambda x: RangeSymUnderNode(x[0].value.text)))         # G -> symbol - _

regex_grammar.add_production(Production(I, Sentence(openBracket), lambda x: SymbolNode("(")))        # I -> (
regex_grammar.add_production(Production(I, Sentence(closeBracket), lambda x: SymbolNode(")")))       # I -> )
regex_grammar.add_production(Production(I, Sentence(openSquareBracket), lambda x: SymbolNode("[")))  # I -> [
regex_grammar.add_production(Production(I, Sentence(closeSquareBracket), lambda x: SymbolNode("]"))) # I -> ]
regex_grammar.add_production(Production(I, Sentence(union), lambda x: SymbolNode("|")))              # I -> |
regex_grammar.add_production(Production(I, Sentence(mult), lambda x: SymbolNode("*")))               # I -> *
regex_grammar.add_production(Production(I, Sentence(sub), lambda x: SymbolNode("-")))                # I -> -
regex_grammar.add_production(Production(I, Sentence(plus), lambda x: SymbolNode("+")))               # I -> +
regex_grammar.add_production(Production(I, Sentence(underscore), lambda x: SymbolNode("_")))         # I -> _
regex_grammar.add_production(Production(I, Sentence(quest), lambda x: SymbolNode("?")))              # I -> ?
regex_grammar.add_production(Production(I, Sentence(point), lambda x: SymbolNode(".")))              # I -> .