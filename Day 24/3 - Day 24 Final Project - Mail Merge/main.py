#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
guests = []


with open("Input/Names/invited_names.txt", "r") as guest_list:
    guests = guest_list.readlines()
    guests = list(map(lambda x: x.rstrip(), guests))
    print(guests)

with open("Input/Letters/starting_letter.txt", "r") as starting_letter:
    letter = starting_letter.read()
    print(letter)
    print(guests)
    for guest in guests:
        edited_letter = letter.replace("[name]", guest)
        edited_letter = letter.replace("Angela", "Tushar")
        with open(f"Output/ReadyToSend/letter_for_{guest}.txt", "w") as new_letter:
            new_letter.write(edited_letter)
        
        
