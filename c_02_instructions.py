# Generates headings (eg: ---- Heading ----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration}")


# Display instructions
def instructions():
    statement_generator("instructions", "-")

    print('''
instructions go here.
- instruction 1  
- instruction 2
- etc  
    ''')




# Main routine goes here

# Display instructions if requested
want_instructions = input("press <enter> to read the instructions"
                          "or any key to continue ")

if want_instructions == "":
    instructions()
print ("program continues")