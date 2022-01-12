"""
Definicion de la gramatica del lenguaje
Gramatica G = < S, N, T, P >
"""

from compilacion.grammars.grammar import Grammar
from compilacion.grammars.sentence import Sentence
from compilacion.grammars.production import Production
from compilacion.grammars.epsilon import Epsilon


G = Grammar()

# Terminales
player = G.define_terminal('player')
team = G.define_terminal('team')
game = G.define_terminal('game')
manager = G.define_terminal('manager')
referee = G.define_terminal('referee')
forTerm = G.define_terminal('for')
inTerm = G.define_terminal('in')
ifTerm = G.define_terminal('if')
elseTerm = G.define_terminal('else')
filterTerm = G.define_terminal('filter')
by = G.define_terminal('by')
function = G.define_terminal('function')
TEAM = G.define_terminal('TEAM')
orTerm = G.define_terminal('OR')
andTerm = G.define_terminal('AND')
notTerm = G.define_terminal('NOT')
intTerm = G.define_terminal('int')
strTerm = G.define_terminal('str')
boolTerm = G.define_terminal('bool')
floatTerm = G.define_terminal('float')

underscore = G.define_terminal('_')
point = G.define_terminal('.')
doblePoint = G.define_terminal(':')
statSep = G.define_terminal(';')
valueSep = G.define_terminal(',')

openB = G.define_terminal('(')
closeB = G.define_terminal(')')
openCurlyB = G.define_terminal('{')
closeCurlyB = G.define_terminal('}')
openSquareB = G.define_terminal('[')
closeSquareB = G.define_terminal(']')

plus = G.define_terminal('+')
sub = G.define_terminal('-')
mult = G.define_terminal('*')
div = G.define_terminal('/')
mod = G.define_terminal('%')

asig = G.define_terminal('=')
less = G.define_terminal('<')
great = G.define_terminal('>')
lessEq = G.define_terminal('<=')
greatEq = G.define_terminal('>=')
equals = G.define_terminal('==')
notEquals = G.define_terminal('!=')
 
iden = G.define_terminal('<id>')
num = G.define_terminal('<num>')
text = G.define_terminal('<text>')


# No-terminales
S = G.define_noTerminal('S')
SL = G.define_noTerminal('SL')
ST = G.define_noTerminal('ST')
Z = G.define_noTerminal('Z')
D = G.define_noTerminal('D')
AS = G.define_noTerminal('AS')
FR = G.define_noTerminal('FR')
IF = G.define_noTerminal('IF')
FUN = G.define_noTerminal('FUN')
ARD = G.define_noTerminal('ARD')
TYD = G.define_noTerminal('TYD')
TY = G.define_noTerminal('TY')
AT = G.define_noTerminal('AT')
ATH = G.define_noTerminal('ATH')
ARG = G.define_noTerminal('ARG')
IDL = G.define_noTerminal('IDL')
ARI = G.define_noTerminal('ARI')
FUNC = G.define_noTerminal('FUNC')
EL = G.define_noTerminal('EL')
E = G.define_noTerminal('E')
T = G.define_noTerminal('T')
X = G.define_noTerminal('X')
Y = G.define_noTerminal('Y')
F = G.define_noTerminal('F')
EB = G.define_noTerminal('EB')
TB = G.define_noTerminal('TB')
XB = G.define_noTerminal('XB')
YB = G.define_noTerminal('YB')
FB = G.define_noTerminal('FB')

G.startNoTerminal = S


# Producciones
epsilon = G.epsilon
G.add_production(Production(S, Sentence(SL))) # S -> SL
G.add_production(Production(SL, Sentence(statSep, ST, SL), epsilon)) # SL -> ; ST SL | €
# G.add_production(Production(SL, Sentence(statSep, ST, Z))) # SL -> ; ST Z
# G.add_production(Production(Z, Sentence(statSep, ST, Z), epsilon)) # Z-> ; ST Z | €
G.add_production(Production(ST, Sentence(D), Sentence(AS), Sentence(FR), Sentence(IF), Sentence(FUN), Sentence(ARD))) # ST -> D | AS | FR | IF | FUN | ARD
G.add_production(Production(D, Sentence(TYD, iden, openB, ARG, closeB))) # D -> TYD id ( ARG )
G.add_production(Production(TYD, Sentence(player), Sentence(team), Sentence(game), Sentence(manager), Sentence(referee))) # TYD -> player | team | game | manager | referee
G.add_production(Production(ARG, Sentence(iden), Sentence(iden, asig, AT), Sentence(iden, asig, AT, valueSep, ARG))) # ARG -> id | id = AT | id = AT , ARG
G.add_production(Production(AT, Sentence(ATH), Sentence(text))) # AT -> ATH | " text "
G.add_production(Production(ATH, Sentence(iden), Sentence(num), Sentence(FUNC), Sentence(iden, point, iden), Sentence(underscore, point, iden), Sentence(ARI))) # ATH -> id | num | FUNC | id . id | _ . id | ARI
G.add_production(Production(AS, Sentence(TY, iden, asig, E), Sentence(TY, iden, asig, EB))) # AS -> TY id = E | TY id = EB
G.add_production(Production(TY, Sentence(TYD), Sentence(intTerm), Sentence(strTerm), Sentence(boolTerm), Sentence(floatTerm))) # TY -> TYD | int | str | bool | float
G.add_production(Production(ARI, Sentence(iden, openSquareB, num, closeSquareB))) # ARI -> id [ num ]
G.add_production(Production(FUNC, Sentence(iden, openB, closeB), Sentence(iden, openB, EL, closeB))) # FUNC -> id ( ) | id ( EL )
G.add_production(Production(EL, Sentence(E), Sentence(EB), Sentence(E, valueSep, EL), Sentence(EB, valueSep, EL))) # EL -> E | EB | E , EL | EB , EL
G.add_production(Production(FR, Sentence(forTerm, iden, inTerm, iden, doblePoint, openCurlyB, ST, closeCurlyB), Sentence(forTerm, iden, inTerm, iden, point, iden, doblePoint, openCurlyB, ST, closeCurlyB))) # FR -> for id in id : { ST } | for id in id . id : { ST }
G.add_production(Production(IF, Sentence(ifTerm, EB, doblePoint, openCurlyB, ST, closeCurlyB), Sentence(ifTerm, EB, doblePoint, openCurlyB, ST, closeCurlyB, elseTerm, openCurlyB, ST, closeCurlyB))) # IF -> if EB : { ST } | if EB : { ST } else { ST }
G.add_production(Production(FUN, Sentence(function, TY, iden, openB, ARG, closeB))) # FUN -> function TY id ( ARG )
G.add_production(Production(ARD, Sentence(TY, iden, openSquareB, IDL, closeSquareB))) # ARD -> TY id IDL [ IDL ]
G.add_production(Production(IDL, Sentence(iden), Sentence(iden, valueSep, IDL))) # IDL -> id | id , IDL
G.add_production(Production(E, Sentence(T, X))) # E -> T X
G.add_production(Production(X, Sentence(plus, T, X), Sentence(sub, T, X), epsilon)) # X -> + T X | - T X | €
G.add_production(Production(T, Sentence(F, Y))) # T -> F Y
G.add_production(Production(Y, Sentence(mult, F, Y), Sentence(div, F, Y), Sentence(mod, F, Y), epsilon)) # Y -> * F Y | / F Y | % F Y | €
G.add_production(Production(F, Sentence(openB, E, closeB), Sentence(ATH))) # F -> ( E ) | ATH
G.add_production(Production(EB, Sentence(TB, XB), Sentence(notTerm, EB))) # EB -> TB XB | NOT EB
G.add_production(Production(XB, Sentence(orTerm, TB, XB), Sentence(andTerm, TB, XB), epsilon)) # XB -> OR TB XB | AND TB XB | €
G.add_production(Production(TB, Sentence(FB, YB))) # TB -> FB YB
G.add_production(Production(YB, Sentence(great, FB, YB), Sentence(less, FB, YB), Sentence(greatEq, FB, YB), Sentence(lessEq, FB, YB), Sentence(equals, FB, YB), Sentence(notEquals, FB, YB), epsilon)) # YB -> > FB YB | < FB YB | >= FB YB | <= FB YB | == FB YB | != FB YB | €
G.add_production(Production(FB, Sentence(openB, EB, closeB), Sentence(ATH))) # FB -> ( EB ) | ATH
