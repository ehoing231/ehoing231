#!/usr/bin/env python3
"""
Random Joke Generator using JokeAPI

This script fetches random jokes from the JokeAPI and displays them in the terminal.
It supports multiple categories and can be used as a command-line tool.

API: https://jokeapi.dev/
"""

import requests
import json
import sys
from typing import Dict, Optional


class JokeGenerator:
    """Fetches and displays random jokes from JokeAPI."""
    
    BASE_URL = "https://v2.jokeapi.dev/joke"
    
    CATEGORIES = [
        'Any',
        'General',
        'Knock-Knock',
        'Programming',
        'Dark',
        'Pun',
        'Spooky'
    ]
    
    def __init__(self):
        """Initialize the JokeGenerator."""
        self.session = requests.Session()
    
    def get_joke(self, category: str = 'Any', safe_mode: bool = False) -> Optional[str]:
        """
        Fetch a random joke from the API.
        
        Args:
            category: The joke category (default: 'Any')
            safe_mode: Whether to filter unsafe content (default: False)
            
        Returns:
            Formatted joke string or None if error occurs
        """
        try:
            url = f"{self.BASE_URL}/{category}"
            params = {}
            
            if safe_mode:
                params['safe-mode'] = True
            
            response = self.session.get(url, params=params, timeout=5)
            response.raise_for_status()
            
            data = response.json()
            
            if data.get('error'):
                print(f"Error: {data.get('message', 'Unknown error')}")
                return None
            
            # Format joke based on type
            if data['type'] == 'single':
                return data['joke']
            elif data['type'] == 'twopart':
                return f"{data['setup']}\n\n{data['delivery']}"
            
        except requests.exceptions.RequestException as e:
            print(f"Network error: {e}")
            return None
        except json.JSONDecodeError:
            print("Error parsing response")
            return None
    
    def get_multiple_jokes(self, count: int = 5, category: str = 'Any') -> list:
        """
        Fetch multiple random jokes.
        
        Args:
            count: Number of jokes to fetch
            category: The joke category
            
        Returns:
            List of joke strings
        """
        jokes = []
        for i in range(count):
            joke = self.get_joke(category)
            if joke:
                jokes.append(joke)
        return jokes
    
    def list_categories(self) -> None:
        """Display available categories."""
        print("\nAvailable joke categories:")
        for i, category in enumerate(self.CATEGORIES, 1):
            print(f"  {i}. {category}")
        print()
    
    def display_joke(self, joke: str) -> None:
        """Display a formatted joke."""
        print("\n" + "="*60)
        print(joke)
        print("="*60 + "\n")


def main():
    """
    Main function to run the joke generator from command line.
    """
    generator = JokeGenerator()
    
    print("\n🎭 Welcome to the Random Joke Generator! 🎭\n")
    
    if len(sys.argv) > 1:
        if sys.argv[1] == '--list':
            generator.list_categories()
            return
        elif sys.argv[1] == '--help':
            print("Usage: python joke_generator.py [options]")
            print("\nOptions:")
            print("  --list    Show available joke categories")
            print("  --help    Show this help message")
            print("\nExamples:")
            print("  python joke_generator.py              # Get a random joke")
            print("  python joke_generator.py programming # Get a programming joke")
            return
        else:
            category = sys.argv[1]
            if category not in [c.lower() for c in generator.CATEGORIES]:
                print(f"Unknown category: {category}")
                generator.list_categories()
                return
            category = category.capitalize()
    else:
        category = 'Any'
    
    print(f"Fetching joke from category: {category}...\n")
    joke = generator.get_joke(category)
    
    if joke:
        generator.display_joke(joke)
        print("😂 Enjoyed the joke? Run again for more laughs!\n")
    else:
        print("Failed to get a joke. Please try again.\n")


if __name__ == "__main__":
    main()