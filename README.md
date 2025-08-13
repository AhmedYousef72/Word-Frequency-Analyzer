# Word Frequency Analyzer

A comprehensive text analysis tool that analyzes word frequency in text files with both command-line and graphical user interfaces.

## 📋 Project Overview

**Selected Option:** Option 3 - Word Frequency Analyzer  
**Programming Language:** Python 3.7+  
**Author:** Ahmed Yousef El Sayed  
**Submission Date:** August 13, 2025

This project analyzes text files to identify and visualize the most frequently used words, providing insights into text content through statistical analysis and visual representations.

## ✨ Features

### Core Requirements ✅
- **File Input:** Accepts any text file path as input
- **Text Processing:** Ignores punctuation and case sensitivity
- **Word Frequency Analysis:** Counts occurrence of each word
- **Top Results:** Displays the 10 most frequent words with their counts

### Bonus Features ✅
- **Visual Charts:** Interactive bar charts using matplotlib
- **Efficient Processing:** Optimized for large files using Python's Counter class
- **Multiple Interfaces:** Both CLI and GUI options for different user preferences
- **Statistical Summary:** Shows total words, unique words, and percentages
- **Professional Error Handling:** Graceful handling of missing files and edge cases

### Additional Features 🚀
- **Smart Launcher:** Interactive menu to choose between CLI and GUI
- **Text-based Charts:** ASCII bar charts in CLI mode
- **Professional GUI:** User-friendly interface with file browser and tabs
- **Comprehensive Statistics:** Detailed analysis beyond basic requirements
- **Cross-platform:** Works on Windows, macOS, and Linux

## 🛠️ Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Required Dependencies
```bash
pip install matplotlib
```

*Note: tkinter comes pre-installed with Python*

### Installation Steps
1. Clone or download the project files
2. Install dependencies: `pip install matplotlib`
3. You're ready to go!

## 🚀 Usage

### Option 1: Interactive Launcher (Recommended)
```bash
python launcher.py
```
This provides a user-friendly menu to choose between CLI and GUI interfaces.

### Option 2: Command Line Interface (CLI)
```bash
# Basic analysis
python analyzer.py sample.txt

# With text-based bar chart
python analyzer.py sample.txt --chart

# Help
python analyzer.py
```

**CLI Features:**
- Fast processing for automation
- Text-based visualization
- Perfect for scripts and batch processing
- Detailed console output with statistics

### Option 3: Graphical User Interface (GUI)
```bash
python analyzer_gui.py
```

**GUI Features:**
- Interactive file browser
- Beautiful matplotlib charts
- Tabbed interface (Results & Chart)
- Real-time statistics display
- User-friendly for non-technical users

## 📁 Project Structure

```
word-frequency-analyzer/
├── launcher.py          # Interactive launcher menu
├── analyzer.py          # Command-line interface
├── analyzer_gui.py      # Graphical user interface
├── sample.txt          # Sample text file for testing
└── README.md           # This documentation
```

## 🔧 Technical Implementation

### Core Algorithm
1. **File Reading:** UTF-8 encoding with error handling
2. **Text Cleaning:** Regex-based punctuation removal and case normalization
3. **Word Extraction:** Filters out single-character words and empty strings
4. **Frequency Counting:** Uses Python's optimized Counter class
5. **Result Processing:** Sorts and extracts top N results
6. **Visualization:** Both text-based and graphical chart generation

### Key Design Decisions
- **Object-Oriented Design:** Clean, maintainable code structure
- **Error Handling:** Comprehensive exception handling for edge cases
- **Type Hints:** Modern Python practices for better code documentation
- **Multiple Interfaces:** Serves both technical and non-technical users
- **Performance:** Efficient algorithms suitable for large files

### Code Quality Features
- **Documentation:** Comprehensive docstrings for all methods
- **Error Handling:** Graceful handling of file errors and edge cases
- **Code Organization:** Clean separation of concerns
- **Best Practices:** Follows PEP 8 style guidelines
- **Extensibility:** Easy to modify and extend functionality

## 📊 Sample Output

### CLI Output Example
```
==================================================
WORD FREQUENCY ANALYSIS RESULTS
==================================================
Total words analyzed: 1,247
Unique words found: 342

Top 10 Most Frequent Words:
------------------------------
 1. the            87 (7.0%)
 2. and            56 (4.5%)
 3. programming    34 (2.7%)
 4. code           28 (2.2%)
 5. software       25 (2.0%)
```

### GUI Features
- Interactive file selection dialog
- Real-time statistics display
- Professional matplotlib charts
- Tabbed interface for organized results
- Status bar with progress updates

## 🧪 Testing

The application has been thoroughly tested with:
- **Various file types:** .txt files with different encodings
- **Different text sizes:** From small samples to large documents
- **Edge cases:** Empty files, files with only punctuation, non-English characters
- **Error scenarios:** Missing files, permission errors, corrupted files

## 🎯 Why This Implementation?

### Technical Choices
- **Python:** Excellent for text processing with rich library ecosystem
- **tkinter:** Built-in GUI framework requiring no additional installations
- **matplotlib:** Industry-standard plotting library for data visualization
- **Counter class:** Optimized for frequency counting operations
- **Regex:** Robust text cleaning and word extraction

### User Experience
- **Multiple Interfaces:** Serves different user preferences and use cases
- **Professional Design:** Clean, intuitive interfaces
- **Error Prevention:** Input validation and user-friendly error messages
- **Flexibility:** Easy to modify for different requirements

## 🔮 Potential Enhancements

If given more time, potential improvements could include:
- **Language Detection:** Support for multiple languages
- **Export Options:** Save results to CSV, JSON, or PDF formats
- **Advanced Filtering:** Stop words removal, minimum word length settings
- **Batch Processing:** Analyze multiple files simultaneously
- **Web Interface:** Browser-based version for broader accessibility
- **Database Integration:** Store and compare analysis results over time

## 🤝 Development Process

This project demonstrates:
- **Requirements Analysis:** Carefully implemented all specified features
- **Incremental Development:** Built core features first, then added enhancements
- **User-Centered Design:** Created interfaces for different user types
- **Quality Assurance:** Thorough testing with various inputs
- **Documentation:** Comprehensive code documentation and user guides


*This project was developed as part of the Software Development Internship technical assignment, demonstrating programming fundamentals, problem-solving skills, and software design principles.*