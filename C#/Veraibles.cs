Console.Title = "Veraibles"
import os, sys
sys.path.append(os.getcwd()) # Adds the current directory to the system path for module import access
from veraibles_core import VeraiblesCore

# Create an instance of the VeraiblesCore class with default settings
vc = VeraiblesCore()

def main():
    """Main function that handles user input and runs appropriate methods in vc"""
    
    while True:  # Main loop for program execution
        print("\n")
        
        # Get user command from input
        cmd = input("> ")
        
        if cmd == 'exit':   # Exit command
            break          # End the loop and close the program
            
        elif cmd == 'help':  # Help command
            vc.printHelp()  # Print help message
            
        else:               # If no valid commands are entered  