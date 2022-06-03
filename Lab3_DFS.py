'''Importamos la libreria Queve.'''
from queue import Queue
class Grafo:
    
    '''
    Clase Grafo la cual nos va a representar a nuestro Grafo.

    ...

    Parametros
    ----------
        m_numero_nodos : int
            Numero de nodos 
        numero_nodos : int
            Rango de nodos 
        m_dirigido : boolean
            Tipo de grafo si es dirigida o no dirigida.
        m_lista_adyacencia : diccionario
            Representación gráfica - Lista de adyacencia.
    Establecimiento de los parametros para el metodo constructor (inicializado)

    Métodos
    ------- 
        Agregar_borde(self, nodo1, nodo2, peso=1):
            Agregar arista al grafo.
        Imprimir_lista_adyacencia(self):
            Imprime la representacion grafica
        __init__(self, numero_nodos, dirigido=True):
            Recibe el numero de nodos y rango y verifica si es dirigido o no
        def dfs(self, nodo_de_inicio, objetivo, camino = [], visitado = set()):
            Imprimir el recorrido DFS de un vértice fuente dado.

    '''

    def __init__(self, numero_nodos, dirigido = True):
        '''
        Recibe el numero de nodos de nuestra clase principal Grafos. 

        Parametros.
            m_numero_nodos : int
                 Numero de nodos 
            numero_nodos : int
                Rango de nodos 
            m_dirigido : boolean
                Tipo de grafo si es dirigida o no dirigida.
            m_lista_adyacencia : diccionario
                Representación gráfica - Lista de adyacencia.
        '''
        # Numero de nodos
        self.m_numero_nodos = numero_nodos
        # Rango de nodos
        self.m_nodos = range(self.m_numero_nodos)
        # Tipo de grafo
        self.m_dirigido = dirigido
        # Usamos un directorio de datos para implementar una lista de adyacencia
        self.m_lista_adyacencia = {nodo: set() for nodo in self.m_nodos}

    def agregar_borde(self, nodo1, nodo2, peso=1):
        '''
        Agregar borde al gráfo 
        Parametros
        ----------
            nodo1: int
            nodo2: int
            peso: int
            Peso y se agregan a nuestra lista de adyacencia con el nodo que corresponde.
        '''
        # Agrega el nodo 2 a nuestra lista del nodo 1.
        self.m_lista_adyacencia[nodo1].add((nodo2, peso))
        # Evalua si el nodo es dirigido o no
        if not self.m_dirigido:
            # Agrega el nodo 1 a nuestra lista del nodo 2.
            self.m_lista_adyacencia[nodo2].add((nodo1, peso))

    def Imprimir_lista_adyacencia(self):
        '''
        Nos imprime la representacion grafica por pantalla el grafo generado de nuestra lista de ayacencia.

        Parametros
        ---------- 
        No recibe

        Retorna
        ------
        Nada
        '''
        # Recorre la lista de adyacencia
        for llave in self.m_lista_adyacencia.keys():
            # Imprime el nodo
            print("nodo", llave, ": ", self.m_lista_adyacencia[llave])

    def dfs(self, nodo_de_inicio, objetivo, camino = [], visitado = set()):
        '''
        Función que imprime el recorrido BFS de un vértice fuente dado. bfs_traversal(int s) y
        recorre los vértices alcanzables desde s.
        Genera una lista de las colas visitadas y muestra el recorrido realizado, recibe el 
        valor de nodo_de_inicio.

        Parametros
        -----------
        nodo_de_inicio : int
        visitado : int
        camino: lista

        Retorna
        -------
        Recorido del nodo vecino y peso

        '''
        # Ruta del nodo de inicio
        camino.append(nodo_de_inicio) 
        # Se agrega a la lista de nodos visitados
        visitado.add(nodo_de_inicio)
        #Nodo de inicio es igual a nuestro objetivo
        if nodo_de_inicio == objetivo:
            #Retorno de ruta
            return camino
            #Bucle para la lista adyacencia 
        for (vecino, peso) in self.m_lista_adyacencia[nodo_de_inicio]:
            # Si nuestro nodo vecino no esta en los nodos visitados 
            if vecino not in visitado:
                #Asignamos si el resultado es igual a nuestro vecino, objetivo, camino y visitado
                resultado = self.dfs(vecino, objetivo, camino, visitado)
                #Evalua el resultado 
                if resultado is not None:
                    #Devuelve nuestro resultado
                    return resultado
        # Aplila el camino y retorna la ruta
        camino.pop()
        return None

if __name__ == "__main__":
    print("----------------------------------------------------------")
    print("Caso 1")
    grafo = Grafo(5, dirigido=False)
    # Cada uno agrega los bordes del grafo con el peso
    grafo.agregar_borde(3, 1)
    grafo.agregar_borde(2, 2)
    grafo.agregar_borde(1, 4)
    grafo.agregar_borde(0, 2)
    grafo.agregar_borde(2, 3)

    # Imprime la lista de colas
    grafo.Imprimir_lista_adyacencia()

    
    camino_transversal = []
    camino_transversal = grafo.dfs(0, 3)
    print(f"El camino transversal del nodo 0 a el nodo 3 is: {camino_transversal}")

    print("----------------------------------------------------------")
    print("Caso 2")
    grafo = Grafo(4, dirigido=False)
    # Cada uno agrega los bordes del grafo con el peso
    grafo.agregar_borde(3, 1)
    grafo.agregar_borde(2, 2)
    grafo.agregar_borde(1, 0)
    grafo.agregar_borde(0, 2)
    grafo.agregar_borde(2, 3)

    # Imprime la lista de colas
    grafo.Imprimir_lista_adyacencia()

    
    camino_transversal = []
    camino_transversal = grafo.dfs(0, 3)
    print(f"El camino transversal del nodo 0 a el nodo 3 is: {camino_transversal}")

    print("----------------------------------------------------------")
    print("Caso 3")
    grafo = Grafo(6, dirigido=False)
    # Cada uno agrega los bordes del grafo con el peso
    grafo.agregar_borde(3, 0)
    grafo.agregar_borde(2, 5)
    grafo.agregar_borde(1, 4)
    grafo.agregar_borde(5, 2)
    grafo.agregar_borde(2, 3)

    # Imprime la lista de colas
    grafo.Imprimir_lista_adyacencia()

    
    camino_transversal = []
    camino_transversal = grafo.dfs(0, 3)
    print(f"El camino transversal del nodo 0 a el nodo 3 is: {camino_transversal}")

