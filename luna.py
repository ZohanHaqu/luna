import sys
import os

# Function to convert Luna commands to Python syntax
def luna_to_python(command):
    # A simple dictionary to map Luna commands to Python commands
    luna_commands = {
        "print": "print",   # Print command
        "input": "input",   # Input command
        "if": "if",         # If statement
        "else": "else",     # Else statement
        "for": "for",       # For loop
        "while": "while",   # While loop
        "def": "def",       # Function definition
        "return": "return", # Return command
        "break": "break",   # Break statement
        "continue": "continue" # Continue statement
    }

    # Handle multi-line statements and indents properly
    for luna_cmd, py_cmd in luna_commands.items():
        if command.strip().lower().startswith(luna_cmd):
            # Convert command and handle indentation
            return command.replace(luna_cmd, py_cmd, 1)
    
    # If no specific Luna command found, just return the command as-is
    return command

# Function to load and execute a script
def load_script(file_path):
    try:
        # Open the file and read the content
        with open(file_path, "r") as file:
            luna_script = file.read()

        # Convert the Luna script to Python
        python_script = ""
        for line in luna_script.splitlines():
            python_script += luna_to_python(line) + '\n'

        # Execute the converted Python script
        exec(python_script)
        print(f"Successfully executed {file_path}")
    
    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"Error executing script {file_path}: {e}")

# Function to display help
def display_help():
    help_text = """
    Welcome to the Luna Shell Help!

    Available Commands:
    1. 'load <filename>' - Load and execute a Luna script file (.lna).
    2. 'exit' - Exit the Luna Shell.
    3. 'help' - Display this help message.
    4. 'clear' - Clear the terminal screen.

    Luna Programming Language:
    - Luna commands are similar to Python syntax.
    - The language supports basic commands like 'print', 'input', 'if', 'for', 'while', and 'def'.
    - Functions can be defined using 'def <function_name>(<args>):'.
    - To print output, use 'print(<message>)'.
    - To take input from the user, use 'input(<prompt>)'.

    Luna Functions:
    1. print(<message>) - Outputs a message to the console.
    2. input(<prompt>) - Takes input from the user. The prompt is optional.
    3. if <condition>: - A conditional statement.
    4. else: - An else branch for if conditions.
    5. for <variable> in <iterable>: - A loop that iterates over an iterable.
    6. while <condition>: - A loop that runs while the condition is true.
    7. def <function_name>(<args>): - Function definition.
    8. return <value> - Return a value from a function.
    9. break - Exit the nearest loop.
    10. continue - Skip the rest of the current loop iteration.

    Enjoy using Luna Shell!
    """
    print(help_text)

# Function to clear the terminal screen
def clear_screen():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Linux and macOS
    else:
        os.system('clear')

# Main loop for Luna Shell
def luna_shell():
    # New welcome text
    print("Luna Programming Language Version 1.0\n")
    print("Luna was brought to you by:")
    print("\nZohan Haque (Lead Developer)")
    print("Zohan Haque's Software (Company that developed it)\n")
    print("Welcome to the Luna Shell! Type 'exit' to quit, or 'load <filename>' to load a script.")
    print("Type 'help' to view the available commands.\n")
    
    while True:
        # Get the user input (Luna command)
        luna_command = input("LunaShell> ")

        # Check for exit condition
        if luna_command.lower() == 'exit':
            print("Exiting Luna Shell...")
            break

        # Check for help command
        elif luna_command.lower() == 'help':
            display_help()

        # Check for clear command
        elif luna_command.lower() == 'clear':
            clear_screen()

        # Check if the user wants to load a script
        elif luna_command.lower().startswith('load '):
            file_path = luna_command[5:].strip()  # Extract file path after 'load '
            load_script(file_path)
        else:
            # Convert the Luna command to Python
            python_command = luna_to_python(luna_command)

            try:
                # Execute the Python command
                exec(python_command)
            except Exception as e:
                print(f"Error executing command: {e}")

# Run the Luna Shell
if __name__ == "__main__":
    luna_shell()
