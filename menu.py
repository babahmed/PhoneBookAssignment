def options():
    # Create an entry variable using the input function and multiple line strings format
    print("Entry")
    entry = int(input("""
                    >>>Please select an option?<<<
                    1. List
                    2. Create
                    3. Find 
                    4. Modify
                    5. Delete
                    6. Exit
                    Enter your entry here(1,2,3 0r 4):  """))

# Close the function
    return entry
