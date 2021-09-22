def format_name(f_name, l_name):
    if f_name == "" or l_name =="":
        return "You did'nt enter a valid name."

    formatted_name = (f_name + " " + l_name).title()    
    return formatted_name

print(format_name(input("Enter your first name: "), input("Enter your last name: ")))