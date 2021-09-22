def format_name(f_name, l_name):
    """Take a first and last name and format it to return the title case version of the name."""

    if f_name == "" or l_name =="":
        return "You did'nt enter a valid name."

    formatted_name = (f_name + " " + l_name).title()    
    return formatted_name

print(format_name(input("Enter your first name: "), input("Enter your last name: ")))
print(format_name.__doc__)