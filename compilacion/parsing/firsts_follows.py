from compilacion.grammars.grammar import Grammar
from compilacion.grammars.noTerminal import NoTerminal
from compilacion.grammars.sentence import Sentence
from compilacion.grammars.epsilon import Epsilon
from compilacion.grammars.terminal import Terminal


def calculate_firsts(G: Grammar):
    firsts = {'$':'$'}

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


def calculate_follows(G: Grammar):
    follows = {}

    for noTerm in G.noTerminals:
        if noTerm == G.startNoTerminal:
            follows[noTerm.name] = []
            follows[noTerm.name].append(G.EOF)

        calculate_noTerminal_follows(noTerm, G, follows)
    
    return follows


def calculate_noTerminal_follows(noTerm : Terminal, G: Grammar, follows):
    if not follows.__contains__(str(noTerm)):
        follows[noTerm.name] = []

    for p in G.productions: # nos movermos por todas las producciones de la gramatica y vemos en que producciones aparece noTerm
        for sentence in p.right: # nos movemos por la secuencia de formas oracionales de cada produccion
            if noTerm in sentence.symbols:
                i = sentence.getIndex(noTerm)
                sent = Sentence(*sentence.symbols[i + 1:])

                if len(sent.symbols) > 0:
                    firsts = { str(sent) : [] }
                    calculate_sentence_firsts(sent, firsts, G.epsilon) # calculo el first de la forma oracion
                    z_first = [x for x in firsts[str(sent)] if type(x) != Epsilon] # tomo todos los elementos expcepto €

                    if z_first != []:
                        for f in z_first: # caso: First(Z) - € sub Follow(A)
                            if not f in follows[noTerm.name]:
                                follows[noTerm.name].append(f)
                        
                        if len(z_first) == len(firsts[str(sent)]): # € esta en First(Z), { First(Z) - € sub Follow(A) } union Follow(Z)
                            continue
                     
                if p.left.name != noTerm.name:
                    if not follows.__contains__(p.left.name):
                        nt = p.left if p.left.name == str(p.left.name) else sent.symbols[0]
                        calculate_noTerminal_follows(nt, G, follows)
                    for f in follows[p.left.name]: # Follow(X) sub Follow(A)
                        if not f in follows[noTerm.name]:
                            follows[noTerm.name].append(f)
