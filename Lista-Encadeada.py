# Elemento da Lista Encadeada
class ElementoDaListaSimples:
    def __init__(self, dado, cor):
        self.dado = dado
        self.cor = cor
        self.proximo = None

# Lista Encadeada Simples
class ListaEncadeadaSimples:
    def __init__(self, nodos = None):
        self.head = None
        if nodos is not None:
            nodo = ElementoDaListaSimples(dado=nodos.pop(0))
            self.head = nodo
            for elem in nodos:
                nodo.proximo = ElementoDaListaSimples(dado=elem)
                nodo = nodo.proximo

    # Inserir no final
    def inserirNoFinal(self, nodo):
        if self.head is None:
            self.head = nodo
            return
        nodo_atual = self.head
        while nodo_atual.proximo != None:
            nodo_atual = nodo_atual.proximo
        nodo_atual.proximo = nodo
        return

    # Inserir prioridade
    def inserirPrioridade(self, nodo): # Recebe o nodo passado por parâmetro da função inserir
        if self.head is None:          # Se o Head estiver vazio:
            self.head = nodo           # define o nodo recebido como o Head
            return

        if self.head.cor == 'V':       # Se Head possuir cor verde:
            nodo.proximo = self.head   # faz o nodo apontar para o Head
            self.head = nodo           # depois define o nodo como o novo Head
            return
        # Definição de elementos para percorrer a lista encadeada:
        nodo_atual = self.head
        nodo_anterior = None
        while nodo_atual.cor != 'V':    # Percorre a lista enquanto a cor do elemento for diferente de Verde
            nodo_anterior = nodo_atual  # Avança o elemento anterior na lista
            nodo_atual = nodo_atual.proximo # Avança o elemento atual na lista

        # Após elemento da cor Verde ser identificado, o nodo é inseirdo na lista encadeada
        nodo_anterior.proximo = nodo    # Faz o nodo anterior apontar para o nodo que é inserido
        nodo.proximo = nodo_atual       # Faz o nodo inserido apontar para o nodo atual
        return

    def inserir(self, dado, cor):
        nodo = ElementoDaListaSimples(dado, cor)
        if self.head is None:
            self.head = nodo
            return
        else:
            if nodo.cor == 'V':
                self.inserirNoFinal(nodo)
            else:
                self.inserirPrioridade(nodo)
        return

# TESTE DE FUNCIONAMENTO:
lista = ListaEncadeadaSimples() # Cria uma lista encadeada simples:

# Inserção de dados na lista encadeada:
for i in range (0,5,1):
    print('\nNova Ficha: ')
    valor = int(input('Nº: '))
    cor = input('Cor: ')
    lista.inserir(valor,cor)

# Imprime os dados da lista encadeada:
nodo_atual = lista.head
print('\nSequência de Fichas:')
while nodo_atual is not None:
    print(f"Ficha nº {nodo_atual.dado}, Cor: {nodo_atual.cor}")
    nodo_atual = nodo_atual.proximo