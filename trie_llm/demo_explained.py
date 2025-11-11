"""
TRIE AUTOCOMPLETE - VISUAL EXPLANATION
=====================================

This demo shows step-by-step how a Trie works for autocomplete.
"""

from trie import Trie

def print_section(title):
    """Print a section header"""
    print("\n" + "=" * 70)
    print(f"  {title}")
    print("=" * 70)

def demo_basic_trie():
    """Demonstrate basic Trie operations with simple examples"""
    
    print_section("STEP 1: Creating an Empty Trie")
    trie = Trie()
    print("✓ Created empty Trie (like an empty tree)")
    
    print_section("STEP 2: Inserting Words with Common Prefixes")
    # More intertwined words with overlapping prefixes
    words = [
        "cat", "cats", "catch", "catcher",
        "car", "cars", "card", "cargo", "carpet",
        "dog", "dogs", "dogma",
        "door", "doorway", "doorbell"
    ]
    
    print("\nLet's insert these words one by one:")
    for word in words:
        trie.insert(word)
        print(f"  ✓ Inserted: {word}")
    
    print("\nWhat's happening internally:")
    print("""
    The Trie builds a tree structure like this:
    
            root
           /    \\
          c      d
          |      |
          a      o
         / \\     |
        t   r   g/o
            |     |
            d     r
    
    - 'cat', 'car', 'card' share the path c→a
    - 'dog', 'door' share the path d→o
    """)
    
    print_section("STEP 3: Searching for Prefix 'ca'")
    prefix = "ca"
    suggestions = trie.search_prefix(prefix)
    
    print(f"\nSearching for words starting with '{prefix}'...")
    print(f"✓ Found {len(suggestions)} suggestions: {suggestions}")
    
    print("\nHow it works:")
    print("  1. Start at root → move to 'c' node")
    print("  2. From 'c' → move to 'a' node")
    print("  3. Found 'ca' node! Now collect ALL words under it")
    print("  4. Results: cat, car, card")
    
    print_section("STEP 4: Searching for Prefix 'd'")
    prefix = "d"
    suggestions = trie.search_prefix(prefix)
    
    print(f"\nSearching for words starting with '{prefix}'...")
    print(f"✓ Found {len(suggestions)} suggestions: {suggestions}")
    
    print_section("STEP 5: Searching for Non-Existent Prefix 'xyz'")
    prefix = "xyz"
    suggestions = trie.search_prefix(prefix)
    
    print(f"\nSearching for words starting with '{prefix}'...")
    print(f"✗ Found {len(suggestions)} suggestions: {suggestions}")
    print("\nWhy? The Trie doesn't have a path for 'x', so it returns empty.")

def demo_fantasy_autocomplete():
    """Show a more realistic example with fantasy words"""
    
    print_section("REAL-WORLD EXAMPLE: Fantasy Game Autocomplete")
    
    trie = Trie()
    fantasy_words = [
        "dragon", "druid", "dwarf",
        "magic", "mage", "mana",
        "sword", "spell", "shield",
        "warrior", "wizard", "wand"
    ]
    
    print("\nInserting fantasy game terms...")
    for word in fantasy_words:
        trie.insert(word)
    print(f"✓ Loaded {len(fantasy_words)} words")
    
    print("\n" + "-" * 70)
    print("Now imagine you're typing in a game search box...")
    print("-" * 70)
    
    test_prefixes = ["dr", "ma", "w", "sp"]
    
    for prefix in test_prefixes:
        suggestions = trie.search_prefix(prefix)
        print(f"\n  You type: '{prefix}'")
        print(f"  Autocomplete shows: {suggestions}")

def demo_why_trie_is_fast():
    """Explain why Trie is efficient"""
    
    print_section("WHY USE A TRIE? (Performance)")
    
    print("\n📊 Comparison:")
    print("\n  Method 1: Simple List Search (Slow)")
    print("  - Loop through ALL words")
    print("  - Check if each starts with prefix")
    print("  - Time: O(n × m) where n=words, m=word length")
    
    print("\n  Method 2: Trie (Fast!) ✨")
    print("  - Follow the prefix path directly")
    print("  - Only collect words under that path")
    print("  - Time: O(p + k) where p=prefix length, k=results")
    
    print("\n💡 Example: 1,000,000 words, prefix 'ca'")
    print("  - List: Check all 1,000,000 words 😱")
    print("  - Trie: Follow 'c'→'a', get only relevant words 🚀")

def main():
    """Run all demonstrations"""
    print("\n")
    print("🎓 TRIE DATA STRUCTURE - COMPLETE EXPLANATION")
    print("=" * 70)
    
    demo_basic_trie()
    demo_fantasy_autocomplete()
    demo_why_trie_is_fast()
    
    print_section("KEY TAKEAWAYS")
    print("""
    ✓ Trie = Tree structure that stores strings by prefix
    ✓ Words with same prefix share the same path
    ✓ Perfect for autocomplete (fast prefix search)
    ✓ Much faster than checking every word in a list
    
    Real-world uses:
    - Google search suggestions
    - Phone contact search
    - IDE code completion
    - Spell checkers
    """)
    
    print("\n" + "=" * 70)
    print("Now try running: python main.py")
    print("You'll see this in action with AI-generated words!")
    print("=" * 70 + "\n")

if __name__ == "__main__":
    main()
