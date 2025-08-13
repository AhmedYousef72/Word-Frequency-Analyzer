#!/usr/bin/env python3
"""
Word Frequency Analyzer
Analyzes a text file and reports the most frequent words.
"""

import sys
import re
import os
from collections import Counter
from typing import List, Tuple

class WordFrequencyAnalyzer:
    def __init__(self):
        self.word_count = {}
        
    def read_file(self, file_path: str) -> str:
        """Read and return the content of a text file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
            sys.exit(1)
        except Exception as e:
            print(f"Error reading file: {e}")
            sys.exit(1)
    
    def clean_and_split_text(self, text: str) -> List[str]:
        """Clean text and split into words, removing punctuation and converting to lowercase."""
        # Convert to lowercase
        text = text.lower()
        
        # Remove punctuation and split into words
        # This regex keeps only letters and spaces
        words = re.findall(r'\b[a-z]+\b', text)
        
        # Filter out empty strings and very short words (optional)
        words = [word for word in words if len(word) > 1]
        
        return words
    
    def count_words(self, words: List[str]) -> Counter:
        """Count the frequency of each word."""
        return Counter(words)
    
    def get_top_words(self, word_counter: Counter, top_n: int = 10) -> List[Tuple[str, int]]:
        """Get the top N most frequent words."""
        return word_counter.most_common(top_n)
    
    def display_results(self, top_words: List[Tuple[str, int]], total_words: int):
        """Display the results in a formatted way."""
        print("\n" + "="*50)
        print("WORD FREQUENCY ANALYSIS RESULTS")
        print("="*50)
        print(f"Total words analyzed: {total_words}")
        print(f"Unique words found: {len(self.word_count)}")
        print("\nTop 10 Most Frequent Words:")
        print("-" * 30)
        
        for i, (word, count) in enumerate(top_words, 1):
            percentage = (count / total_words) * 100
            print(f"{i:2d}. {word:<15} {count:>5} ({percentage:.1f}%)")
    
    def create_simple_bar_chart(self, top_words: List[Tuple[str, int]]):
        """Create a simple text-based bar chart (Bonus feature)."""
        if not top_words:
            return
            
        print("\n" + "="*50)
        print("VISUAL REPRESENTATION")
        print("="*50)
        
        max_count = top_words[0][1]  # Highest frequency
        max_bar_length = 40  # Maximum bar length in characters
        
        for word, count in top_words:
            # Calculate bar length proportional to frequency
            bar_length = int((count / max_count) * max_bar_length)
            bar = "█" * bar_length
            print(f"{word:<12} |{bar} {count}")
    
    def analyze_file(self, file_path: str, show_chart: bool = False):
        """Main method to analyze a file and display results."""
        print(f"Analyzing file: {file_path}")
        
        # Read file content
        content = self.read_file(file_path)
        
        # Clean and split text into words
        words = self.clean_and_split_text(content)
        
        if not words:
            print("No words found in the file.")
            return
        
        # Count word frequencies
        self.word_count = self.count_words(words)
        
        # Get top 10 words
        top_words = self.get_top_words(self.word_count, 10)
        
        # Display results
        self.display_results(top_words, len(words))
        
        # Show bar chart if requested (bonus feature)
        if show_chart:
            self.create_simple_bar_chart(top_words)

def main():
    """Main function to handle command line arguments and run the analyzer."""
    if len(sys.argv) < 2:
        print("Usage: python analyzer.py <file_path> [--chart]")
        print("Example: python analyzer.py sample.txt")
        print("Example: python analyzer.py sample.txt --chart")
        sys.exit(1)
    
    file_path = sys.argv[1]
    show_chart = '--chart' in sys.argv
    
    # Check if file exists
    if not os.path.exists(file_path):
        print(f"Error: File '{file_path}' does not exist.")
        sys.exit(1)
    
    # Create analyzer and run analysis
    analyzer = WordFrequencyAnalyzer()
    analyzer.analyze_file(file_path, show_chart)

if __name__ == "__main__":
    main()