from schema import *
from google import genai
from google.genai.types import GenerateContentConfig
from trie import Trie
import os

from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

# Ensure you have your API key set up (e.g., as an environment variable)
client = genai.Client(api_key = api_key) 
    

def generate_and_load_trie(theme: str, num_words: int, trie: Trie):
    """
    Generates structured content using Gemini, validates with Pydantic,
    and loads the words into the Trie.
    """
    prompt = f"Generate exactly {num_words} unique words and phrases related to the theme of '{theme}' for an autocomplete feature."

    # Use the Pydantic model as the response_schema
    config = GenerateContentConfig(
        response_mime_type="application/json",
        response_schema=ThemedWordList,
    )

    print(f"Generating content for theme: '{theme}'...")
    response = client.models.generate_content(
        model="gemini-2.5-flash", # Use a fast model like flash
        contents=prompt,
        config=config,
    )

    # The response.parsed attribute automatically gives you an instantiated Pydantic object
    try:
        word_list_object: ThemedWordList = response.parsed

        # Load the generated words into the Trie
        for word in word_list_object.words:
            trie.insert(word.lower()) # Convert to lowercase for case-insensitive autocomplete
        
        print(f"Successfully loaded {len(word_list_object.words)} words into the Trie.")
        return word_list_object.words

    except Exception as e:
        print(f"Error parsing structured response or loading Trie: {e}")
        print("Raw response text:", response.text)
        return []

# --- Execution ---
def main():
    """Interactive autocomplete demo"""
    print("=" * 70)
    print("TRIE AUTOCOMPLETE WITH GEMINI API")
    print("=" * 70)
    
    # Get theme from user
    print("\nAvailable themes: space, cooking, technology, ocean, fantasy, sports, music, mythical creatures")
    theme = input("Enter a theme: ").strip() or "fantasy"
    
    # Get number of words
    try:
        num_words = int(input("How many words to generate? (default 30): ").strip() or "30")
    except ValueError:
        num_words = 30
    
    # Generate and load words
    my_trie = Trie()
    theme_words = generate_and_load_trie(theme, num_words, my_trie)
    
    if not theme_words:
        print("Failed to generate words. Exiting.")
        return
    
    print(f"\n✓ Generated words: {', '.join(theme_words[:10])}{'...' if len(theme_words) > 10 else ''}")
    
    # Automatically visualize the Trie structure (show complete words)
    my_trie.visualize(max_depth=20)  # Set high enough to show full words
    
    # Interactive autocomplete
    print("\n" + "=" * 70)
    print("AUTOCOMPLETE DEMO")
    print("=" * 70)
    print("Type a prefix to get suggestions (or 'quit' to exit)")
    
    while True:
        prefix = input("\nEnter prefix: ").strip()
        
        if prefix.lower() == 'quit':
            break
        
        if not prefix:
            continue
        
        suggestions = my_trie.search_prefix(prefix.lower())
        
        if suggestions:
            print(f"✓ Suggestions for '{prefix}': {suggestions}")
        else:
            print(f"✗ No suggestions found for '{prefix}'")
    
    print("\nThanks for using Trie Autocomplete!")

if __name__ == "__main__":
    main()