"""
Definicion de la gramatica para el lexer
Gramatica G = < S, N, T, P >
"""

from compilacion.grammars.grammar import Grammar
from compilacion.grammars.sentence import Sentence
from compilacion.grammars.production import Production
from compilacion.grammars.epsilon import Epsilon


lexer_grammar = Grammar()

# Terminales
player = lexer_grammar.define_terminal('player')
team = lexer_grammar.define_terminal('team')
game = lexer_grammar.define_terminal('game')
manager = lexer_grammar.define_terminal('manager')
referee = lexer_grammar.define_terminal('referee')
forTerm = lexer_grammar.define_terminal('for')
inTerm = lexer_grammar.define_terminal('in')
ifTerm = lexer_grammar.define_terminal('if')
elseTerm = lexer_grammar.define_terminal('else')
filterTerm = lexer_grammar.define_terminal('filter')
by = lexer_grammar.define_terminal('by')
function = lexer_grammar.define_terminal('function')
TEAM = lexer_grammar.define_terminal('TEAM')
orTerm = lexer_grammar.define_terminal('OR')
andTerm = lexer_grammar.define_terminal('AND')
notTerm = lexer_grammar.define_terminal('NOT')
intTerm = lexer_grammar.define_terminal('int')
strTerm = lexer_grammar.define_terminal('str')
boolTerm = lexer_grammar.define_terminal('bool')
floatTerm = lexer_grammar.define_terminal('float')

underscore = lexer_grammar.define_terminal('_')
point = lexer_grammar.define_terminal('.')
doblePoint = lexer_grammar.define_terminal(':')
statSep = lexer_grammar.define_terminal(';')
valueSep = lexer_grammar.define_terminal(',')

openB = lexer_grammar.define_terminal('(')
closeB = lexer_grammar.define_terminal(')')
openCurlyB = lexer_grammar.define_terminal('{')
closeCurlyB = lexer_grammar.define_terminal('}')
openSquareB = lexer_grammar.define_terminal('[')
closeSquareB = lexer_grammar.define_terminal(']')

plus = lexer_grammar.define_terminal('+')
sub = lexer_grammar.define_terminal('-')
mult = lexer_grammar.define_terminal('*')
div = lexer_grammar.define_terminal('/')
mod = lexer_grammar.define_terminal('%')

asig = lexer_grammar.define_terminal('=')
less = lexer_grammar.define_terminal('<')
great = lexer_grammar.define_terminal('>')
lessEq = lexer_grammar.define_terminal('<=')
greatEq = lexer_grammar.define_terminal('>=')
equals = lexer_grammar.define_terminal('==')
notEquals = lexer_grammar.define_terminal('!=')
 
iden = lexer_grammar.define_terminal('<id>')
num = lexer_grammar.define_terminal('<num>')
text = lexer_grammar.define_terminal('<text>')


# No-terminales
S = lexer_grammar.define_noTerminal('S')
SL = lexer_grammar.define_noTerminal('SL')
ST = lexer_grammar.define_noTerminal('ST')
D = lexer_grammar.define_noTerminal('D')
AS = lexer_grammar.define_noTerminal('AS')
FR = lexer_grammar.define_noTerminal('FR')
IF = lexer_grammar.define_noTerminal('IF')
FUN = lexer_grammar.define_noTerminal('FUN')
ARD = lexer_grammar.define_noTerminal('ARD')
TYD = lexer_grammar.define_noTerminal('TYD')
TY = lexer_grammar.define_noTerminal('TY')
AT = lexer_grammar.define_noTerminal('AT')
ATH = lexer_grammar.define_noTerminal('ATH')
ARG = lexer_grammar.define_noTerminal('ARG')
IDL = lexer_grammar.define_noTerminal('IDL')
ARI = lexer_grammar.define_noTerminal('ARI')
FUNC = lexer_grammar.define_noTerminal('FUNC')
EL = lexer_grammar.define_noTerminal('EL')
E = lexer_grammar.define_noTerminal('E')
T = lexer_grammar.define_noTerminal('T')
X = lexer_grammar.define_noTerminal('X')
Y = lexer_grammar.define_noTerminal('Y')
F = lexer_grammar.define_noTerminal('F')
EB = lexer_grammar.define_noTerminal('EB')
TB = lexer_grammar.define_noTerminal('TB')
XB = lexer_grammar.define_noTerminal('XB')
YB = lexer_grammar.define_noTerminal('YB')
FB = lexer_grammar.define_noTerminal('FB')

lexer_grammar.startNoTerminal = S


# Producciones
epsilon = Epsilon()
lexer_grammar.add_production(Production(S, Sentence(SL))) # S -> SL
lexer_grammar.add_production(Production(SL, Sentence(statSep, ST, SL), epsilon)) # SL -> ; ST 
lexer_grammar.add_production(Production(ST, Sentence(D), Sentence(AS), Sentence(FR), Sentence(IF), Sentence(FUN), Sentence(ARD))) # ST -> D | AS | FR | IF | FUN | ARD
lexer_grammar.add_production(Production(D, Sentence(TYD, iden, openB, ARG, closeB))) # D -> TYD id ( ARG )
lexer_grammar.add_production(Production(TYD, Sentence(player), Sentence(team), Sentence(game), Sentence(manager), Sentence(referee))) # TYD -> player | team | game | manager | referee
lexer_grammar.add_production(Production(ARG, Sentence(iden), Sentence(iden, asig, AT), Sentence(iden, asig, AT, valueSep, ARG))) # ARG -> id | id = AT | id = AT , ARG
lexer_grammar.add_production(Production(AT, Sentence(ATH), Sentence(text))) # AT -> ATH | " text "
lexer_grammar.add_production(Production(ATH, Sentence(iden), Sentence(num), Sentence(FUNC), Sentence(iden, point, iden), Sentence(underscore, point, iden), Sentence(ARI))) # ATH -> id | num | FUNC | id . id | _ . id | ARI
lexer_grammar.add_production(Production(AS, Sentence(TY, iden, asig, E), Sentence(TY, iden, asig, EB))) # AS -> TY id = E | TY id = EB
lexer_grammar.add_production(Production(TY, Sentence(TYD), Sentence(intTerm), Sentence(strTerm), Sentence(boolTerm), Sentence(floatTerm))) # TY -> TYD | int | str | bool | float
lexer_grammar.add_production(Production(ARI, Sentence(iden, openSquareB, num, closeSquareB))) # ARI -> id [ num ]
lexer_grammar.add_production(Production(FUNC, Sentence(iden, openB, closeB), Sentence(iden, openB, EL, closeB))) # FUNC -> id ( ) | id ( EL )
lexer_grammar.add_production(Production(EL, Sentence(E), Sentence(EB), Sentence(E, valueSep, EL), Sentence(EB, valueSep, EL))) # EL -> E | EB | E , EL | EB , EL
lexer_grammar.add_production(Production(FR, Sentence(forTerm, iden, inTerm, iden, doblePoint, openCurlyB, ST, closeCurlyB), Sentence(forTerm, iden, inTerm, iden, point, iden, doblePoint, openCurlyB, ST, closeCurlyB))) # FR -> for id in id : { ST } | for id in id . id : { ST }
lexer_grammar.add_production(Production(IF, Sentence(ifTerm, EB, doblePoint, openCurlyB, ST, closeCurlyB), Sentence(ifTerm, EB, doblePoint, openCurlyB, ST, closeCurlyB, elseTerm, openCurlyB, ST, closeCurlyB))) # IF -> if EB : { ST } | if EB : { ST } else { ST }
lexer_grammar.add_production(Production(FUN, Sentence(function, TY, iden, openB, ARG, closeB))) # FUN -> function TY id ( ARG )
lexer_grammar.add_production(Production(ARD, Sentence(TY, iden, openSquareB, IDL, closeSquareB))) # ARD -> TY id IDL [ IDL ]
lexer_grammar.add_production(Production(IDL, Sentence(iden), Sentence(iden, valueSep, IDL))) # IDL -> id | id , IDL
lexer_grammar.add_production(Production(E, Sentence(T, X))) # E -> T X
lexer_grammar.add_production(Production(X, Sentence(plus, T, X), Sentence(sub, T, X), epsilon)) # X -> + T X | - T X | €
lexer_grammar.add_production(Production(T, Sentence(F, Y))) # T -> F Y
lexer_grammar.add_production(Production(Y, Sentence(mult, F, Y), Sentence(div, F, Y), Sentence(mod, F, Y), epsilon)) # Y -> * F Y | / F Y | % F Y | €
lexer_grammar.add_production(Production(F, Sentence(openB, E, closeB), Sentence(ATH))) # F -> ( E ) | ATH
lexer_grammar.add_production(Production(EB, Sentence(TB, XB), Sentence(notTerm, EB))) # EB -> TB XB | NOT EB
lexer_grammar.add_production(Production(XB, Sentence(orTerm, TB, XB), Sentence(andTerm, TB, XB), epsilon)) # XB -> OR TB XB | AND TB XB | €
lexer_grammar.add_production(Production(TB, Sentence(FB, YB))) # TB -> FB YB
lexer_grammar.add_production(Production(YB, Sentence(great, FB, YB), Sentence(less, FB, YB), Sentence(greatEq, FB, YB), Sentence(lessEq, FB, YB), Sentence(equals, FB, YB), Sentence(notEquals, FB, YB), epsilon)) # YB -> > FB YB | < FB YB | >= FB YB | <= FB YB | == FB YB | != FB YB | €
lexer_grammar.add_production(Production(FB, Sentence(openB, EB, closeB), Sentence(ATH))) # FB -> ( EB ) | ATH
