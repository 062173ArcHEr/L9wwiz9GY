# 代码生成时间: 2025-10-02 01:49:26
import tkinter as tk
a

"""
Graph Algorithm Visualizer in Python using TKinter framework.
"""

class Graph:
    def __init__(self):
        self.nodes = []  # List of tuples (node, position)
        self.edges = []  # List of tuples (node1, node2)
        self.layout = None  # Layout (e.g., Spring, Circle)
        self.algorithm = None  # Algorithm to visualize
        self.running = False  # Flag for algorithm execution

    def add_node(self, node):
        """Add a node to the graph."""
        self.nodes.append(node)

    def add_edge(self, node1, node2):
        """Add an edge to the graph."""
        self.edges.append((node1, node2))

    def set_layout(self, layout):
        """Set the layout for the graph."""
        self.layout = layout

    def set_algorithm(self, algorithm):
        """Set the algorithm to visualize."""
        self.algorithm = algorithm

    def run_algorithm(self):
        """Run the graph algorithm."""
        if self.algorithm:
            self.algorithm(self)
        else:
            raise ValueError("No algorithm set.")

    def stop_algorithm(self):
        """Stop the algorithm execution."""
        self.running = False

class Algorithm:
    def __init__(self, graph):
        self.graph = graph

    def run(self):
        """Run the algorithm on the graph."""
        raise NotImplementedError("Subclass must implement abstract method.")

class Dijkstra(Algorithm):
    def run(self):
        "