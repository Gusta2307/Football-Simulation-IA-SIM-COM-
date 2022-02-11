"""
Definicion de la gramatica del lenguaje
Gramatica G = < S, N, T, P >
"""

from pickletools import read_stringnl_noescape
from compilacion.analisis_semantico.Ast.attributeNode import AttributeNode
from compilacion.analisis_semantico.Ast.expressions.atomExpressions.IdProperty import IdPropertyNone
from compilacion.analisis_semantico.Ast.expressions.atomExpressions.arrayAtom import ArrayAtomNode
from compilacion.analisis_semantico.Ast.expressions.atomExpressions.boolNode import BoolNode
from compilacion.analisis_semantico.Ast.expressions.atomExpressions.funcCall import FuncCall
from compilacion.analisis_semantico.Ast.expressions.atomExpressions.idNode import IdNode
from compilacion.analisis_semantico.Ast.expressions.atomExpressions.indexNode import IndexNode
from compilacion.analisis_semantico.Ast.expressions.atomExpressions.lenNode import LenNode
from compilacion.analisis_semantico.Ast.expressions.atomExpressions.numberNode import FloatNode, IntNode
from compilacion.analisis_semantico.Ast.instructions.breakNode import BreakNode
from compilacion.analisis_semantico.Ast.instructions.continueNode import ContinueNode
from compilacion.analisis_semantico.Ast.instructions.printNode import PrintNode
from compilacion.analisis_semantico.Ast.expressions.atomExpressions.strNode import StrNode
from compilacion.analisis_semantico.Ast.expressions.operators.binaryOperators.addNode import AddNode
from compilacion.analisis_semantico.Ast.expressions.operators.binaryOperators.andNode import AndNode
from compilacion.analisis_semantico.Ast.expressions.operators.binaryOperators.divNode import DivNode
from compilacion.analisis_semantico.Ast.expressions.operators.binaryOperators.equalsNode import EqualsNode
from compilacion.analisis_semantico.Ast.expressions.operators.binaryOperators.greaterNode import GreaterNode
from compilacion.analisis_semantico.Ast.expressions.operators.binaryOperators.greaterOrEqualsNode import GreaterOrEqualsNode
from compilacion.analisis_semantico.Ast.expressions.operators.binaryOperators.lessNode import LessNode
from compilacion.analisis_semantico.Ast.expressions.operators.binaryOperators.lessOrEqualsNode import LessOrEqualsNode
from compilacion.analisis_semantico.Ast.expressions.operators.binaryOperators.modNode import ModNode
from compilacion.analisis_semantico.Ast.expressions.operators.binaryOperators.mulNode import MultNode
from compilacion.analisis_semantico.Ast.expressions.operators.binaryOperators.notEqualsNode import NotEqualsNode
from compilacion.analisis_semantico.Ast.expressions.operators.binaryOperators.orNode import OrNode
from compilacion.analisis_semantico.Ast.expressions.operators.binaryOperators.subNode import SubNode
from compilacion.analisis_semantico.Ast.expressions.operators.unaryOperators.negationNode import NegationNode
from compilacion.analisis_semantico.Ast.expressions.operators.unaryOperators.notNode import NotNode
from compilacion.analisis_semantico.Ast.instruction import Instruction
from compilacion.analisis_semantico.Ast.instructions.executeNode import ExecuteNode
from compilacion.analisis_semantico.Ast.instructions.forNode import ForNode
from compilacion.analisis_semantico.Ast.instructions.functionNode import FunctionNode
from compilacion.analisis_semantico.Ast.instructions.returnNode import ReturnNode
from compilacion.analisis_semantico.Ast.instructions.variableNode import VariableNode
from compilacion.analisis_semantico.Ast.instructions.variables.arrayDeclaration import ArrayDeclaration
from compilacion.analisis_semantico.Ast.instructions.variables.assignNode import AssignNode
from compilacion.analisis_semantico.Ast.instructions.variables.declaration import Declaration
from compilacion.analisis_semantico.Ast.instructions.conditional import Conditional
from compilacion.analisis_semantico.Ast.instructions.strategyNode import StrategyNode
from compilacion.analisis_semantico.Ast.instructions.variables.reassignNode import ReassignNode
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
elifTerm = G.define_terminal('elif')
filterTerm = G.define_terminal('filter')
by = G.define_terminal('by')
function = G.define_terminal('function')
returnTerm = G.define_terminal('return')
printTerm = G.define_terminal('print')
lenTerm = G.define_terminal('len')
goalkeeper = G.define_terminal('goalkeeper')
reportTerm = G.define_terminal('report')
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
# ballPass = G.define_terminal('BALL_PASS')
# shotOnGoal = G.define_terminal('SHOT_ON_GOAL')
# interceptBall = G.define_terminal('INTERCEPT_BALL')
# doLack = G.define_terminal('DO_LACK')
# receiveBall = G.define_terminal('RECEIVE_BALL')
# throwIn = G.define_terminal('THROW_IN')
# cornerKick = G.define_terminal('CORNER_KICK')
# clearBall = G.define_terminal('CLEAR_BALL')
# commitFoul = G.define_terminal('COMMIT_FOUL')

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
voidTerm = G.define_terminal('void')
trueTerm = G.define_terminal('True')
falseTerm = G.define_terminal('False')
objectTerm = G.define_terminal('object')
breakTerm = G.define_terminal('break')
continueTerm = G.define_terminal('continue')


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
factor1 = G.define_noTerminal('<factor1>')
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
assignList = G.define_noTerminal('<assign-var-list>')
instList = G.define_noTerminal('<instruction-list>')
arguments = G.define_noTerminal('<arguments>')
strategies = G.define_noTerminal('<strategies>')
idAtom = G.define_noTerminal('<id-atom>')
atomIndex = G.define_noTerminal('<atom-index>')
statStragList = G.define_noTerminal('<stat-strategy-list>')
labelsVarAtom = G.define_noTerminal('<labels-var-atom>')
atomIndex = G.define_noTerminal('<atom-index>')
rangeintparam = G.define_noTerminal('<rangeint-param>')
rangefloatparam = G.define_noTerminal('<rangefloat-param>')
rangeboolparam = G.define_noTerminal('<rangebool-param>')
rangechoiceparam = G.define_noTerminal('<rangechoice-param>')
breakNoTerm = G.define_noTerminal('<break>')
continueNoTerm = G.define_noTerminal('<continue>')

G.startNoTerminal = program


# Producciones
epsilon = G.epsilon
G.add_production(Production(program, Sentence(statList), lambda x: ProgramNode(x[0]))) # <program> := <stat-list>

G.add_production(Production(statList, Sentence(stat, statSep, statList), lambda x: [x[0]] + x[2])) # <stat-list> := <stat> ; <stat-list>
G.add_production(Production(statList, Sentence(stat, statSep), lambda x: [x[0]]))                  # <stat-list> := <stat> ;

G.add_production(Production(stat, Sentence(assignVar), lambda x: x[0]))      # <stat> := <assign-var>
G.add_production(Production(stat, Sentence(forCycle), lambda x: x[0]))       # <stat> := <for-cycle>
G.add_production(Production(stat, Sentence(conditional), lambda x: x[0]))    # <stat> := <conditional>
G.add_production(Production(stat, Sentence(functionFunc), lambda x: x[0]))   # <stat> := <function-func>
G.add_production(Production(stat, Sentence(defArray), lambda x: x[0]))       # <stat> := <def-array>
G.add_production(Production(stat, Sentence(printVar), lambda x: x[0]))       # <stat> := <print-var>
G.add_production(Production(stat, Sentence(lenList), lambda x: x[0]))        # <stat> := <len-list>
G.add_production(Production(stat, Sentence(filterVal), lambda x: x[0]))      # <stat> := <filter-val>
G.add_production(Production(stat, Sentence(returnVal), lambda x: x[0]))      # <stat> := <return-val>
G.add_production(Production(stat, Sentence(defStrategy), lambda x: x[0]))    # <stat> := <strategy>
G.add_production(Production(stat, Sentence(breakNoTerm), lambda x: x[0]))    # <stat> := <break>
G.add_production(Production(stat, Sentence(continueNoTerm), lambda x: x[0])) # <stat> := <continue>
G.add_production(Production(stat, Sentence(funcCall), lambda x: x[0]))       # <stat> := <funcCall>
G.add_production(Production(stat, Sentence(idAtom), lambda x: ReassignNode(x[0].name, x[0].value))) # <stat> := <id-atom>

G.add_production(Production(breakNoTerm, Sentence(breakTerm), lambda x: BreakNode()))          # <break> := break
G.add_production(Production(continueNoTerm, Sentence(continueTerm), lambda x: ContinueNode())) # <continue> := continue

G.add_production(Production(assignVar, Sentence(typeId, assign, openBracket, attrList, closeBracket), lambda x: Declaration(x[0].identifier, x[0].type, x[3]))) # <assign-var> := <type-id> = ( <attr-list> )
G.add_production(Production(assignVar, Sentence(typeId, assign, arguments), lambda x: Declaration(x[0].identifier, x[0].type)))                                 # <assign-var> := <type-id> = <arguments>
G.add_production(Production(assignVar, Sentence(typeId, assign, expr), lambda x: AssignNode(x[0].identifier, x[0].type, x[2])))                                 # <assign-var> := <type-id> = <expr>

G.add_production(Production(typeNoTerm, Sentence(player), lambda x: x[0]))          # <type> := player
G.add_production(Production(typeNoTerm, Sentence(team), lambda x: x[0]))            # <type> := team
G.add_production(Production(typeNoTerm, Sentence(game), lambda x: x[0]))            # <type> := game
G.add_production(Production(typeNoTerm, Sentence(manager), lambda x: x[0]))         # <type> := manager
G.add_production(Production(typeNoTerm, Sentence(referee), lambda x: x[0]))         # <type> := referee
G.add_production(Production(typeNoTerm, Sentence(goalkeeper), lambda x: x[0]))      # <type> := goalkeeper
G.add_production(Production(typeNoTerm, Sentence(intTerm), lambda x: x[0]))         # <type> := int
G.add_production(Production(typeNoTerm, Sentence(strTerm), lambda x: x[0]))         # <type> := str
G.add_production(Production(typeNoTerm, Sentence(floatTerm), lambda x: x[0]))       # <type> := float
G.add_production(Production(typeNoTerm, Sentence(boolTerm), lambda x: x[0]))        # <type> := bool
G.add_production(Production(typeNoTerm, Sentence(rangeTerm), lambda x: x[0]))       # <type> := range
G.add_production(Production(typeNoTerm, Sentence(rangeintTerm), lambda x: x[0]))    # <type> := rangeint
G.add_production(Production(typeNoTerm, Sentence(rangeboolTerm), lambda x: x[0]))   # <type> := rangebool
G.add_production(Production(typeNoTerm, Sentence(rangefloatTerm), lambda x: x[0]))  # <type> := rangefloat
G.add_production(Production(typeNoTerm, Sentence(rangechoiceTerm), lambda x: x[0])) # <type> := rangechoice
G.add_production(Production(typeNoTerm, Sentence(objectTerm), lambda x: x[0]))      # <type> := object
G.add_production(Production(typeNoTerm, Sentence(voidTerm), lambda x: x[0]))        # <type> := void
G.add_production(Production(typeNoTerm, Sentence(reportTerm), lambda x: x[0]))      # <type> := report

G.add_production(Production(typeId, Sentence(typeNoTerm, ID), lambda x: VariableNode(x[1], x[0])))    # <type-id> := <type> id
G.add_production(Production(idAtom, Sentence(ID, assign, expr), lambda x: AttributeNode(x[0], x[2]))) # <id-atom> := ID = <expr>
G.add_production(Production(instList, Sentence(openCurlyB, statList, closeCurlyB), lambda x: x[1]))   # <instruction-list> := { <stat-list> }
G.add_production(Production(arguments, Sentence(openBracket, argList, closeBracket), lambda x: x[1])) # <arguments> := ( <arg-list> )
G.add_production(Production(arguments, Sentence(openBracket, closeBracket), lambda x: []))            # <arguments> := ()

G.add_production(Production(forCycle, Sentence(forTerm, ID, inTerm, atom, instList), lambda x: ForNode(x[1], x[3], x[4]))) # <for-cycle> := for ID in <atom> <instruction-list>

G.add_production(Production(conditional, Sentence(ifTerm, expr, instList, elseTerm, instList), lambda x: Conditional(x[1], x[2], None, x[4])))         # <conditional> := if <expr> <instruction-list> else <instruction-list>
G.add_production(Production(conditional, Sentence(ifTerm, expr, instList), lambda x: Conditional(x[1], x[2])))                                         # <conditional> := if <expr> <instruction-list>
G.add_production(Production(conditional, Sentence(ifTerm, expr, instList, elifTerm, expr, instList), lambda x: Conditional(x[1], x[2], (x[4], x[5])))) # <conditional> := if <expr> <instruction-list> elif <expr> <instruction-list>
G.add_production(Production(conditional, Sentence(ifTerm, expr, instList, elifTerm, expr, instList, elseTerm, instList), lambda x: Conditional(x[1], x[2], (x[4], x[5]), x[7]))) # <conditional> := if <expr> <instruction-list> elif <expr> <instruction-list> else <instruction-list>

G.add_production(Production(functionFunc, Sentence(function, typeId, arguments, instList), lambda x: FunctionNode(x[1].identifier, x[1].type, x[2], x[3]))) # <function-func> := function <type-id> <arguments>  <instruction-list>

G.add_production(Production(defArray, Sentence(typeId, atom), lambda x: ArrayDeclaration(x[0].identifier, x[0].type, x[1]))) # <def-array> := <type-id> <atom>

G.add_production(Production(printVar, Sentence(printTerm, openBracket, expr, closeBracket), lambda x: PrintNode(x[2]))) # <print-var> := print ( <expr> )

G.add_production(Production(lenList, Sentence(lenTerm, openBracket, atom, closeBracket), lambda x: LenNode(x[2]))) # <len-list> := len ( <atom> )

G.add_production(Production(returnVal, Sentence(returnTerm, expr), lambda x: ReturnNode(x[1]))) # <return-val> := return <expr>
G.add_production(Production(returnVal, Sentence(returnTerm), lambda x: ReturnNode()))           # <return-val> := return

G.add_production(Production(argList, Sentence(typeId, valueSep, argList), lambda x: [x[0]] + x[2])) # <arg-list> := <type-id>, <arg-list>
G.add_production(Production(argList, Sentence(typeId), lambda x: [x[0]]))                           # <arg-list> := <type-id>

G.add_production(Production(attrList, Sentence(idAtom, valueSep, attrList), lambda x: [x[0]] + x[2])) # <atrr-list> := <id-atom>, <attr-list>
G.add_production(Production(attrList, Sentence(idAtom), lambda x: [x[0]]))                            # <attr-list> := <id-atom>

G.add_production(Production(expr, Sentence(term, plus, expr), lambda x: AddNode(x[0], x[2])))                   # <expr> := <term> + <expr>
G.add_production(Production(expr, Sentence(term, sub, expr), lambda x: SubNode(x[0], x[2])))                    # <expr> := <term> - <expr>
G.add_production(Production(expr, Sentence(term, andTerm , expr), lambda x: AndNode(x[0], x[2])))               # <expr> := <term> AND <expr>
G.add_production(Production(expr, Sentence(term, orTerm, expr), lambda x: OrNode(x[0], x[2])))                  # <expr> := <term> OR <expr>
G.add_production(Production(expr, Sentence(notTerm, expr), lambda x: NotNode(x[1])))                            # <expr> := NOT <expr> 
G.add_production(Production(expr, Sentence(term), lambda x: x[0]))                                              # <expr> := <term>

G.add_production(Production(term, Sentence(factor1, great, term), lambda x: GreaterNode(x[0], x[2])))           # <term> := <factor1> > <term>
G.add_production(Production(term, Sentence(factor1, greatEq, term), lambda x: GreaterOrEqualsNode(x[0], x[2]))) # <term> := <factor1> >= <term>
G.add_production(Production(term, Sentence(factor1, less, term), lambda x: LessNode(x[0], x[2])))               # <term> := <factor1> < <term>
G.add_production(Production(term, Sentence(factor1, lessEq, term), lambda x: LessOrEqualsNode(x[0], x[2])))     # <term> := <factor1> <= <term>
G.add_production(Production(term, Sentence(factor1, equals, term), lambda x: EqualsNode(x[0], x[2])))           # <term> := <factor1> == <term>
G.add_production(Production(term, Sentence(factor1, notEquals, term), lambda x: NotEqualsNode(x[0], x[2])))     # <term> := <factor1> != <term>
G.add_production(Production(term, Sentence(factor1), lambda x: x[0]))                                           # <term> := <factor1>

G.add_production(Production(factor1, Sentence(factor, mult,factor1), lambda x: MultNode(x[0], x[2])))           # <factor1> := <factor> * <factor1>
G.add_production(Production(factor1, Sentence(factor, div, factor1), lambda x: DivNode(x[0], x[2])))            # <factor1> := <factor> / <factor1>
G.add_production(Production(factor1, Sentence(factor, mod, factor1), lambda x: ModNode(x[0], x[2])))            # <factor1> := <factor> % <factor1>
G.add_production(Production(factor1, Sentence(factor), lambda x: x[0]))                                         # <factor1> := <factor>

G.add_production(Production(factor, Sentence(openBracket, expr, closeBracket), lambda x: x[1])) # <factor> := ( <expr> )
G.add_production(Production(factor, Sentence(atom), lambda x: x[0]))                            # <factor> := <atom>

G.add_production(Production(atom, Sentence(ID), lambda x: IdNode(x[0])))                                         # <atom> := ID
G.add_production(Production(atom, Sentence(TEXT), lambda x: StrNode(x[0])))                                      # <atom> := TEXT
G.add_production(Production(atom, Sentence(boolType), lambda x: x[0]))                                           # <atom> := <bool-type>
G.add_production(Production(atom, Sentence(numberType), lambda x: x[0]))                                         # <atom> := <number-type>
G.add_production(Production(atom, Sentence(sub, numberType), lambda x: NegationNode(x[1])))                      # <atom> := - <number-type>
G.add_production(Production(atom, Sentence(funcCall), lambda x: x[0]))                                           # <atom> := <funcCall>
G.add_production(Production(atom, Sentence(arrayIndex), lambda x: x[0]))                                         # <atom> := <array-index>
G.add_production(Production(atom, Sentence(ID, point, ID), lambda x: IdPropertyNone(x[0], x[2])))                # <atom> := ID . ID
# G.add_production(Production(atom, Sentence(ID, point, atom), lambda x: IdPropertyNone(x[0], x[2])))                # <atom> := ID . <atom>
G.add_production(Production(atom, Sentence(ID, point, funcCall), lambda x: IdPropertyNone(x[0], x[2])))          # <atom> := ID . <funcCall>
G.add_production(Production(atom, Sentence(TEAM, point, ID), lambda x: (x[0], IdNode(x[2]))))                    # <atom> := TEAM . ID
G.add_production(Production(atom, Sentence(underscore, point, ID), lambda x: (None, IdNode(x[2]))))              # <atom> := _ . ID
G.add_production(Production(atom, Sentence(openSquareB, atomList, closeSquareB), lambda x: ArrayAtomNode(x[1]))) # <atom> := [<atom-list>]
G.add_production(Production(atom, Sentence(arrayIndex), lambda x: x[0]))                                         # <atom> := <array-index>
G.add_production(Production(atom, Sentence(lenList), lambda x: x[0]))                                            # <atom> := <len-list>

G.add_production(Production(atomList, Sentence(atom, valueSep, atomList), lambda x: [x[0]] + x[2])) # <atom-list> := <atom>, <atom-list>
G.add_production(Production(atomList, Sentence(atom), lambda x: [x[0]]))                            # <atom-list> := <atom>

G.add_production(Production(boolType, Sentence(trueTerm), lambda x: BoolNode(x[0])))  # <bool-type> := True
G.add_production(Production(boolType, Sentence(falseTerm), lambda x: BoolNode(x[0]))) # <bool-type> := False

G.add_production(Production(numberType, Sentence(intNum), lambda x: x[0]))   # <number>:= <int-num>
G.add_production(Production(numberType, Sentence(floatNum), lambda x: x[0])) # <number>:= <float-num>

G.add_production(Production(intNum, Sentence(NUM), lambda x: IntNode(int(x[0])))) # <int-num> := NUMBER
G.add_production(Production(floatNum, Sentence(intNum, point, intNum), lambda x: FloatNode(float(str(x[0].value) + x[1] + str(x[2].value))))) # <float-num> := <int-num> . <int-num>

G.add_production(Production(funcCall, Sentence(ID, openBracket, closeBracket), lambda x: FuncCall(x[0])))  # <func-call> := ID ()
G.add_production(Production(funcCall, Sentence(ID, openBracket, exprList,closeBracket), lambda x: FuncCall(x[0], x[2]))) # <func-call> := ID (<expr-list>)

G.add_production(Production(arrayIndex, Sentence(ID, openSquareB, intNum, closeSquareB), lambda x: IndexNode(x[0], x[2]))) # <array-index> := ID [<int-num>]
# G.add_production(Production(atomIndex, Sentence(openSquareB, atom, closeSquareB), lambda x: x[1])) # <atom-index> := [ <atom> ]

G.add_production(Production(exprList, Sentence(expr, valueSep, exprList), lambda x: [x[0]] + x[2])) # <expr-list> := <expr> , <expr-list>
G.add_production(Production(exprList, Sentence(expr), lambda x: [x[0]]))                            # <expr-list> := <expr>

G.add_production(Production(defStrategy, Sentence(strategy, ID, strategies), lambda x: StrategyNode(x[1], x[2]))) # <def-strategy> := strategy ID <strategies>
G.add_production(Production(strategies, Sentence(openCurlyB, statStragList, closeCurlyB), lambda x: x[1]))        # <strategies> := { <stat-strategy-list> }

G.add_production(Production(statStragList, Sentence(statStrag, statSep, statStragList), lambda x: [x[0]] + x[2])) # <stat-strategy-list> := <stat-strategy> ; <stat-strategy-list>
G.add_production(Production(statStragList, Sentence(statStrag, statSep), lambda x: [x[0]]))                       # <stat-strategy-list> := <stat-strategy> ;

G.add_production(Production(statStrag, Sentence(variables), lambda x: x[0]))   # <stat-strategy> := <variables>
G.add_production(Production(statStrag, Sentence(executeFunc), lambda x: x[0])) # <stat-strategy> := <execute-func>

G.add_production(Production(assignList, Sentence(assignVar, valueSep, assignList), lambda x: [x[0]] + x[2])) # <assign-var-list> := <assign-var> , <assign-var-list>
G.add_production(Production(assignList, Sentence(assignVar, valueSep), lambda x: [x[0]]))                    # <assign-var-list> := <assign-var> ,

G.add_production(Production(variables, Sentence(variablesTerm, openCurlyB, assignList, closeCurlyB), lambda x: x[2]))                                        # <variables> := variables { <assign-var-list>  }
G.add_production(Production(executeFunc, Sentence(execute, openBracket, ID, valueSep, ID, closeBracket, instList), lambda x: ExecuteNode(x[2], x[6], x[4]))) # <execute-func> := execute (ID, ID) <instruction-list>