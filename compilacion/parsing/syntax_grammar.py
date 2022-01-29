"""
Definicion de la gramatica del lenguaje
Gramatica G = < S, N, T, P >
"""

from compilacion.analisis_semantico.Ast.expressions.atomExpressions.lenNode import LenNode
from compilacion.analisis_semantico.Ast.expressions.atomExpressions.printNode import PrintNode
from compilacion.analisis_semantico.Ast.instruction import Instruction
from compilacion.analisis_semantico.Ast.instructions.filterNode import FilterNode
from compilacion.analisis_semantico.Ast.instructions.forNode import ForNode
from compilacion.analisis_semantico.Ast.instructions.variables.arrayDeclaration import ArrayDeclaration
from compilacion.analisis_semantico.Ast.instructions.variables.assignNode import AssignNode
from compilacion.analisis_semantico.Ast.instructions.variables.declaration import Declaration
from compilacion.analisis_semantico.Ast.instructions.conditional import Conditional
from compilacion.grammars.grammar import Grammar
from compilacion.grammars.sentence import Sentence
from compilacion.grammars.production import Production
from compilacion.analisis_semantico.Ast.programNode import ProgramNode


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
returnTerm = G.define_terminal('return')
printTerm = G.define_terminal('print')
lenTerm = G.define_terminal('len')
strategy = G.define_terminal('strategy')
variablesTerm = G.define_terminal('variables')
execute = G.define_terminal('execute')
rangeTerm = G.define_terminal('range')
rangeintTerm = G.define_terminal('rangeint')
rangefloatTerm = G.define_terminal('rangefloat')
rangeboolTerm = G.define_terminal('rangebool')
rangechoiceTerm = G.define_terminal('rangechoice')
TEAM = G.define_terminal('TEAM')
orTerm = G.define_terminal('OR')
andTerm = G.define_terminal('AND')
notTerm = G.define_terminal('NOT')
ballPass = G.define_terminal('BALL_PASS')
shotOnGoal = G.define_terminal('SHOT_ON_GOAL')
interceptBall = G.define_terminal('INTERCEPT_BALL')
doLack = G.define_terminal('DO_LACK')
receiveBall = G.define_terminal('RECEIVE_BALL')
throwIn = G.define_terminal('THROW_IN')
cornerKick = G.define_terminal('CORNER_KICK')
clearBall = G.define_terminal('CLEAR_BALL')
commitFoul = G.define_terminal('COMMIT_FOUL')

underscore = G.define_terminal('_')
point = G.define_terminal('.')
doblePoint = G.define_terminal(':')
statSep = G.define_terminal(';')
valueSep = G.define_terminal(',')

openBracket = G.define_terminal('(')
closeBracket = G.define_terminal(')')
openCurlyB = G.define_terminal('{')
closeCurlyB = G.define_terminal('}')
openSquareB = G.define_terminal('[')
closeSquareB = G.define_terminal(']')

plus = G.define_terminal('+')
sub = G.define_terminal('-')
mult = G.define_terminal('*')
div = G.define_terminal('/')
mod = G.define_terminal('%')

assign = G.define_terminal('=')
less = G.define_terminal('<')
great = G.define_terminal('>')
lessEq = G.define_terminal('<=')
greatEq = G.define_terminal('>=')
equals = G.define_terminal('==')
notEquals = G.define_terminal('!=')
 
ID = G.define_terminal('id')
NUM = G.define_terminal('num')
TEXT = G.define_terminal('string')
intTerm = G.define_terminal('int')
strTerm = G.define_terminal('str')
boolTerm = G.define_terminal('bool')
floatTerm = G.define_terminal('float')
trueTerm = G.define_terminal('true')
falseTerm = G.define_terminal('false')
objectTerm = G.define_terminal('object')


# No-terminales
program = G.define_noTerminal('<program>')
statList = G.define_noTerminal('<stat-list>')
stat = G.define_noTerminal('<stat>')
declaration = G.define_noTerminal('<declaration>')
defVar = G.define_noTerminal('<def-var>')
assignVar = G.define_noTerminal('<assign-var>')
assignDel = G.define_noTerminal('<assign-del>')
forCycle = G.define_noTerminal('<for-cycle>')
conditional = G.define_noTerminal('<conditional>')
ifCond= G.define_noTerminal('<if-cond>')
ifClasure = G.define_noTerminal('<if-clasure>')
functionFunc = G.define_noTerminal('<function-func>')
defArray = G.define_noTerminal('<def-array>')
printVar = G.define_noTerminal('<print-var>')
lenList = G.define_noTerminal('<len-list>')
filterVal = G.define_noTerminal('<filter-var>')
returnVal = G.define_noTerminal('<return-val>')
defStrategy = G.define_noTerminal('<def-strategy>')
typeDef = G.define_noTerminal('<type-def>')
argList = G.define_noTerminal('<arg-list>')
idList = G.define_noTerminal('<id-list>')
typeNoTerm = G.define_noTerminal('<type>')
typeId = G.define_noTerminal('<type-id>')
typeDef = G.define_noTerminal('<type-def>')
statStrag = G.define_noTerminal('<stat-strategy>')
variables = G.define_noTerminal('<variables>')
executeFunc = G.define_noTerminal('<execute-func>')
actionsVar = G.define_noTerminal('<actions-var>')
labelsVar = G.define_noTerminal('<labels-var>')
expr = G.define_noTerminal('<expr>')
term = G.define_noTerminal('<term>')
factor = G.define_noTerminal('<factor>')
termBool = G.define_noTerminal('<term-boolean>')
factorBool = G.define_noTerminal('<factor-boolean>')
atom = G.define_noTerminal('<atom>')
boolType = G.define_noTerminal('<bool-type>')
numberType = G.define_noTerminal('<number-type>')
intNum = G.define_noTerminal('<int-num>')
floatNum = G.define_noTerminal('<float-num>')
rangeType = G.define_noTerminal('<range-type>')
funcCall = G.define_noTerminal('<func-call>')
arrayIndex = G.define_noTerminal('<array-index>')
exprList = G.define_noTerminal('<expr-list>')
atomList = G.define_noTerminal('<atom-list>')
attrList = G.define_noTerminal('<attribute-list>')
instList = G.define_noTerminal('<instruction-list>')
arguments = G.define_noTerminal('<arguments>')
strategies = G.define_noTerminal('<strategies>')
idAtom = G.define_noTerminal('<id-atom>')
atomIndex = G.define_noTerminal('<atom-index>')
statStragList = G.define_noTerminal('<stat-strategy-list>')
labelsVarAtom = G.define_noTerminal('<labels-var-atom>')
expressionList = G.define_noTerminal('<expression-list>')
brackets = G.define_noTerminal('<brackets>')
idBrackets = G.define_noTerminal('<id-brackets>')
atomIndex = G.define_noTerminal('<atom-index>')
rangeintparam = G.define_noTerminal('<rangeint-param>')
rangefloatparam = G.define_noTerminal('<rangefloat-param>')
rangeboolparam = G.define_noTerminal('<rangebool-param>')
rangechoiceparam = G.define_noTerminal('<rangechoice-param>')

G.startNoTerminal = program


# Producciones
epsilon = G.epsilon
G.add_production(Production(program, Sentence(statList), lambda x: ProgramNode(x[0])))    # <program> := <stat-list>

G.add_production(Production(statList, Sentence(stat, statSep, statList), lambda x: x[0])) # <stat-list> := <stat> ; <stat-list>
G.add_production(Production(statList, Sentence(stat, statSep), lambda x: x[0]))           # <stat-list> := <stat>;

G.add_production(Production(stat, Sentence(assignVar), lambda x: x[0]))    # <stat> := <assign-var>
G.add_production(Production(stat, Sentence(forCycle), lambda x: x[0]))     # <stat> := <for-cycle>
G.add_production(Production(stat, Sentence(conditional), lambda x: x[0]))  # <stat> := <conditional>
G.add_production(Production(stat, Sentence(functionFunc), lambda x: x[0])) # <stat> := <function-func>
G.add_production(Production(stat, Sentence(defArray), lambda x: x[0]))     # <stat> := <def-array>
G.add_production(Production(stat, Sentence(printVar), lambda x: x[0]))     # <stat> := <print-var>
G.add_production(Production(stat, Sentence(lenList), lambda x: x[0]))      # <stat> := <len-list>
G.add_production(Production(stat, Sentence(filterVal), lambda x: x[0]))    # <stat> := <filter-val>
G.add_production(Production(stat, Sentence(returnVal), lambda x: x[0]))    # <stat> := <return-val>
G.add_production(Production(stat, Sentence(defStrategy), lambda x: x[0]))  # <stat> := <strategy>

G.add_production(Production(assignVar, Sentence(typeId, assign, declaration), lambda x: x[0])) # <assign-var> := <type-id> = <declaration>

G.add_production(Production(declaration, Sentence(defVar), lambda x: x[0]))    # <declaration> := <def-var>
G.add_production(Production(declaration, Sentence(assignDel), lambda x: x[0])) # <declaration> := <assign-del>

G.add_production(Production(defVar, Sentence(openBracket, attrList, closeBracket), lambda x: Declaration(x[1], x[0], x[3]))) # <def-var> := (<attr-list>)
G.add_production(Production(assignDel, Sentence(expr), lambda x: x[0]))                                                      # <assign-del> := <expr>

G.add_production(Production(typeNoTerm, Sentence(player), lambda x: x[0]))     # <type> := player
G.add_production(Production(typeNoTerm, Sentence(team), lambda x: x[0]))       # <type> := team
G.add_production(Production(typeNoTerm, Sentence(game), lambda x: x[0]))       # <type> := game
G.add_production(Production(typeNoTerm, Sentence(manager), lambda x: x[0]))    # <type> := manager
G.add_production(Production(typeNoTerm, Sentence(referee), lambda x: x[0]))    # <type> := referee
G.add_production(Production(typeNoTerm, Sentence(intTerm), lambda x: x[0]))    # <type> := int
G.add_production(Production(typeNoTerm, Sentence(strTerm), lambda x: x[0]))    # <type> := str
G.add_production(Production(typeNoTerm, Sentence(floatTerm), lambda x: x[0]))  # <type> := float
G.add_production(Production(typeNoTerm, Sentence(boolTerm), lambda x: x[0]))   # <type> := bool
G.add_production(Production(typeNoTerm, Sentence(rangeTerm), lambda x: x[0]))  # <type> := range
G.add_production(Production(typeNoTerm, Sentence(objectTerm), lambda x: x[0])) # <type> := object

G.add_production(Production(typeId, Sentence(typeNoTerm, ID), lambda x: x[0]))                                                   # <type-id> := <type> id
G.add_production(Production(idAtom, Sentence(ID, assign, atom), lambda x: x[0]))                                                 # <id-atom> := ID = <atom>
G.add_production(Production(instList, Sentence(openCurlyB, statList, closeCurlyB), lambda x: ForNode(x[1], x[3], x[6])))         # <instruction-list> := {<stat-list>}
G.add_production(Production(arguments, Sentence(openBracket, argList, closeBracket), lambda x: ForNode(x[1], x[3], x[6])))       # <arguments> := (<arg-list>)
G.add_production(Production(arguments, Sentence(brackets), lambda x: ForNode(x[1], x[3], x[6])))                                 # <arguments> := <brackets>
G.add_production(Production(expressionList, Sentence(openBracket, exprList, closeBracket), lambda x: ForNode(x[1], x[3], x[6]))) # <expression-list> := (<expr-list>)
G.add_production(Production(brackets, Sentence(openBracket, closeBracket), lambda x: ForNode(x[1], x[3], x[6])))                 # <brackets> := ()

G.add_production(Production(forCycle, Sentence(forTerm, ID, inTerm, atom, doblePoint, instList), lambda x: ForNode(x[1], x[3], x[6]))) # <for-cycle> := for ID in <atom> : <instruction-list>

G.add_production(Production(conditional, Sentence(ifTerm, expr, doblePoint, instList, elseTerm, instList), lambda x: Conditional(x[1], x[4], None, x[8]))) # <conditional> := if <expr> : <instruction-list> else <instruction-list>
G.add_production(Production(conditional, Sentence(ifTerm, expr, doblePoint, instList), lambda x: Conditional(x[1], x[4])))                                 # <conditional> := if <expr> : <instruction-list>

G.add_production(Production(functionFunc, Sentence(function, typeId, arguments, doblePoint, instList))) # <function-func> := function <type-id> <arguments> <instruction-list>

G.add_production(Production(defArray, Sentence(typeId, atom), lambda x: ArrayDeclaration(x[1], x[0], x[3]))) # <def-array> := <type-id> <atom>

G.add_production(Production(printVar, Sentence(printTerm, expr), lambda x: PrintNode(x[1]))) # <print-var> := <expr>

G.add_production(Production(lenList, Sentence(lenTerm, openBracket, atom, closeBracket), lambda x: LenNode(x[1]))) # <len-list> := len (<atom>)

G.add_production(Production(filterVal, Sentence(filterTerm, atom, by, expr), lambda x: FilterNode(x[1], x[4]))) # <filter-val> := filter <atom> by <expr>


G.add_production(Production(returnVal, Sentence(returnTerm, expr))) # <return-val> := return <expr>

G.add_production(Production(argList, Sentence(typeId, valueSep, argList), lambda x: x[0])) # <arg-list> := <type-id>, <arg-list>
G.add_production(Production(argList, Sentence(typeId), lambda x: x[0]))                    # <arg-list> := <type-id>

G.add_production(Production(attrList, Sentence(idAtom, valueSep, attrList), lambda x: x[0])) # <atrr-list> := <id-atom>, <attr-list>
G.add_production(Production(attrList, Sentence(idAtom), lambda x: x[0]))                     # <attr-list> := <id-atom>

G.add_production(Production(idList, Sentence(ID, valueSep, idList), lambda x: x[0])) # <ID-list> := ID , <ID-list>
G.add_production(Production(idList, Sentence(ID), lambda x: x[0]))                   # <ID-list> := ID

G.add_production(Production(expr, Sentence(term, plus, expr)))     # <expr> := <term> + <expr>
G.add_production(Production(expr, Sentence(term, sub, expr)))      # <expr> := <term> - <expr>
G.add_production(Production(expr, Sentence(term, andTerm , expr))) # <expr> := <term> AND <expr>
G.add_production(Production(expr, Sentence(term, orTerm, expr)))   # <expr> := <term> OR <expr>
G.add_production(Production(expr, Sentence(notTerm, expr)))        # <expr> := NOT <expr> 
G.add_production(Production(expr, Sentence(term)))                 # <expr> := <term>

G.add_production(Production(term, Sentence(factor, mult, term)))      # <term> := <factor> * <term>
G.add_production(Production(term, Sentence(factor, div, term)))       # <term> := <factor> / <term>
G.add_production(Production(term, Sentence(factor, mod, term)))       # <term> := <factor> % <term>
G.add_production(Production(term, Sentence(factor, great, term)))     # <term> := <factor> > <term>
G.add_production(Production(term, Sentence(factor, greatEq, term)))   # <term> := <factor> >= <term>
G.add_production(Production(term, Sentence(factor, less, term)))      # <term> := <factor> < <term>
G.add_production(Production(term, Sentence(factor, lessEq, term)))    # <term> := <factor> <= <term>
G.add_production(Production(term, Sentence(factor, equals, term)))    # <term> := <factor> == <term>
G.add_production(Production(term, Sentence(factor, notEquals, term))) # <term> := <factor> != <term>
G.add_production(Production(term, Sentence(factor)))                  # <term> := <factor>

G.add_production(Production(factor, Sentence(openBracket, expr, closeBracket))) # <factor> := (<expr>)
G.add_production(Production(factor, Sentence(atom)))                            # <factor> := <atom>
G.add_production(Production(factor, Sentence(sub, factor)))                     # <factor> := - <factor>

G.add_production(Production(atom, Sentence(ID)))                                  # <atom> := ID
G.add_production(Production(atom, Sentence(TEXT)))                                # <atom> := TEXT
G.add_production(Production(atom, Sentence(boolType)))                            # <atom> := <bool-type>
G.add_production(Production(atom, Sentence(numberType)))                          # <atom> := <number-type>
G.add_production(Production(atom, Sentence(funcCall)))                            # <atom> := <funcCall>
G.add_production(Production(atom, Sentence(arrayIndex)))                          # <atom> := <array-index>
G.add_production(Production(atom, Sentence(rangeType)))                           # <atom> := <range-type>
G.add_production(Production(atom, Sentence(ID, point, ID)))                       # <atom> := ID . ID
G.add_production(Production(atom, Sentence(TEAM, point, ID)))                     # <atom> := TEAM . ID
G.add_production(Production(atom, Sentence(underscore, point, ID)))               # <atom> := _ . ID
G.add_production(Production(atom, Sentence(openSquareB, atomList, closeSquareB))) # <atom> := [<atom-list>]
G.add_production(Production(atom, Sentence(atomIndex)))                           # <atom> := <atom-index>
G.add_production(Production(atom, Sentence(lenList)))                             # <atom> := <len-list>

G.add_production(Production(atomList, Sentence(atom, valueSep, atomList ))) # <atom-list> := <atom>, <atom-list>
G.add_production(Production(atomList, Sentence(atom)))                      # <atom-list> := <atom>

G.add_production(Production(boolType, Sentence(trueTerm)))  # <bool-type> := True
G.add_production(Production(boolType, Sentence(falseTerm))) # <bool-type> := False

G.add_production(Production(numberType, Sentence(intNum)))   # <number>:= <int-num>
G.add_production(Production(numberType, Sentence(floatNum))) # <number>:= <float-num>

G.add_production(Production(intNum, Sentence(NUM)))                     # <int-num> := NUMBER
G.add_production(Production(floatNum, Sentence(intNum, point, intNum))) # <float-num> := <int-num> . <int-num>

G.add_production(Production(funcCall, Sentence(ID, brackets)))                           # <func-call> := ID <brackets>
G.add_production(Production(funcCall, Sentence(ID, openBracket, exprList,closeBracket))) # <func-call> := ID <expression-list>

G.add_production(Production(arrayIndex, Sentence(ID, atomIndex)))                  # <array-index> := ID <atomIndex>
G.add_production(Production(atomIndex, Sentence(openSquareB, atom, closeSquareB))) # <atom-index> := [<atom>]

G.add_production(Production(exprList, Sentence(expr, valueSep, exprList))) # <expr-list> := <expr> , <expr-list>
G.add_production(Production(exprList, Sentence(expr)))                     # <expr-list> := <expr>

G.add_production(Production(defStrategy, Sentence(strategy, ID, strategies))) # <def-strategy> := strategy ID <strategies>
G.add_production(Production(strategies, Sentence(openCurlyB, statStragList, closeCurlyB)))  # <strategies> := { <stat-strategy-list> }

G.add_production(Production(statStragList, Sentence(statStrag, statSep, statStragList))) # <stat-strategy-list> := <stat-strategy> ; <stat-strategy-list>
G.add_production(Production(statStragList, Sentence(statStrag, statSep)))                         # <stat-strategy-list> := <stat-strategy> ;

G.add_production(Production(statStrag, Sentence(variables)))   # <stat-strategy> := <variables>
G.add_production(Production(statStrag, Sentence(executeFunc))) # <stat-strategy> := <execute-func>

G.add_production(Production(variables, Sentence(variablesTerm, openCurlyB, attrList, closeCurlyB)))   # <variables> := variables { <attribute-list> }
G.add_production(Production(executeFunc, Sentence(execute, openBracket, ID, closeBracket, instList))) # <execute-func> := execute (ID) <instruction-list>

# G.add_production(Production(actionsVar, Sentence(idAtom, valueSep, actionsVar))) # <actions-var> := <id-atom> , <actions-var>
# G.add_production(Production(actionsVar, Sentence(labelsVarAtom)))                       # <actions-var> := <id-atom>

# G.add_production(Production(actionsVar, Sentence(labelsVarAtom, valueSep, actionsVar))) # <actions-var> := <labels-var-atom>, <actions-var>
# G.add_production(Production(actionsVar, Sentence(labelsVarAtom)))                       # <actions-var> := <labels-var-atom> 

# G.add_production(Production(labelsVarAtom, Sentence(labelsVar, assign, atom))) # <labels-var-atom> := <labels-var> = <atom>

# G.add_production(Production(labelsVar, Sentence(ballPass)))      # <labels-var> := BALL_PASS
# G.add_production(Production(labelsVar, Sentence(shotOnGoal)))    # <labels-var> := SHOT_ON_GOAL
# G.add_production(Production(labelsVar, Sentence(interceptBall))) # <labels-var> := INTERCEPT_BALL
# G.add_production(Production(labelsVar, Sentence(doLack)))        # <labels-var> := DO_LACK
# G.add_production(Production(labelsVar, Sentence(receiveBall)))   # <labels-var> := RECEIVE_BALL
# G.add_production(Production(labelsVar, Sentence(throwIn)))       # <labels-var> := THROW_IN
# G.add_production(Production(labelsVar, Sentence(cornerKick)))    # <labels-var> := CORNER_KICK
# G.add_production(Production(labelsVar, Sentence(clearBall)))     # <labels-var> := CLEAR_BALL
# G.add_production(Production(labelsVar, Sentence(commitFoul)))    # <labels-var> := COMMIT_FOUL

G.add_production(Production(rangeType, Sentence(rangeintTerm, rangeintparam)))                        # <range-type> := rangeint <rangeint-params>
G.add_production(Production(rangeType, Sentence(rangefloatTerm, rangefloatparam)))                    # <range-type> := rangefloat <rangefloatparam>
G.add_production(Production(rangeType, Sentence(rangeboolTerm, brackets)))                            # <range-type> := rangebool <brackets>
G.add_production(Production(rangeType, Sentence(rangeboolTerm, openBracket, funcCall, closeBracket))) # <range-type> := rangebool (<funcCall>)
G.add_production(Production(rangeType, Sentence(rangechoiceTerm, rangechoiceparam)))                  # <range-type> := rangechoice <rangechoiceparam>

G.add_production(Production(rangeintparam, Sentence(openBracket, intNum, valueSep, intNum, closeBracket)))                     # <rangeint-params> := (<int-num>, <int-num>)
G.add_production(Production(rangeintparam, Sentence(openBracket, intNum, valueSep, intNum, valueSep, funcCall, closeBracket))) # <rangeint-params> := (<int-num>, <int-num>, <funcCall>)

G.add_production(Production(rangefloatparam, Sentence(openBracket, floatNum, valueSep, floatNum, closeBracket)))                     # <rangefloat-params> := (<float-num>, <float-num>)
G.add_production(Production(rangefloatparam, Sentence(openBracket, floatNum, valueSep, floatNum, valueSep, funcCall, closeBracket))) # <rangefloat-params> := (<float-num>, <float-num>, <funcCall>)

G.add_production(Production(rangechoiceparam, Sentence(openBracket, atom, closeBracket)))                     # <rangechoice-params> := (<atom>)
G.add_production(Production(rangechoiceparam, Sentence(openBracket, atom, valueSep, funcCall, closeBracket))) # <rangechoice-params> := (<atom>, <funcCall>)
