from compilacion.grammars.grammar import Grammar
from compilacion.grammars.noTerminal import NoTerminal
from compilacion.grammars.sentence import Sentence
from compilacion.grammars.epsilon import Epsilon
from compilacion.grammars.terminal import Terminal


def calculate_firsts(G: Grammar):
    firsts = {}

    for term in G.terminals:  # calcular firsts de los terminales
        if not firsts.__contains__(term.name): 
            firsts[term.name] = [term]

    for noTerm in G.noTerminals: # calcular firsts de los no-terminales
        calculate_noTerminal_firsts(noTerm, firsts, G.epsilon)
    
    return firsts


def calculate_noTerminal_firsts(noTerm : NoTerminal, firsts, epsilon):
    if not firsts.__contains__(noTerm.name):
        firsts[noTerm.name] = []

    for p in noTerm.productions:
        for sentence in p.right:
            if not firsts.__contains__(str(sentence)):
                firsts[str(sentence)] = []

            calculate_sentence_firsts(sentence, firsts, epsilon)
            
            for f in firsts[str(sentence)]: # 
                if f not in firsts[noTerm.name]:
                    firsts[noTerm.name].append(f)


def calculate_sentence_firsts(sentence : Sentence, firsts, epsilon):
    if type(sentence) == Epsilon:
        if epsilon not in firsts[str(sentence)]:
            firsts[str(sentence)] = [epsilon]
    
    elif len(sentence.symbols) == 1 and type(sentence.symbols[0]) == Terminal: # si es un terminal, entonces lo añado al first(sentence)
        if sentence.symbols[0] not in firsts[str(sentence)]:
            firsts[str(sentence)] = [sentence.symbols[0]]
    else:
        for sym in sentence.symbols:
            if type(sym) == Epsilon:
                continue

            elif type(sym) == Terminal:
                if sym not in firsts[str(sentence)]:
                    firsts[str(sentence)] = [sym]

            elif type(sym) == NoTerminal:
                calculate_noTerminal_firsts(sym, firsts, epsilon) # calculo el first(sym)
                if len(firsts[sym.name]) == 1 and type(firsts[str(sym.name)][0]) == Epsilon:
                    continue

                for f in firsts[sym.name]:
                    if f not in firsts[str(sentence)]:
                        firsts[str(sentence)].append(f)  # pongo todo lo del first(sym) en first(sentence)
            break


def calculate_follows(G: Grammar, firsts):
    follows = {}

    for noTerm in G.noTerminals:
        if noTerm == G.startNoTerminal:
            follows[noTerm.name] = []
            follows[noTerm.name].append(G.EOF)

        calculate_noTerminal_follows(noTerm, G, firsts, follows)
    
    return follows


def calculate_noTerminal_follows(noTerm : Terminal, G: Grammar, firsts, follows):
    if not follows.__contains__(noTerm.name):
        follows[noTerm.name] = []

    for p in G.productions: # nos movermos por todas las producciones de la gramatica y vemos en que producciones aparece noTerm
        for sentence in p.right: # nos movemos por la secuencia de formas oracionales de cada produccion
            if noTerm in sentence.symbols:
                i = sentence.getIndex(noTerm)
                sent = Sentence(*sentence.symbols[i + 1:])
                
                if len(sent.symbols) > 0:
                    z_first = [x for x in firsts[str(sent)] if type(x) != Epsilon]
                    if z_first != []:
                        for f in z_first: # caso: First(Z) - € sub Follow(A)
                            if not f in follows[noTerm.name]:
                                follows[noTerm.name].append(f)
                        
                        if len(z_first) != len(firsts[str(sent)]): # € esta en First(Z), { First(Z) - € sub Follow(A) } union Follow(Z)
                            for f in follows[str(sent)]:
                                if not f in follows[noTerm.name]:
                                    follows[noTerm.name].append(f)
                    else:
                        calculate_noTerminal_follows(p.left, G, firsts, follows)
                        for f in follows[str(p.left)]:
                            if not f in follows[noTerm.name]:
                                follows[noTerm.name].append(f)
                else: 
                    for f in follows[str(p.left)]:
                        if not f in follows[noTerm.name]:
                            follows[noTerm.name].append(f)



#!!!!ANTERIOR!!!!
# def calculate_noTerminal_follows(no_term, G, firsts, follows):
#     for p in G.productions: 
#         for sentence in p.right: 
#             if no_term not in sentence.symbols: continue # si el termino no esta en la forma oracional, continuo buscando
#             i = sentence.getIndex(no_term) # tomo la posicion de no_term en la forma oracional            
#             # if (i == 0): continue # si es el primer elemento no se aplica ninguna regla
            
#             if not follows.__contains__(str(no_term)):
#                 follows[str(no_term)] = []

#             if i != len(sentence.symbols) - 1: # si detras hay otra forma oracional
#                 sentence = sentence.symbols[i + 1:]
#                 z_first = [x for x in firsts[str(sentence[0])] if type(x) != Epsilon] 

#                 if len(z_first) != 0: # si z_first != epsilon, pongo los elementos del z_first en el Follow(a)
#                     for f in z_first: # caso: X-> WAZ, A es un no-terminal y Z no deriva epsilon
#                         if f not in follows[str(no_term)]:
#                             follows[str(no_term)].append(f)  # First(Z) - epsilon subconj Follow(A)
                
#                 if len(z_first) == len(firsts[str(sentence[0])]): # significa que no hay epsilon en el first
#                     continue
              
#             # si detras no viene otro elemento o Z ->* epsilon, entonces Follow(X) subconj Follow(no_term)
#             if str(p.left) != str(no_term):
#                 # if follows.__contains__(str(p.left)):
#                 if follows[str(p.left)] != []:
#                     for f in follows[str(p.left)]:
#                         if f not in follows[str(no_term)]:
#                             follows[str(no_term)].append(f)