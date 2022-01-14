from compilacion.grammars.production import Production
from compilacion.grammars.noTerminal import NoTerminal
from compilacion.grammars.sentence import Sentence
from compilacion.grammars.epsilon import Epsilon
from compilacion.grammars.terminal import Terminal


# # EJEMPLO 1 (ok)
S = NoTerminal('S')
A = NoTerminal('A')
B = NoTerminal('B')
C = NoTerminal('C')
D = NoTerminal('D')
I = NoTerminal('I')
Z = NoTerminal('Z')

assig = Terminal('=')
N = Terminal('num')
Id = Terminal('id')
Plus = Terminal('+')
Mult = Terminal('*')
Sub = Terminal('-')
Div = Terminal('/')
OpenBracket = Terminal('(')
CloseBracket = Terminal(')')
Union = Terminal('|')
epsilon = Epsilon()

# # Producciones de I
# i_p1 = Production(I, Sentence(N), Sentence(Id), Sentence(Plus), Sentence(Mult), Sentence(Sub), Sentence(Div), Sentence(OpenBracket), Sentence(CloseBracket))
# I.add_production(i_p1)

# # Producciones de S
# s_p1 = Production(S, Sentence(A))
# s_p2 = Production(S, Sentence(A), Sentence(B))
# s_p3 = Production(S, epsilon)
# s_p3 = Production(S, Sentence(Z, D))


# S.add_production(s_p3)
# S.add_production(s_p1)
# S.add_production(s_p2)
# Z.add_production(Production(Z, epsilon))

# # Producciones de A
# a_p1 = Production(A, Sentence(B))
# A.add_production(a_p1)


# # Producciones de B
# b_p3 = Production(B, Sentence(C, D))
# b_p2 = Production(B, Sentence(Plus, C))
# b_p1 = Production(B, Sentence(Mult, C))

# B.add_production(b_p3)
# B.add_production(b_p2)
# B.add_production(b_p1)


# # Produccciones de C
# c_p1 = Production(C, Sentence(OpenBracket, S, CloseBracket), Sentence(Id))
# # c_p1 = Production(C, epsilon)
# C.add_production(c_p1)

# # Producciones de D
# d_p1 = Production(D, Sentence(Sub, N))
# D.add_production(d_p1)

# productions = [s_p1, s_p2, s_p3, a_p1, b_p3, b_p2, b_p1, c_p1, d_p1]
# no_terminales = [S, A, B, C, D]



# # EJEMPLO 2 (ok)
E = NoTerminal('E')
E1 = NoTerminal('E1')
T = NoTerminal('T')
T1 = NoTerminal('T1')
F = NoTerminal('F')
X = NoTerminal('X')
Y = NoTerminal('Y')

# # Producciones E
# e_p1 = Production(E, Sentence(T, E1))
# E.add_production(e_p1)

# # Producciones E1
# e1_p1 = Production(E1, Sentence(Plus, T, E1), Sentence(Sub, T, E1), epsilon)
# E1.add_production(e1_p1)
# # 
# # Producciones T
# t_p1 = Production(T, Sentence(F, T1))
# T.add_production(t_p1)
# # 
# # Producciones T1
# t1_p1 = Production(T1, Sentence(Mult, F,  T1), Sentence(Div, F, T1), epsilon)
# T1.add_production(t1_p1)
# # 
# # Producciones F
# f_p1 = Production(F, Sentence(OpenBracket, E, CloseBracket), Sentence(Id), Sentence(N))
# F.add_production(f_p1)

# # Producciones X
# x_p1 = Production(X, Sentence(T, E, E1, F))
# X.add_production(x_p1)

# no_terminales = [E, E1, T, T1, F]
# no_terminales = [E, E1, T, T1, F, X]
# productions = [e_p1, e1_p1, t_p1, t1_p1, f_p1]
# productions = [e_p1, e1_p1, t_p1, t1_p1, f_p1, x_p1]
# productions = [e_p1, e1_p1, t_p1, t1_p1, f_p1, i_p1]



# EJEMPLO 3 (ok)
# # Producciones E
# e_p1 = Production(E, Sentence(T, X))
# E.add_production(e_p1)

# # Producciones T
# t_p1 = Production(T, Sentence(F, Y))
# T.add_production(t_p1)

# # Producciones F
# f_p1 = Production(F, Sentence(N))
# f_p2 = Production(F, Sentence(OpenBracket, E, CloseBracket))
# F.add_production(f_p2)
# F.add_production(f_p1)

# # Producciones Y
# y_p1 = Production(Y, Sentence(Mult, F, Y))
# y_p2 = Production(Y, epsilon)
# Y.add_production(y_p1)
# Y.add_production(y_p2)

# # Producciones X
# x_p1 = Production(X, Sentence(F, Y))
# x_p2 = Production(X, Sentence(Plus, T, X))
# x_p3 = Production(X, epsilon)
# X.add_production(x_p1)
# X.add_production(x_p2)
# X.add_production(x_p3)

# no_terminales = [E, T, X, F, Y]
# productions = [e_p1, t_p1, f_p1, f_p2, y_p1, y_p2, x_p1, x_p2, x_p3]



# ejemplo 4 (ok)
# s_p1 = Production(S, Sentence(E))
# S.add_production(s_p1)

# # e_p1 = Production(E, Sentence(Plus, T, E), Sentence(T))
# e_p1 = Production(E, Sentence(T, Plus, E), Sentence(T))
# E.add_production(e_p1)

# # t_p1 = Production(T, Sentence(Mult, F, T), Sentence(F))
# t_p1 = Production(T, Sentence(F, Mult, T), Sentence(F))
# T.add_production(t_p1)

# f_p1 = Production(F, Sentence(OpenBracket, E, CloseBracket), Sentence(N))
# F.add_production(f_p1)

# productions = [s_p1, e_p1, t_p1, f_p1]
# terminales = [Plus, Mult, OpenBracket, CloseBracket, N]
# no_terminales = [S, E, T, F]


#ejemplo 5

s_p1 = Production(S, Sentence(E))
S.add_production(s_p1)

e_p1 = Production(E, Sentence(A, assig, A), Sentence(N))
E.add_production(e_p1)

a_p1 = Production(A, Sentence(N, Plus, A), Sentence(N))
A.add_production(a_p1)

# x_p1 = Production(X, Sentence(Plus), Sentence(Mult))
# X.add_production(x_p1)

productions = [s_p1, e_p1, a_p1]
terminales = [assig, Plus, N, Mult]
no_terminales = [S, E, A, X]


# terminales = [N, Id,Plus,Mult,Sub,Div,OpenBracket,CloseBracket,Union]