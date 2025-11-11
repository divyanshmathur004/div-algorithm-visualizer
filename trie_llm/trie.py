from schema import *

class TrieNode:
    """A node in the Trie structure."""
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.word = None

class Trie:
    """A Trie data structure for efficient prefix-based searching (autocomplete)."""
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str):
        """Inserts a word into the Trie."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.word = word

    def _get_all_words(self, node: TrieNode, results: List[str]):
        """Helper to collect all words under a given node."""
        if node.is_end_of_word:
            results.append(node.word)
        for child_node in node.children.values():
            self._get_all_words(child_node, results)

    def search_prefix(self, prefix: str) -> List[str]:
        """Returns autocomplete suggestions for a given prefix."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []  # Prefix not found
            node = node.children[char]

        suggestions = []
        self._get_all_words(node, suggestions)
        return suggestions

    def visualize(self, max_depth: int = 3):
        """
        Visualize the Trie structure in a tree format.
        Shows the first few levels to avoid overwhelming output.
        """
        print("\n" + "=" * 70)
        print("🌳 TRIE VISUALIZATION")
        print("=" * 70)
        print("root")
        self._visualize_helper(self.root, "", 0, max_depth)
        print("=" * 70)
    
    def _visualize_helper(self, node: TrieNode, prefix: str, depth: int, max_depth: int):
        """Recursive helper to visualize the trie."""
        if depth >= max_depth:
            return
        
        children = sorted(node.children.items())
        for i, (char, child_node) in enumerate(children):
            is_last = (i == len(children) - 1)
            connector = "└── " if is_last else "├── "
            extension = "    " if is_last else "│   "
            
            # Show the complete word when we reach the end
            word_marker = f" ✓ [{child_node.word}]" if child_node.is_end_of_word else ""
            print(f"{prefix}{connector}{char}{word_marker}")
            
            self._visualize_helper(child_node, prefix + extension, depth + 1, max_depth)