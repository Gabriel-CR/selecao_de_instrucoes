import graphviz


class ViewTree:
    def __init__(self, root):
        self.root = root

        self.convert_tree_to_image(self.root, "tree")

    def build_graph(self, node, graph):
        if node is None:
            return

        # Adicionar o nó atual ao gráfico
        graph.node(str(node), str(node.data))

        if node.left is not None:
            # Adicionar o filho esquerdo e a aresta correspondente
            graph.node(str(node.left), str(node.left.data))
            graph.edge(str(node), str(node.left))
            self.build_graph(node.left, graph)

        if node.right is not None:
            # Adicionar o filho direito e a aresta correspondente
            graph.node(str(node.right), str(node.right.data))
            graph.edge(str(node), str(node.right))
            self.build_graph(node.right, graph)

    def convert_tree_to_image(self, root, output_file):
        graph = graphviz.Digraph(format='png')
        self.build_graph(root, graph)
        graph.render(output_file, view=True)
