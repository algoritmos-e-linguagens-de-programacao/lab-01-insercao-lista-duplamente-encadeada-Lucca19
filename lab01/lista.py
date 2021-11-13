class Node:

    def init(self, x):
        self.x = x
        self.next = None
        self.prev = None


class Lista:

    def init(self):
        self.init = None
        self.tail = None

    def append(self, node):
        """
        Método para inserir um elemento no final
        :param node:
        :return:
        """
        if self.init is None:
            self.init = node
            self.tail = node
            return

        self.tail.next = node
        node.prev = self.tail
        self.tail = node


    def add(self, node):
        """
        Inserir um elemento sempre no inicio da lista
        :param node:
        :return:
        """
        if self.init is None:
            self.init = node
            self.tail = node
            return

        self.init.prev = node
        node.next = self.init
        self.init = node

    def str(self):
        str_aux = '['
        node_aux = self.init
        while(node_aux is not None):
            str_aux += str(node_aux.x) + ','
            node_aux = node_aux.next
        str_aux += ']'
        return str_aux


if name == 'main':
    lista = Lista()
    lista.add(Node(x=27))
    lista.add(Node(x=1))
    print(lista)
    lista.append(Node(x=5))
    lista.append(Node(x=19))
    print(lista)