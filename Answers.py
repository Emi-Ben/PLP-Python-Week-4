# 1  Function to read a file and write modified content to a new file
def modify_file(input_file, output_file):
    try:
        # Open the input file in read mode
        with open(input_file, 'r') as file:
            content = file.read()
        
        # Modify the content (e.g., convert to uppercase)
        modified_content = content.upper()

        # Open the output file in write mode and write the modified content
        with open(output_file, 'w') as file:
            file.write(modified_content)
        print(f"Content has been modified and saved to {output_file}")
    
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
input_file = 'input.txt'  # Replace with your input file path
output_file = 'output.txt'  # Replace with your output file path
modify_file(input_file, output_file)



# 2 Function to ask for a filename and handle errors
def read_file():
    filename = input("Please enter the filename: ")

    try:
        # Try to open the file in read mode
        with open(filename, 'r') as file:
            content = file.read()
            print("File content successfully read:")
            print(content)

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")

    except PermissionError:
        print(f"Error: You do not have permission to read the file '{filename}'.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to read a file
read_file()
