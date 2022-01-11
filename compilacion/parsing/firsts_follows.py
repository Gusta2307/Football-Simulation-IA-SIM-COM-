from compilacion.grammars.grammar import Grammar
from compilacion.grammars.noTerminal import NoTerminal
from compilacion.grammars.sentence import Sentence
from compilacion.grammars.epsilon import Epsilon
from compilacion.grammars.terminal import Terminal


def calculate_firsts(G : Grammar):
    firsts = calculate_noTerminal_firsts(G.productions)

    for term in G.terminals:  # calculo los firsts de los terminales
          if not firsts.__contains__(str(term)):
            firsts[str(term)] = [term]
    return firsts


def calculate_noTerminal_firsts(productions):
    firsts = {}

    for p in productions:
        for sentence in p.right:
            if not firsts.__contains__(str(p.left)):
                firsts[str(p.left)] = []

            for first in calculate_sentence_firsts(sentence):
                if first not in firsts[str(p.left)]:
                    firsts[str(p.left)].append(first) # first de un no-terminal
    return firsts


def calculate_sentence_firsts(sentence):
    if len(sentence.symbols) == 0: # si la forma oracional deriva en epsilo, first(sentence) = epsilon
        yield Epsilon()
        
    elif len(sentence.symbols) == 1: # si la forma oracional solo tiene un elemento
        term = sentence.symbols[0]

        if type(term) == Terminal:
            yield term

        elif type(term) == NoTerminal: # si es un no-terminal calculo todos sus first y fusiono ese conjunto con el que se esta calculando actualmente
            p_firsts = calculate_noTerminal_firsts(term.productions)
            for t in p_firsts[str(term)]:
                yield t
 
    else:  # si existe mas de un elemento en la forma oracional
        find_t = False
        for i in range(len(sentence.symbols)): 
            term = sentence.symbols[i]
            
            if find_t: break
            
            if type(term) == Terminal: # si es un terminal lo devuelvo y paro de buscar en esa forma oracional
                yield term
                break
            elif type(term) == Epsilon:
                continue
            else:
                for first in calculate_sentence_firsts(Sentence(term)): # si es un no-terminal, calculo el first y si deriva epsilon, calculo el first del siguiente termino, asi sucesivamente hasta que encuentre un terminal
                    if type(first) != Epsilon: 
                        yield first
                        find_t = True


def calculate_follows(G, firsts):
    follows = {}

    for p in G.productions:
        if p.left == G.startNoTerminal:
            follows[str(p.left)] = []
            follows[str(p.left)].append(G.EOF)

        calculate_noTerminal_follows(p.left, G, firsts, follows)
        
    return follows


def calculate_noTerminal_follows(no_term, G, firsts, follows):
    for p in G.productions: # nos movermos por todas las producciones de la gramatica y vemos en que producciones aparece <no_term>
        for sentence in p.right: # nos movemos por la secuencia de formas oracionales de cada produccion
            if no_term not in sentence.symbols: continue # si el termino no esta en la forma oracional, continuo buscando

            i = sentence.getIndex(no_term) # tomo la posicion de no_term en la forma oracional            
            if (i == 0): continue # si es el primer elemento no se aplica ninguna regla
            
            if not follows.__contains__(str(no_term)):
                follows[str(no_term)] = []

            if i != len(sentence.symbols) - 1: # si detras hay otra forma oracional
                sentence = sentence.symbols[i + 1:]
                z_first = [x for x in firsts[str(sentence[0])] if type(x) != Epsilon] 

                if len(z_first) != 0: # si z_first != epsilon, pongo los elementos del z_first en el Follow(a)
                    for f in z_first: # caso: X-> WAZ, A es un no-terminal y Z no deriva epsilon
                        if f not in follows[str(no_term)]:
                            follows[str(no_term)].append(f)  # First(Z) - epsilon subconj Follow(A)
                
                if len(z_first) == len(firsts[str(sentence[0])]): # significa que no hay epsilon en el first
                    continue
              
            # si detras no viene otro elemento o Z ->* epsilon, entonces Follow(X) subconj Follow(no_term)
            if str(p.left) != str(no_term):
                if follows.__contains__(str(p.left)):
                    if follows[str(p.left)] != []:
                        for f in follows[str(p.left)]:
                            if f not in follows[str(no_term)]:
                                follows[str(no_term)].append(f)