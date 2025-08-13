#!/usr/bin/env python3
"""
Word Frequency Analyzer - GUI Version
A graphical user interface for analyzing word frequency in text files.
"""

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, scrolledtext
import re
import os
from collections import Counter
from typing import List, Tuple
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.figure

class WordFrequencyAnalyzerGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Frequency Analyzer")
        self.root.geometry("800x600")
        self.root.configure(bg='#f0f0f0')
        
        # Variables
        self.file_path = tk.StringVar()
        self.word_count = {}
        self.total_words = 0
        
        self.create_widgets()
        
    def create_widgets(self):
        """Create and arrange all GUI widgets."""
        
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="Word Frequency Analyzer", 
                               font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # File selection frame
        file_frame = ttk.LabelFrame(main_frame, text="File Selection", padding="10")
        file_frame.grid(row=1, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(0, 10))
        file_frame.columnconfigure(1, weight=1)
        
        ttk.Label(file_frame, text="Text File:").grid(row=0, column=0, sticky=tk.W, padx=(0, 5))
        
        file_entry = ttk.Entry(file_frame, textvariable=self.file_path, width=50)
        file_entry.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(0, 5))
        
        browse_btn = ttk.Button(file_frame, text="Browse", command=self.browse_file)
        browse_btn.grid(row=0, column=2, padx=(5, 0))
        
        # Analyze button
        analyze_btn = ttk.Button(main_frame, text="Analyze File", 
                                command=self.analyze_file, style='Accent.TButton')
        analyze_btn.grid(row=2, column=0, columnspan=3, pady=10)
        
        # Results notebook (tabs)
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.grid(row=3, column=0, columnspan=3, sticky=(tk.W, tk.E, tk.N, tk.S), pady=(0, 10))
        main_frame.rowconfigure(3, weight=1)
        
        # Results tab
        self.results_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.results_frame, text="Results")
        
        # Create results widgets
        self.create_results_widgets()
        
        # Chart tab
        self.chart_frame = ttk.Frame(self.notebook)
        self.notebook.add(self.chart_frame, text="Chart")
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready - Select a text file to analyze")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, 
                              relief=tk.SUNKEN, anchor=tk.W)
        status_bar.grid(row=4, column=0, columnspan=3, sticky=(tk.W, tk.E), pady=(10, 0))
    
    def create_results_widgets(self):
        """Create widgets for the results tab."""
        
        # Statistics frame
        stats_frame = ttk.LabelFrame(self.results_frame, text="Statistics", padding="10")
        stats_frame.pack(fill=tk.X, padx=10, pady=10)
        
        self.total_words_var = tk.StringVar(value="Total Words: 0")
        self.unique_words_var = tk.StringVar(value="Unique Words: 0")
        
        ttk.Label(stats_frame, textvariable=self.total_words_var, font=('Arial', 10, 'bold')).pack(anchor=tk.W)
        ttk.Label(stats_frame, textvariable=self.unique_words_var, font=('Arial', 10, 'bold')).pack(anchor=tk.W)
        
        # Results frame
        results_label_frame = ttk.LabelFrame(self.results_frame, text="Top 10 Most Frequent Words", padding="10")
        results_label_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=(0, 10))
        
        # Treeview for results
        columns = ('Rank', 'Word', 'Count', 'Percentage')
        self.tree = ttk.Treeview(results_label_frame, columns=columns, show='headings', height=12)
        
        # Configure columns
        self.tree.heading('Rank', text='Rank')
        self.tree.heading('Word', text='Word')
        self.tree.heading('Count', text='Count')
        self.tree.heading('Percentage', text='Percentage')
        
        self.tree.column('Rank', width=60, anchor=tk.CENTER)
        self.tree.column('Word', width=150, anchor=tk.W)
        self.tree.column('Count', width=100, anchor=tk.CENTER)
        self.tree.column('Percentage', width=100, anchor=tk.CENTER)
        
        # Scrollbar for treeview
        scrollbar = ttk.Scrollbar(results_label_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    def browse_file(self):
        """Open file dialog to select a text file."""
        filename = filedialog.askopenfilename(
            title="Select Text File",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if filename:
            self.file_path.set(filename)
    
    def read_file(self, file_path: str) -> str:
        """Read and return the content of a text file."""
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            messagebox.showerror("Error", f"File '{file_path}' not found.")
            return ""
        except Exception as e:
            messagebox.showerror("Error", f"Error reading file: {e}")
            return ""
    
    def clean_and_split_text(self, text: str) -> List[str]:
        """Clean text and split into words."""
        text = text.lower()
        words = re.findall(r'\b[a-z]+\b', text)
        words = [word for word in words if len(word) > 1]
        return words
    
    def count_words(self, words: List[str]) -> Counter:
        """Count the frequency of each word."""
        return Counter(words)
    
    def get_top_words(self, word_counter: Counter, top_n: int = 10) -> List[Tuple[str, int]]:
        """Get the top N most frequent words."""
        return word_counter.most_common(top_n)
    
    def update_results_display(self, top_words: List[Tuple[str, int]], total_words: int):
        """Update the results display with analysis results."""
        
        # Clear previous results
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Update statistics
        unique_words = len(self.word_count)
        self.total_words_var.set(f"Total Words: {total_words:,}")
        self.unique_words_var.set(f"Unique Words: {unique_words:,}")
        
        # Add results to treeview
        for i, (word, count) in enumerate(top_words, 1):
            percentage = (count / total_words) * 100
            self.tree.insert('', tk.END, values=(
                i, 
                word.title(), 
                f"{count:,}", 
                f"{percentage:.1f}%"
            ))
    
    def create_chart(self, top_words: List[Tuple[str, int]]):
        """Create and display a bar chart."""
        
        # Clear previous chart
        for widget in self.chart_frame.winfo_children():
            widget.destroy()
        
        if not top_words:
            ttk.Label(self.chart_frame, text="No data to display", 
                     font=('Arial', 12)).pack(expand=True)
            return
        
        # Create matplotlib figure
        fig = matplotlib.figure.Figure(figsize=(10, 6), dpi=80)
        ax = fig.add_subplot(111)
        
        words = [word.title() for word, _ in top_words]
        counts = [count for _, count in top_words]
        
        # Create bar chart
        bars = ax.bar(words, counts, color='skyblue', edgecolor='navy', alpha=0.7)
        
        # Customize chart
        ax.set_title('Top 10 Most Frequent Words', fontsize=14, fontweight='bold')
        ax.set_xlabel('Words', fontsize=12)
        ax.set_ylabel('Frequency', fontsize=12)
        ax.tick_params(axis='x', rotation=45)
        
        # Add value labels on bars
        for bar, count in zip(bars, counts):
            height = bar.get_height()
            ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                   f'{count}', ha='center', va='bottom', fontsize=9)
        
        # Adjust layout
        fig.tight_layout()
        
        # Create canvas and add to GUI
        canvas = FigureCanvasTkAgg(fig, self.chart_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    def analyze_file(self):
        """Main method to analyze the selected file."""
        file_path = self.file_path.get().strip()
        
        if not file_path:
            messagebox.showwarning("Warning", "Please select a text file first.")
            return
        
        if not os.path.exists(file_path):
            messagebox.showerror("Error", f"File '{file_path}' does not exist.")
            return
        
        self.status_var.set("Analyzing file...")
        self.root.update()
        
        try:
            # Read file content
            content = self.read_file(file_path)
            if not content:
                return
            
            # Clean and split text into words
            words = self.clean_and_split_text(content)
            
            if not words:
                messagebox.showinfo("Info", "No words found in the file.")
                self.status_var.set("Ready")
                return
            
            # Count word frequencies
            self.word_count = self.count_words(words)
            self.total_words = len(words)
            
            # Get top 10 words
            top_words = self.get_top_words(self.word_count, 10)
            
            # Update displays
            self.update_results_display(top_words, self.total_words)
            self.create_chart(top_words)
            
            # Switch to results tab
            self.notebook.select(0)
            
            self.status_var.set(f"Analysis complete - {self.total_words:,} words analyzed")
            
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred during analysis: {e}")
            self.status_var.set("Ready")

def main():
    """Main function to run the GUI application."""
    root = tk.Tk()
    
    # Configure style
    style = ttk.Style()
    style.theme_use('clam')
    
    # Create and run the application
    app = WordFrequencyAnalyzerGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()