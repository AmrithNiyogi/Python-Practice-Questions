# Define a function to create a password
def create_password():
    # Prompt the user to create a password and store the input in the variable 'password'
    password = input("Create your password: ")
    # Return the created password
    return password

# Define a function to check if the entered password matches the created password
def check_password(password, text):
    # Return True if the entered password matches the created password, otherwise False
    return password == text

# Ensure the code runs only if this script is executed directly
if __name__ == "__main__":
    # Initialize a variable to control the loop
    loop_break = False
    # Call the create_password function to create and store a password in 'pass_word'
    pass_word = create_password()
    
    # Continue looping until the password is verified
    while not loop_break:
        # Prompt the user to enter the password and store the input in 'txt'
        txt = input("Enter the password: ")
        # Check if the entered password matches the created password
        loop_break = check_password(pass_word, txt)
        
        # If the password is correct, print a verification message
        if loop_break:
            print("Password has been verified.")
        # If the password is incorrect, print an error message and prompt the user to try again
        else:
            print("Wrong password. Try again.")
