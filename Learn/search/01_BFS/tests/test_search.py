import unittest
from ..src.search import bfs, dfs

class TestSearchAlgorithms(unittest.TestCase):
    def setUp(self):
        # Create a simple graph for testing
        self.graph = {
            'A': [('B', 'B'), ('C', 'C')],
            'B': [('D', 'D'), ('E', 'E')],
            'C': [('F', 'F')],
            'D': [],
            'E': [('G', 'G')],
            'F': [('H', 'H')],
            'G': [],
            'H': [],
            'I': []
        }

    def successors(self, state):
        """Get all possible actions and resulting states from a given state."""
        return self.graph.get(state, [])

    def test_bfs_find_path(self):
        """Test BFS finds a path in a simple graph."""
        result = bfs('A', lambda x: x == 'H', self.successors)
        self.assertIsNotNone(result)
        actions, states, explored = result
        self.assertEqual(states, ['A', 'C', 'F', 'H'])
        self.assertTrue(explored >= 4)  # At least 4 nodes explored

    def test_dfs_find_path(self):
        """Test DFS finds a path in a simple graph."""
        result = dfs('A', lambda x: x == 'H', self.successors)
        self.assertIsNotNone(result)
        actions, states, explored = result
        self.assertEqual(states, ['A', 'B', 'E', 'G'])
        self.assertTrue(explored >= 4)  # At least 4 nodes explored

    def test_bfs_no_solution(self):
        """Test BFS handles no solution case."""
        result = bfs('A', lambda x: x == 'I', self.successors)
        self.assertIsNone(result)

    def test_dfs_no_solution(self):
        """Test DFS handles no solution case."""
        result = dfs('A', lambda x: x == 'I', self.successors)
        self.assertIsNone(result)

    def test_bfs_cyclic_graph(self):
        """Test BFS handles cycles in graph."""
        # Add a cycle to the graph
        self.graph['H'] = [('C', 'C')]
        result = bfs('A', lambda x: x == 'H', self.successors)
        self.assertIsNotNone(result)
        actions, states, explored = result
        self.assertEqual(states[-1], 'H')  # Last state should be H

    def test_dfs_cyclic_graph(self):
        """Test DFS handles cycles in graph."""
        # Add a cycle to the graph
        self.graph['H'] = [('C', 'C')]
        result = dfs('A', lambda x: x == 'H', self.successors)
        self.assertIsNotNone(result)
        actions, states, explored = result
        self.assertEqual(states[-1], 'H')  # Last state should be H

if __name__ == '__main__':
    unittest.main()
