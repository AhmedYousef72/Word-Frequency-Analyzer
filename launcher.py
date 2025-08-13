#!/usr/bin/env python3
"""
Word Frequency Analyzer Launcher
Choose between Command Line Interface (CLI) or Graphical User Interface (GUI)
"""

import sys
import os

def show_menu():
    """Display the launcher menu."""
    print("\n" + "="*50)
    print("  WORD FREQUENCY ANALYZER")
    print("="*50)
    print("Choose your preferred interface:")
    print()
    print("1. Command Line Interface (CLI)")
    print("   - Fast and simple")
    print("   - Great for scripts and automation")
    print("   - Usage: python analyzer.py <file> [--chart]")
    print()
    print("2. Graphical User Interface (GUI)")
    print("   - User-friendly with visual charts")
    print("   - Interactive file browser")
    print("   - Beautiful data visualization")
    print()
    print("3. Exit")
    print("="*50)

def launch_cli():
    """Launch the CLI version."""
    print("\nLaunching CLI version...")
    print("Note: You can also run 'python analyzer.py <filename>' directly")
    
    if len(sys.argv) > 1:
        # If file argument provided, use it
        os.system(f"python analyzer.py {' '.join(sys.argv[1:])}")
    else:
        # Ask for file input
        filename = input("Enter the path to your text file: ").strip()
        if filename:
            chart_option = input("Show chart? (y/n): ").strip().lower()
            chart_flag = "--chart" if chart_option == 'y' else ""
            os.system(f"python analyzer.py \"{filename}\" {chart_flag}")

def launch_gui():
    """Launch the GUI version."""
    print("\nLaunching GUI version...")
    try:
        os.system("python analyzer_gui.py")
    except Exception as e:
        print(f"Error launching GUI: {e}")
        print("Make sure you have tkinter and matplotlib installed:")
        print("pip install matplotlib")

def main():
    """Main launcher function."""
    
    # If command line arguments provided, launch CLI directly
    if len(sys.argv) > 1 and sys.argv[1].endswith('.txt'):
        launch_cli()
        return
    
    while True:
        show_menu()
        
        try:
            choice = input("\nEnter your choice (1-3): ").strip()
            
            if choice == '1':
                launch_cli()
                break
            elif choice == '2':
                launch_gui()
                break
            elif choice == '3':
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")
                
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()